

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

    update()
    render()

    # this actually makes the timer inaccurate. I would need to use a sleep(delta) to have a semi accurate time that would adjust to runtime
    # FIXME
    time.sleep(1) #FIXME uncomment
    # FIXME remove loop limit
    #if codex.get_time_seconds_left() < -240:
    #    exit()