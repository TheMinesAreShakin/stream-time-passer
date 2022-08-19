import dialogqueue

class Chatter:

    def __init__(self, chatterName):
        #self.queued_dialog = ""
        self.chatterName = chatterName

    
    def queue_dialog(self, dialog, wait_time=0, callback=None):
        # adds newline for you
        #self.queued_dialog += "{}: {}\n".format(self.chatterName, dialog)
        dialogqueue.queue_dialog(dialog=dialog, chatter_name=self.chatterName, wait_time=wait_time, callback=callback)


    #def get_queued_dialog(self):
    #    out = self.queued_dialog
    #    self.queued_dialog = ""
    #    return out