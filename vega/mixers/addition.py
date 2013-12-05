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
import threading

from vega.analyzer import log


class AdditionMixer:

    # Set this to false to stop the mixer's mainloop:
    run = True

    def __init__(self, generator):
        self.generator = generator

    @log
    def message(self, recipient, text, date):
        'Immediately proxies real messages to the output module.'
        self.output.message(recipient, text)

    def loop(self):
        'Main loop for dummy messages generation.'
        while True:
            messages = self.generator.gen()
            import pprint
            pprint.pprint(messages)
            for message in messages:
                dt = message['date'] - time.time()
                if dt > 0:
                    time.sleep(dt)
                    self.output.message(message['recipient'], message['text'])

    def start_loop(self):
        self.loop_thread = threading.Thread(target=self.loop)
        self.loop_thread.start()
