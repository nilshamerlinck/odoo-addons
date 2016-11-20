.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Log Active Sessions
===================
	  
OCA's module `auth_session_timeout` (server-tools) updates the mtime of the session file at each RPC request.

The added Scheduled Action checks all sessions files every minute to determine how many sessions have been active in the last 5 minutes.

It will appear in server log like this: `3 active sessions (user1, user2, user3)`

Please note that:

* users are ordered from the most recently active to the last
* same user might appear multiple times if it's shared
* the sessions files directory should not be shared by multiple Odoo instances
