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


from .scrambler import Scrambler


class ProxyScrambler(Scrambler):
    '''
    Scrambler with no scrambling, only proxies messages to/from the adapter.
    '''

    def __init__(self, adapter):
        '''
        Initializes a new Scrambler with the given adapter.
        '''
        self.adapter = adapter

    def login(self):
        pass

    def logout(self):
        pass

    # --- Active actions ---

    def msg(self, recipient, message):
        '''
        Send ``message`` to ``recipient``.
        Returns the message id.
        '''
        pass

    def post(self, recipient, message, conversation=None):
        '''
        Post ``message`` on the wall of ``recipient``.
        If ``conversation``is None, a new conversation is created.

        Returns the conversation id and the post id.
        '''
        pass

    # --- Passive actions ---

    def browse(self, recipient, limit=None):
        '''
        Returns the conversation id for the ``limit`` latest conversations
        on ``recipient``'s wall.
        '''
        pass

    def read(self, conversation, limit=None):
        '''
        Returns the message id for the ``limit`` latest messages
        in ``conversation``.
        '''
        pass
