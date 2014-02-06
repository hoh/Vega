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
import threading

import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

from vega.analyzer import log

dbus.mainloop.glib.threads_init()
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

class PidginDBusInterface:

    def __init__(self):
        self.bus = dbus.SessionBus()

    @log
    def send_message(self, recipient, text):
        date = time.time()
        self.output.message(recipient, text, date)

    @log
    def recv_message(self, emitter, text, date):
        print('{} {}: {}'.format(date, emitter, text))

    def wrote_im_msg(self, account, sender, message, conversation, flags):
        print(sender, "writing:", message)
        self.send_message(self.contacts['Bob'], message)

    def run(self):

        self.bus.add_signal_receiver(self.wrote_im_msg,
                                     dbus_interface="im.pidgin.purple.PurpleInterface",
                                     signal_name="WroteImMsg")

        loop = GObject.MainLoop()
        loop.run()

