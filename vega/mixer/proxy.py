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

    def __init__(self, adapter, cipher):
        '''
        Initializes a new Scrambler with the given adapter.
        '''
        self.adapter = adapter
        self.cipher = cipher

    def login(self):
        pass

    def logout(self):
        pass

    # --- Active actions ---

    def msg(self, recipient, message, readers=None):
        '''
        Send ``message`` to ``recipient``.
        Returns the message id.
        '''

        # By default, only me and the recipient can decrypt messages.
        readers = readers if readers else (recipient, 'me')
        encrypted_message = self.cipher.encrypt(message, readers)
        self.adapter.msg(recipient, encrypted_message)

    def post(self, recipient, message, conversation=None, readers=None):
        '''
        Post ``message`` on the wall of ``recipient``.
        If ``conversation``is None, a new conversation is created.

        Returns the conversation id and the post id.
        '''

        # By default, only me and the wall's owner can decrypt messages.
        readers = readers if readers else (recipient, 'me')
        encrypted_message = self.cipher.encrypt(message, readers)

        self.adapter.post(recipient, encrypted_message, conversation=False)

    # --- Passive actions ---

    def browse(self, recipient, limit=None):
        '''
        Returns the conversation id for the ``limit`` latest conversations
        on ``recipient``'s wall.
        '''
        conversations = self.adapter.browse(recipient, limit)
        return conversations

    def read(self, conversation, limit=None):
        '''
        Returns the message id for the ``limit`` latest messages
        in ``conversation``.
        '''
        conversation = self.adapter.read(conversation, limit)
        return conversation.decrypt(self.cipher)
