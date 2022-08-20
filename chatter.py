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


import dialogqueue

class Chatter:

    def __init__(self, chatterName):
        #self.queued_dialog = ""
        self.chatterName = chatterName

    
    def queue_dialog(self, dialog, wait_time=0, callback=None):
        # adds newline for you
        #self.queued_dialog += "{}: {}\n".format(self.chatterName, dialog)
        dialogqueue.queue_dialog(dialog=dialog, chatter_name=self.chatterName, wait_time=wait_time, callback=callback)


    #def get_queued_dialog(self):
    #    out = self.queued_dialog
    #    self.queued_dialog = ""
    #    return out