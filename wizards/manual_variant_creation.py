# -*- coding: utf-8 -*-
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
################################################################################
from openerp.models import TransientModel
from openerp import api, fields


class ManualVariantWizardLine(TransientModel):
    _name = 'product.manual_variant_wizard_line'
    _description = 'Manual Variant Creation Wizard Line'
    
    wizard_id = fields.Many2one('product.manual_variant_wizard', string='Wizard ID')
    attribute_id = fields.Many2one('product.attribute', string='Attribute')
    value_ids = fields.Many2many('product.attribute.value', relation='manual_variant_wizard_lines_values_rel', column1='line_id', column2='val_id', string='Product Attribute Value')
    
    
class ManualVariantWizard(TransientModel):
    _name = 'product.manual_variant_wizard'
    _description = 'Manual Variant Creation Wizard'
    _rec_name = 'id'
    
    @api.multi
    def _default_line_ids(self):
        res = []
        cur_templ = self.env['product.template'].browse(self._context.get('active_id'))
        
        if cur_templ:
            # We were run from product template form, fill the lines
            for line in cur_templ.attribute_line_ids:
                res.append(dict(
                    attribute_id=line.attribute_id.id#,
                    #value_ids=[val.id for val in line.value_ids]
                ))
        return res
    
    
    #product_template_id = fields.Many2many('product.template', string='Product template')
    line_ids = fields.One2many('product.manual_variant_wizard_line', inverse_name='wizard_id', string='Attribute lines', default=_default_line_ids)
        
    @api.one
    def create_variants(self):
        cur_templ = self.env['product.template'].browse(self._context.get('active_id'))
        
        if cur_templ:
            value_lists = [[val.id for val in line.value_ids] for line in self.line_ids]
            print value_lists
            cur_templ.manually_create_variant_ids(value_lists)
        return False