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

from vega.interfaces.cli import CLIInterface
from vega.generators.test import FixedIntervalGenerator
from vega.mixers import AdditionMixer
from vega.encryption.test import DummyEncryption
from vega.adapters.test import DummyEmitter

from vega.contacts.test import TestContacts


def main():
    interface = CLIInterface()
    generator = FixedIntervalGenerator()
    mixer = AdditionMixer(generator)
    encryption = DummyEncryption()
    emitter = DummyEmitter()

    contacts = TestContacts()

    interface.output = mixer
    generator.output = mixer
    mixer.output = encryption
    encryption.output = emitter

    interface.contacts = contacts
    generator.contacts = contacts

    mixer.start_loop()
    interface.run()

if __name__ == '__main__':
    main()
