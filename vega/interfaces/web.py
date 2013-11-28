# Copyright (c) 2013 "Hugo Herter"
# [http://hugoherter.com]
#
# This file is part of Vega.
#
# Vega is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import time

import bottle
from bottle import request

from vega.analyzer import log

DEBUG = False

index_page = '''<!doctype html>
<html>
    <body>
        <section>
            {}
        </section>
        <section>
            <form action='/post' method='POST'>
                <select name='recipient'>
                    <option value="Alice">Alice</option>
                    <option value="Bob">Bob</option>
                </select>
                <input name='message' placeholder='Your message...' />
                <input type='submit' value='Send' />

                <input type='hidden' name='CSRF_token' value='6ddbbac0-5849' />
            </form>
        </section>
    </body>
</html>
'''


class WebInterface:

    def __init__(self):
        self._app = bottle.Bottle()
        self._app.route('/', method='GET', callback=self.index)
        self._app.route('/post', method='POST', callback=self.post)

    def index(self):
        return index_page.format('')

    def post(self):
        recipient = request.forms.get('recipient')
        message = request.forms.get('message')
        self.send_message(self.contacts[recipient], message)
        return index_page.format('Message sent to {}'.format(recipient))

    @log
    def send_message(self, recipient, text):
        date = time.time()
        self.output.message(recipient, text, date)

    @log
    def recv_message(self, emitter, text, date):
        self._messages.append('{} {}: {}'.format(date, emitter, text))

    def run(self):
        bottle.run(self._app, reloader=DEBUG)
