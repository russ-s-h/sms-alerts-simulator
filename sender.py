import threading
import logging
import random
import queue
import time

class Sender(threading.Thread):
    """
    Sender Thread Class
    """
    def __init__(self, group=None, target=None, name=None, args=[], kwargs=None, verbose=None):
        super(Sender,self).__init__()
        self.target = target
        self.name = name
        self.messageQueue = args[0]
        self.logging = args[1]
        self.messageStats = args[2]
        self.failureRate = args[3]
        self.avgSendTime = args[4]
        self.times = args[5]
    
    def run(self):
        self.sendMessages()

    def sendMessage(self):
        # wait for random period of time around the configured mean
        time.sleep(abs(random.normalvariate(self.avgSendTime, 1)))
        # determine whether the message failed to send or not
        if random.randint(0,100) >= self.failureRate:
            self.messageStats['sent'] += 1
        else:
            self.messageStats['failed'] += 1
        self.messageStats['total'] += 1
    
    def sendMessages(self):
        while not self.messageQueue.empty():
            message = self.messageQueue.get()
            startTime = time.time()
            self.sendMessage()
            endTime = time.time()
            totalTime = endTime - startTime
            self.times.append(totalTime)
            #self.logging.debug('Sending ' + str(message.getRecipient()) + ' : ' + str(self.q.qsize()) + ' items in queue')
        return