from chatter import Chatter
import codex

class TimingTina(Chatter):


    def __init__(self):
        super().__init__("TimingTina")


    def update(self):
        seconds_left = codex.get_time_seconds_left()
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