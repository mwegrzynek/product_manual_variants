# -*- coding: utf-8 -*-
from openerp.models import Model


class Product(Model):
    _name = 'product.template'
    _inherit = 'product.template'

    def create_variant_ids(self, cr, uid, ids, context=None):
        '''
        Disable automatic variant generation
        '''
        return True
    
