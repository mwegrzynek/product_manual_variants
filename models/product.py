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
        
        Product = self.env['product.product'].with_context(ctx)

        for tmpl_id in self:

            existing_variants = {tuple([val.id for val in var.attribute_value_ids]) for var in tmpl_id.product_variant_ids}
            all_variants = set(itertools.product(*value_lists))
                            
            variants_to_create = all_variants - existing_variants

            for variant_ids in variants_to_create:
                Product.create(dict(
                    product_tmpl_id=tmpl_id.id,
                    attribute_value_ids=[(6, 0, variant_ids)]
                ))

        return True