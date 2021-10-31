# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Property Management",
    'version': '14.0.1.0.0',
    "author": "WEHA Consultant",
    "website": "https://www.weha-id.com",
    "category": "Property",
    "depends": [
        'mail',
        'maintenance'
    ],
    "license": "AGPL-3",
    "data": [
        'views/property_menu_view.xml',
        'views/property_config_view.xml',
        'views/property_land_view.xml',
        'views/property_building_view.xml',
        'views/property_room_view.xml',
        'data/data.xml',
        #'data/res.country.state.csv',
        'security/ir.model.access.csv'

    ],
    'application': True,
    "images": ['static/description/main_screenshot.png','static/description/main_screenshot.svg'],
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
