# -*- coding: utf-8 -*-
{
    'name': "product_manual_variants",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],
    'data': ["security/ir.model.access.csv"],

    'demo': ["data/product_manual_variants_demo.xml"],

    'tests': [
    ],
}
