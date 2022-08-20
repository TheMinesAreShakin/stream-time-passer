'''
    Tool to pass the time on stream.
    Copyright (C) 2022  theMinesAreShakin

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''


import random
from subprocess import call

from chatter import Chatter
import codex

class TimingTina(Chatter):


    def __init__(self):
        super().__init__("Tina")
        self.timid = 0


    def queue_dialog(self, dialog, wait_time=0, callback=None):
        codex.set_did_tina_chat_true(dialog)
        return super().queue_dialog(dialog, wait_time=wait_time, callback=callback)


    def handle_andy_rage(self):
        if codex.get_did_andy_rage():
            # find way to queue dialog for certain amount of time? maybe add seconds counter to the get_did_andy_rage function to delay the true return
            self.queue_dialog("Sheesh I'm just excited, chill andy", wait_time=2)
            self.intimidate()


    def intimidate(self):
        self.timid = random.randrange(3, 5)


    def create_dialog(self):
        seconds_left = codex.get_time_seconds_left()
        if self.timid > 0 and seconds_left != 0:
            if seconds_left % 60 == 0:
                # FIXME remove
                #print("Tina: {}".format(self.timid))
                self.timid -= 1
            return
        if seconds_left == 0:
            self.queue_dialog("Stream time!")
        elif seconds_left % 60 == 0 and seconds_left > 0 and codex.get_wait_type() == "S":
            d = "Only {} till stream starts!".format(codex.get_time_minsec_str())
            self.queue_dialog(d)
        elif seconds_left % 60 == 0 and seconds_left < 0 and codex.get_wait_type() == "S":
            d = "Stream should have started {} minutes ago >:(".format(codex.get_time_min_str(include_minus=False))
            self.queue_dialog(d)
        elif seconds_left % 60 == 0 and seconds_left > 0 and codex.get_wait_type() == "B":
            d = "Only {} till he's back".format(codex.get_time_minsec_str())
            self.queue_dialog(d)
        elif seconds_left % 60 == 0 and seconds_left < 0 and codex.get_wait_type() == "B":
            d = "He should have been back {} minutes ago >:(".format(codex.get_time_min_str(include_minus=False))
            self.queue_dialog(d)


    def update(self):
        self.create_dialog()
        self.handle_andy_rage()