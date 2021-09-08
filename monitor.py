import threading
import random
import queue
import time

class Monitor(threading.Thread):
    """
    Monitor Thread Class
    """
    def __init__(self, group=None, target=None, name=None, args=[], kwargs=None, verbose=None):
        super(Monitor,self).__init__()
        self.target = target
        self.name = name
        self.monitorInterval = args[0]
        self.stats = args[1]
        self.times = args[2]
        self.totalMessages = args[3]
    
    def run(self):
        while self.stats['total'] < self.totalMessages:
            time.sleep(self.monitorInterval)
            print('*************************')
            print(f"Total Messages Sent:\t{self.stats['total']}")
            print(f"Successful Messages Sent:\t{self.stats['sent']}")
            print(f"Failed Messages:\t{self.stats['failed']}")
            if len(self.times):
                print(f"Average Processing Time:\t{round(sum(self.times) / len(self.times)+1,2)}")