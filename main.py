import time
import codex
from timingtina import TimingTina


tina = TimingTina()

def update():
    # should be called every second
    codex.update()
    tina.update()


def render():
    output = ""
    if codex.get_time_seconds_left() % 10 == 0:
        output += "{} in: {}".format("Stream Starting" if codex.get_wait_type() == "S" else "Be Right Back", codex.get_time_minsec_str()) + "\n"
    output += tina.get_queued_dialog()
    print(output, end="")


codex.user_setup()
while True:
    update()
    render()
    time.sleep(1)