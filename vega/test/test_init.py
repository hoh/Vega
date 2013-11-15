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

import pytest
from vega.scrambler import ProxyScrambler
from vega.adapter import DummyAdapter


def test_msg():
    s = ProxyScrambler(DummyAdapter())
    with pytest.raises(TypeError):
        s.msg()
    with pytest.raises(TypeError):
        s.msg('Hello')
    s.msg('Hello', 'Bob')


def test_post():
    s = ProxyScrambler(DummyAdapter())
    s.post('Bob', 'Hello', conversation=None)
    #s.post('Bob', 'Hello', conversation=0)


def test_browse():
    s = ProxyScrambler(DummyAdapter())
    s.browse('Bob')
    s.browse('Bob', limit=10)


def test_read():
    conversation = 10
    s = ProxyScrambler(DummyAdapter())
    s.read(conversation)
    s.read(conversation, limit=10)
