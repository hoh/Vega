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

from vega.interfaces.web import WebInterface
from vega.generators.test import EmptyGenerator
from vega.mixers import AdditionMixer
from vega.encryption.test import DummyEncryption
from vega.adapters.test import DummyEmitter

from vega.adapters.test import DummyReceiver
from vega.encryption.test import DummyDecryption
from vega.filters.test import DummyFilter

from vega.contacts.test import TestContacts


def main():
    interface = WebInterface()
    generator = EmptyGenerator()
    mixer = AdditionMixer()
    encryption = DummyEncryption()
    emitter = DummyEmitter()

    receiver = DummyReceiver()
    decryption = DummyDecryption()
    filter = DummyFilter()

    contacts = TestContacts()

    interface.output = mixer
    generator.output = mixer
    mixer.output = encryption
    encryption.output = emitter

    receiver.output = decryption
    decryption.output = filter
    filter.output = interface

    contacts = TestContacts()
    receiver.contacts = contacts
    interface.contacts = contacts

    interface.run()

if __name__ == '__main__':
    main()
