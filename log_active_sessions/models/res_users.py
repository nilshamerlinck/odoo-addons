# -*- coding: utf-8 -*-

from openerp import api, models
from openerp import http

from openerp.http import root
from openerp.http import request

import os.path
from glob import glob

from time import time

import pickle

ACTIVE_SESSION = 5 * 60 # did something in the last 5 minutes

import logging
_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def log_active_sessions(self):
        deadline = time() - ACTIVE_SESSION

        active_users = []
        
        session_store = root.session_store
        sessions = glob(os.path.join(session_store.path, '*.sess'))
        sessions.sort(key=os.path.getmtime)
        sessions.reverse()
        
        for s in sessions:
            try:
                if os.path.getmtime(s) > deadline:
                    s = pickle.load(open(s, 'r'))
                    if 'login' in s and s['login']: # not anonymous
                        active_users.append(s['login'])
                else:
                    break # files have been order by mtime DESC
            except OSError:
                pass

        if len(active_users) > 0:
            log = '%d active session%s (%s)' % (len(active_users),
                                                len(active_users) > 1 and 's' or '',
                                                ', '.join(active_users))
        else:
            log = '0 active session'
        logging.info(log)
        
        return True
