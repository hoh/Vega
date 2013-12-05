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

from vega.analyzer import log


class CLIInterface:

    @log
    def send_message(self, recipient, text):
        date = time.time()
        self.output.message(recipient, text, date)

    @log
    def recv_message(self, emitter, text, date):
        print('{} {}: {}'.format(date, emitter, text))

    def run(self):
        try:
            while True:
                recipient = input('Recipient [Bob]: ')
                if not recipient:
                    recipient = 'Bob'
                if recipient not in self.contacts:
                    print('Unknown contact: {}'.format(recipient))
                    continue
                message = input('Message [Sample text...]: ')
                if not message:
                    message = 'Sample text...'
                self.send_message(recipient, message)
        except KeyboardInterrupt:
            print()
            return
