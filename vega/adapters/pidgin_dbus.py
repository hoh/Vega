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
import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

from vega.analyzer import log

#dbus.mainloop.glib.threads_init()
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)


class PidginDBusAdapter:

    def __init__(self):
        bus = dbus.SessionBus()

        bus.add_signal_receiver(self.wrote_im_msg,
                                     dbus_interface="im.pidgin.purple.PurpleInterface",
                                     signal_name="WroteImMsg")

        obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
        self.purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

    @log
    def message(self, recipient, encrypted_text):
        '''
            Used as output interface.

            FIXME: Sends the message to all recipients as I don't know yet how
            to select the recipient.
        '''
        for conv in self.purple.PurpleGetIms():
            self.purple.PurpleConvImSend(self.purple.PurpleConvIm(conv), encrypted_text)

    @log
    def receive_message(self, emitter, encrypted_text, date):
        self.output.message(emitter, encrypted_text, date)
        
    @log
    def wrote_im_msg(self, account, sender, message, conversation, flags):
        if message[0] == '.': 
            return
        print(sender, "wrote:", message)
        recipient = self.contacts['Bob']
        date = time.time()
        self.output.message(recipient, message, date)

    def run(self):
        loop = GObject.MainLoop()
        loop.run()

