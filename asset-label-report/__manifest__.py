# -*- coding: utf-8 -*-
{
    'name': "Assets Label Report",

    'summary': """
        Asset report with basic information""",

    'description': """
        Adds report to asset with Name and custom asset number, suitable for printing labels.
    """,

    'author': "amondi Media d.o.o. // Matija Gudlin",
    'website': "https://amondi-media.com",
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_asset', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/assets_label_report.xml',
        'views/assets_view.xml',
        'views/assets_form.xml',
    ],
}
