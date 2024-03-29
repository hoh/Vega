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

from vega.interfaces.test import TestInterface
from vega.generators.test import EmptyGenerator
from vega.mixers import AdditionMixer
from vega.encryption.test import DummyEncryption
from vega.adapters.test import DummyEmitter

from vega.adapters.test import DummyReceiver
from vega.encryption.test import DummyDecryption
from vega.filters.test import DummyFilter

from vega.contacts.test import TestContacts


def test_emission_initialization():
    interface = TestInterface()
    generator = EmptyGenerator()
    mixer = AdditionMixer(generator)
    encryption = DummyEncryption()
    emitter = DummyEmitter()

    assert interface
    assert generator
    assert mixer
    assert encryption
    assert emitter


def test_reception_initialization():
    interface = TestInterface()
    receiver = DummyReceiver()
    decryption = DummyDecryption()
    filter = DummyFilter()

    assert interface
    assert receiver
    assert decryption
    assert filter


def test_contacts_initialization():
    contacts = TestContacts()

    assert contacts


def test_emission_link():
    interface = TestInterface()
    generator = EmptyGenerator()
    mixer = AdditionMixer(generator)
    encryption = DummyEncryption()
    emitter = DummyEmitter()

    interface.output = mixer
    generator.output = mixer
    mixer.output = encryption
    encryption.output = emitter


def test_reception_link():
    receiver = DummyReceiver()
    decryption = DummyDecryption()
    filter = DummyFilter()
    interface = TestInterface()

    receiver.output = decryption
    decryption.output = filter
    filter.output = interface


def test_emission_flow():
    interface = TestInterface()
    generator = EmptyGenerator()
    mixer = AdditionMixer(generator)
    encryption = DummyEncryption()
    emitter = DummyEmitter()

    interface.output = mixer
    generator.output = mixer
    mixer.output = encryption
    encryption.output = emitter

    contacts = TestContacts()

    generator.gen()

    recipient = contacts['Bob']
    date = time.time()
    interface.send_message(recipient, 'Hello Bob !', date)


def test_reception_flow():
    receiver = DummyReceiver()
    decryption = DummyDecryption()
    filter = DummyFilter()
    interface = TestInterface()

    receiver.output = decryption
    decryption.output = filter
    filter.output = interface

    contacts = TestContacts()
    receiver.contacts = contacts

    receiver.fetch()
