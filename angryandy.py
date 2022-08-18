import random

from chatter import Chatter
import codex

class AngryAndy(Chatter):
    def __init__(self):
        super().__init__("Andy")
        self.reset_patience()


    def reset_patience(self):
        self.patience = random.randrange(5, 8)


    def update(self):
        did_chat, chat_content = codex.get_did_tina_chat()
        if did_chat:
            self.patience -= 1
            if self.patience == 0:
                self.reset_patience()
                self.queue_dialog("we get it \"{}\" shut up already".format(chat_content))
                codex.set_did_andy_rage_true()
        
        # test patience LUL
        if codex.get_time_seconds_left() % 10 == 0:
            self.queue_dialog(str(self.patience))