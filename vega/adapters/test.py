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


class DummyEmitter:

    @log
    def message(self, recipient, encrypted_text):
        print("Sending to {} : {}".format(recipient, encrypted_text))


class DummyReceiver:

    @log
    def fetch(self):
        emitter = self.contacts['Alice']
        encrypted_text = 'Hello Alice !'
        date = time.time()
        self.output.message(emitter, encrypted_text, date)
