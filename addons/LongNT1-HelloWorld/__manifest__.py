# -*- coding: utf-8 -*-
{
    'name': "LongNT1-HelloWorld",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product','web','vietNamAddressAutofill',],


    'installable': True,
    'auto_install': False,
    'application': True,

    # always loaded
    'data': [
        'security/people_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_bds.xml',
        'views/category.xml',
        'views/tre_product_follow.xml',
        'views/menu_item.xml',
        'data/product_direction.xml',
        'data/product_type.xml',
        
    ],


    'assets': {
    'web.assets_backend': [
        # 'web/static/src/js/legacy/public/public_widget.js',  
        # 'web/static/src/js/fields/basic_fields.js',  
        # 'web/static/src/js/fields/field_registry.js',  
        #'LongNT1-HelloWorld/static/src/js/custom_keothaanh.js',  
        'LongNT1-HelloWorld/static/src/css/an_chatter.css',
        #'LongNT1-HelloWorld/static/src/xml/many2many_binary_custom.xml',
        #'LongNT1-HelloWorld/static/src/js/many2many_binary_custom.js',
        
    ],
},
    


    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    
}

