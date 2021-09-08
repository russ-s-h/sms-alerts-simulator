import threading
import logging
import random
import queue
import time

class Sender(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=[], kwargs=None, verbose=None):
        super(Sender,self).__init__()
        self.target = target
        self.name = name
        self.q = args[0]
        self.logging = args[1]
        self.messageStats = args[2]
        self.failureRate = args[3]
        self.avgSendTime = args[4]
        self.times = args[5]
    
    def run(self):
        while not self.q.empty():
            message = self.q.get()
            startTime = time.time()
            self.sendMessage()
            endTime = time.time()
            totalTime = endTime - startTime
            self.times.append(totalTime)
            #self.logging.debug('Sending ' + str(message.getRecipient()) + ' : ' + str(self.q.qsize()) + ' items in queue')
        return

    def sendMessage(self):
        time.sleep(abs(random.normalvariate(self.avgSendTime, 1)))
        if random.randint(0,100) >= self.failureRate:
            self.messageStats['sent'] += 1
        else:
            self.messageStats['failed'] += 1
        self.messageStats['total'] += 1