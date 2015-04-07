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
{
    'name': 'Product manual variants',

    'summary': '''
        This addon disables automatic generation of product variants and intrudes a wizard
        for manual.
    ''',

    'description': '''
        Very useful for companies having very big portfolio of products with variants, when not all
        variants all valid.
    ''',

    'author': 'Litex Service Sp. z o.o.',
    'website': 'http://www.litex.pl',

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Usability',
    'version': '1.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'web_m2x_options'],
    
    'installable': True,
    
    'data': [
        'security/ir.model.access.csv',
        'wizards/manual_variant_creation_view.xml',
        'models/product_view.xml'
    ],

    'demo': ['data/product_manual_variants_demo.xml'],

    'tests': [
    ],
}
