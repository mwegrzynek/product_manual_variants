# -*- coding: utf-8 -*-
import itertools


from openerp import api
from openerp.models import Model


class Product(Model):
    _name = 'product.template'
    _inherit = 'product.template'

    def create_variant_ids(self, cr, uid, ids, context=None):
        '''
        Disable automatic variant generation
        '''
        return True
    
    @api.multi
    def manually_create_variant_ids(self, value_lists):
        '''
        Based on original create_variant_ids
        '''
        ctx = self.env.context.copy() 
        
        if ctx.get('create_product_variant'):
            return None

        ctx.update(active_test=False, create_product_variant=True)

        for tmpl_id in self:

            # list of values combination
            all_variants = itertools.product(*value_lists)

            # check product
            variant_ids_to_active = []
            variants_active_ids = []
            variants_inactive = []
            for product_id in tmpl_id.product_variant_ids:
                variants = map(int,product_id.attribute_value_ids)
                if variants in all_variants:
                    variants_active_ids.append(product_id.id)
                    all_variants.pop(all_variants.index(variants))
                    if not product_id.active:
                        variant_ids_to_active.append(product_id.id)
                else:
                    variants_inactive.append(product_id)
            if variant_ids_to_active:
                product_obj.write(cr, uid, variant_ids_to_active, {'active': True}, context=ctx)

            # create new product
            for variant_ids in all_variants:
                values = {
                    'product_tmpl_id': tmpl_id.id,
                    'attribute_value_ids': [(6, 0, variant_ids)]
                }
                id = product_obj.create(cr, uid, values, context=ctx)
                variants_active_ids.append(id)

            # unlink or inactive product
            for variant_id in map(int,variants_inactive):
                try:
                    with cr.savepoint():
                        product_obj.unlink(cr, uid, [variant_id], context=ctx)
                except (psycopg2.Error, osv.except_osv):
                    product_obj.write(cr, uid, [variant_id], {'active': False}, context=ctx)
                    pass
        return True