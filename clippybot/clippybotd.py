#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot
from clippybot.tools import *
from clippybot.db import *

class ClipPybot(ircbot.SingleServerIRCBot):
    def __init__(self, config):
        self._config = config

        super(ClipPybot, self).__init__([(self._config['global']['host'], self._config['global']['port'])], self._config['global']['nick'], self._config['global']['nick'])
        
    def on_welcome(self, serv, ev):
        serv.join("#foo")

    def on_pubmsg(self, serv, ev):
        if ev.arguments()[0].startswith('!'):
            nick = irclib.nm_to_n(ev.source())
	    message = ev.arguments()[0].lower()
            channel = ev.target()
            command = message.split()[0]
            action = message.split()[1]
            args = ' '.join(message.split()[2:])

            if command == '!todo':
                if action == 'add':
                    name = args.split(' ')[0]
                    todo = ' '.join(args.split(' ')[1:])
                    with Db(db_name='%s-todo' % (nick), db_file='clippybot-db.json', db_type='list' ) as db:
                        db.save(args)
                    serv.privmsg(channel, '...Todo saved.')
                if action == 'list':
                    with Db(db_name='%s-todo' % (nick), db_file='clippybot-db.json', db_type='list') as db:
                        serv.privmsg(channel, "%s, Here is your todo list:" % (nick))
                        for i, v in enumerate(db.get_all()):
                            serv.privmsg(channel, "%s: %s" % (i, v))
                    serv.privmsg(channel, "Good Luck %s!" % nick)
