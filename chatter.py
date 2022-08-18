class Chatter:

    def __init__(self, chatterName):
        self.queued_dialog = ""
        self.chatterName = chatterName

    
    def queue_dialog(self, dialog):
        # adds newline for you
        self.queued_dialog += "{}: {}\n".format(self.chatterName, dialog)


    def get_queued_dialog(self):
        out = self.queued_dialog
        self.queued_dialog = ""
        return out