# -*- coding: utf-8 -*-
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
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],
    
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
