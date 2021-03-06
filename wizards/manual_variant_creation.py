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
from openerp.models import TransientModel
from openerp.exceptions import Warning
from openerp import api, fields, _



class ManualVariantWizardLine(TransientModel):
    _name = 'product.manual_variant_wizard_line'
    _description = 'Manual Variant Creation Wizard Line'
    
    wizard_id = fields.Many2one('product.manual_variant_wizard', string='Wizard ID')
    attribute_id = fields.Many2one('product.attribute', string='Attribute')
    value_ids = fields.Many2many(
        'product.attribute.value', 
        relation='manual_variant_wizard_lines_values_rel', 
        column1='line_id', 
        column2='val_id', 
        string='Product Attribute Value'
    )
    available_value_ids = fields.Many2many(
        'product.attribute.value', 
        relation='manual_variant_wizard_lines_available_values_rel', 
        column1='wizard_id', 
        column2='val_id', 
        string='Available product attribute values'
    )
    
    
class ManualVariantWizard(TransientModel):
    _name = 'product.manual_variant_wizard'
    _description = 'Manual Variant Creation Wizard'
    _rec_name = 'id'
    
    def _default_product_template_id(self):
        return self.env['product.template'].browse(self._context.get('active_id'))
    
    product_template_id = fields.Many2one('product.template', string='Product template', default=_default_product_template_id, required=True, ondelete='cascade')
    line_ids = fields.One2many('product.manual_variant_wizard_line', inverse_name='wizard_id', string='Attribute lines', required=True)
    
    @api.onchange('product_template_id')
    def _on_change_product_template_id(self):
        # You can not just add ManualVariantWizardLine instances! Instead, return a list of their create dicts
        attrs = []

        for line in self.product_template_id.attribute_line_ids:
            attrs.append(dict(
                attribute_id=line.attribute_id.id,
                available_value_ids=[(6, 0, line.value_ids.mapped('id'))]
            ))
           
        self.line_ids = attrs

    @api.one
    def create_variants(self):
        cur_templ = self.product_template_id
        if cur_templ:
            # Verify, all attribute values are allowed
            template_value_ids = {val.id for line in cur_templ.attribute_line_ids for val in line.value_ids}
            wizard_value_ids = {val.id: val.name for line in self.line_ids for val in line.value_ids}        
            
            extra_value_id_names = [wizard_value_ids[val_id] for val_id in set(wizard_value_ids) - set(template_value_ids)]
            if extra_value_id_names:
                raise Warning(_('The following attributes are not defined in the template and can not be used:') + '\n' + ','.join(extra_value_id_names))
            
            value_lists = [[val.id for val in line.value_ids] for line in self.line_ids]
            
            cur_templ.manually_create_variant_ids(value_lists)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }