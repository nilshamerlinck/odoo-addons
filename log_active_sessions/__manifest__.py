# -*- coding: utf-8 -*-
{
    'name': "Log Active Sessions",
    'summary': "Adds a Scheduled Action to log active sessions",
    'author': "Nils Hamerlinck, Odoo Community Association (OCA)",
    'maintainer': 'Odoo Community Association (OCA)',
    'category': 'Tools',
    'version': '10.0.0.1.0',
    'license': 'AGPL-3',

    'depends': [
        'base',
        'auth_session_timeout',
    ],

    'data': [
        'data/ir_cron_data.xml',
    ],

    'installable': True,
}
