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

from codecs import getencoder, getdecoder

from vega.analyzer import log


class DummyEncryption:

    encode = getencoder('rot-13')

    @log
    def message(self, recipient, text):
        encrypted_text = self.encode(text)[0]
        self.output.message(recipient, encrypted_text)


class DummyDecryption:

    decode = getdecoder('rot-13')

    @log
    def message(self, emitter, encrypted_text, date):
        decrypted_text = self.decode(encrypted_text)[0]
        self.output.message(emitter, decrypted_text, date)
