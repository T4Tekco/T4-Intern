# -*- coding: utf-8 -*-
{
    'name': "HungVP-Hello_Odoo 3",
    'version': '1.0',

    # Loại module
    'category': 'Tutorial',

    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    #### Chấp nhận số âm
    'sequence': 5,

    # Mô tả module
    'summary': 'App to manage custom data with user permissions',
    'description': """This module provides a custom app with viewer and creator permissions.""",


    # Module dựa trên các category nào
    # Khi hoạt động, category trong 'depends' phải được install
    ### rồi module này mới đc install
    'depends': [],

    # Module có được phép install hay không
    # Nếu bạn thắc mắc nếu tắt thì làm sao để install
    # Bạn có thể dùng 'auto_install'
    'installable': True,
    'auto_install': False,
    'application': True,

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/teacher_view.xml',    
        'views/teacher_data.xml',  # Đường dẫn đến tệp XML mới
        'views/course_list_template.xml',
        'views/menu_item_course.xml',
        'views/menu_item_lesson.xml',
        'views/menu_view.xml',
    ],

    'assets': {
    'web.assets_backend': [
  
        'HungVP-HelloWorld/static/src/css/an_chatter.css',
    
        ],
    },
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
}