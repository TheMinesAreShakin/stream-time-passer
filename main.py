import time

import codex
from timingtina import TimingTina
from angryandy import AngryAndy


tina = TimingTina()
andy = AngryAndy()

def update():
    # should be called every second
    codex.update()
    tina.update()
    andy.update()


def render():
    output = ""
    if codex.get_time_seconds_left() % 10 == 0:
        output += "{} in: {}".format("Stream Starting" if codex.get_wait_type() == "S" else "Be Right Back", codex.get_time_minsec_str()) + "\n"
    output += tina.get_queued_dialog()
    output += andy.get_queued_dialog()
    print(output, end="")


codex.user_setup()
while True:
    update()
    render()

    # this actually makes the timer inaccurate. I would need to use a sleep(delta) to have a semi accurate time that would adjust to runtime
    # FIXME
    #time.sleep(1) #FIXME uncomment
    # FIXME remove loop limit
    if codex.get_time_seconds_left() < -240:
        exit()