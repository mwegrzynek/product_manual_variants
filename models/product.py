# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-Today Litex Service Sp. z o.o. 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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