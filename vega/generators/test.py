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
import random

from vega.analyzer import log


class EmptyGenerator:

    @log
    def gen(self):
        # Populate with zero message:
        return []


class FixedIntervalGenerator:

    interval = 2
    duration = 5

    @log
    def pop(self):
        message = {
            'recipient': self.contacts['Charlie'],
            'text': '',
            'date': time.time() + self.interval,
        }
        return message

    @log
    def gen(self):
        n = 3
        interval = float(self.duration) / n

        messages = [
            {'recipient': self.contacts['Charlie'],
             'text': '?DUMMY:',
             'date': time.time() + (interval * i),
             }
            for i in range(n)
        ]
        messages = sorted(messages, key=lambda x: x['date'])
        return messages
