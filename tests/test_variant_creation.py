# -*- coding: UTF-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.tests import common
from openerp.tools import mute_logger


class TestVariantCreation(common.TransactionCase):
    
    def setUp(self):
        super(TestVariantCreation, self).setUp()
        self.ProductTemplate = self.env['product.template']
        self.AttributeLine = self.env['product.attribute.line']        
    
    @mute_logger('openerp.addons.base.ir.ir_model', 'openerp.osv.orm')
    def test_manual_variant_creation(self):
        
        # Create product template
        prd = self.ProductTemplate.create(dict(
            name='Test template'
        ))
        
        self.assertEqual(prd.product_variant_count, 0)
        
        # Assign attribute lines
        al1 = self.AttributeLine.create(dict(
            product_tmpl_id=prd.id,
            attribute_id=self.ref('product.product_attribute_1')
        ))
        al1.value_ids += self.env.ref('product.product_attribute_value_1')
        al1.value_ids += self.env.ref('product.product_attribute_value_2')
        
        al2 = self.AttributeLine.create(dict(
            product_tmpl_id=prd.id,
            attribute_id=self.ref('product.product_attribute_2')
        ))
        al2.value_ids += self.env.ref('product.product_attribute_value_3')
        al2.value_ids += self.env.ref('product.product_attribute_value_4')
        
        prd.attribute_line_ids += al1
        prd.attribute_line_ids += al2
        
        self.env.cr.commit()
        
        # There should be no product variants        
        self.assertEqual(prd.product_variant_count, 0)
                
        prd.manually_create_variant_ids([
            [self.env.ref('product.product_attribute_value_1'), self.env.ref('product.product_attribute_value_1')],
            [self.env.ref('product.product_attribute_value_4')]
        ])
        