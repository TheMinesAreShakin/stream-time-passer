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

import time
from tkinter import dialog

import codex
import dialogqueue
from timingtina import TimingTina
from angryandy import AngryAndy
from funfactfred import FunFactFred


chatters = [
    ["tina", TimingTina()],
    ["andy", AngryAndy()],
    ["fred", FunFactFred()]
]

def update():
    # should be called every second
    codex.update()
    for chatter in chatters:
        chatter[1].update()


def render():
    output = ""
    if codex.get_time_seconds_left() % 10 == 0:
        output += "{} in: {}".format("Stream Starting" if codex.get_wait_type() == "S" else "Be Right Back", codex.get_time_minsec_str()) + "\n"
    output += dialogqueue.update_and_get_dialog()
    print(output, end="")


codex.user_setup()
while True:
    start_time = time.perf_counter()
    update()
    render()
    end_time = time.perf_counter()
    delta = end_time - start_time

    try:
        time.sleep(1-delta) #FIXME uncomment
    except ValueError:
        # if delta is greater than 1
        continue
    # FIXME testing code
    #time.sleep(0.1)
    #if codex.get_time_seconds_left() < -240:
    #    exit()