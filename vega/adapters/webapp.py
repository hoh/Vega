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

'''
Allows two test WebApp instances to send messages to each other.
'''

import time
import requests

from vega.analyzer import log


class WebAppEmitter:

    def __init__(self, URL):
        self.URL = URL

    @log
    def message(self, recipient, encrypted_text):
        requests.post(
            self.URL,
            data={
                'recipient': recipient,
                'encrypted_text': encrypted_text,
                'date': time.time(),
                })


class WebAppReceiver:

    @log
    def fetch(self):
        emitter = self.contacts['Alice']
        encrypted_text = 'Uryyb Nyvpr !'
        date = time.time()
        self.output.message(emitter, encrypted_text, date)
