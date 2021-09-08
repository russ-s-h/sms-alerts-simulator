from message import Message
import threading
import logging
import random
import queue
import time

class Producer(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=[], kwargs=None, verbose=None):
        super(Producer,self).__init__()
        self.target = target
        self.name = name
        self.q = args[0]
        self.logging = args[1]
        self.totalMessages = args[2]

    def run(self):
        self.createBatchMessages()

    def createBatchMessages(self):
        for _ in range(self.totalMessages):
            newMessage = Message()
            self.q.put(newMessage)
            #self.logging.debug('Putting ' + str(newMessage.getRecipient())  + ' : ' + str(self.q.qsize()) + ' items in queue')
