import random

from chatter import Chatter
import codex

class TimingTina(Chatter):


    def __init__(self):
        super().__init__("Tina")
        self.timid = 0


    def queue_dialog(self, dialog):
        codex.set_did_tina_chat_true(dialog)
        return super().queue_dialog(dialog)


    def handle_andy_rage(self):
        if codex.get_did_andy_rage():
            self.queue_dialog("Sheesh I'm just excited, chill andy")
            self.intimidate()


    def intimidate(self):
        self.timid = random.randrange(3, 5)


    def create_dialog(self):
        seconds_left = codex.get_time_seconds_left()
        if self.timid > 0 and seconds_left != 0:
            if seconds_left % 60 == 0:
                print("Tina: {}".format(self.timid))
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