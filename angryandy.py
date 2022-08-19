import random

from chatter import Chatter
import codex

class AngryAndy(Chatter):
    def __init__(self):
        super().__init__("Andy")
        self.patience = 0
        self.reset_patience()


    def reset_patience(self):
        self.patience = random.randrange(5, 8)


    def update(self):
        did_chat, chat_content = codex.get_did_tina_chat()
        if did_chat:
            self.patience -= 1
            if self.patience == 0:
                self.reset_patience()
                # TODO move following 2 lines into rage function, also find way to queue dialog for certain amount of time?
                # maybe add seconds counter to the get_did_tina_chat function to delay the true return
                self.queue_dialog("we get it \"{}\" shut up already".format(chat_content), wait_time=2, callback=codex.set_did_andy_rage_true)
        
        # FIXME remove test patience LUL
        #if codex.get_time_seconds_left() % 10 == 0:
        #    self.queue_dialog(str(self.patience))