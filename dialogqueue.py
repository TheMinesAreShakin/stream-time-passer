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


# this is not actually a queue, it's more like a waiting room
queue = []

def queue_dialog(dialog, chatter_name, wait_time=0, callback=None):
    '''callback needs to have no args'''
    global queue
    queue.append([
        wait_time,
        chatter_name,
        dialog,
        callback
    ])


def update_and_get_dialog():
    '''will decrement wait_time of all dialog and will return a string with
    the dialog that had a wait_time of 0'''
    global queue
    output = ""

    for i, entry in enumerate(queue):
        if entry[0] > 0:
            entry[0] -= 1
            continue
        else:
            output += create_chat_message(entry)
            # call the callback func if there is one
            if entry[3] is not None:
                entry[3]()
            queue.pop(i)
    
    return output


def create_chat_message(entry):
    return "{}: {}\n".format(entry[1], entry[2])