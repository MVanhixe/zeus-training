{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Marjan Vanhixe',
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_type_views.xml',
        'views/estate_property_tage_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False
}