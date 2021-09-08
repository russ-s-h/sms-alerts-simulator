from producer import Producer
from sender import Sender
from monitor import Monitor
import threading
import argparse
import logging
import random
import queue
import time

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("totalMessages", nargs="?", type=int, default=1000, help='Total number of messages that will be produced (int)')
    parser.add_argument("monitorInterval", nargs="?", type=int,  default=2, help='Frequency of monitor updates in seconds (int)')
    parser.add_argument("numSenders", nargs="?", type=int, default=1, help='Total number of senders (int)')
    args = parser.parse_args()

    messageQueue = queue.Queue()
    totalMessages = args.totalMessages
    monitorInterval = args.monitorInterval
    numSenders = args.numSenders

    sendTimes = []
    messageStats = { 'sent' : 0, 'failed' : 0, 'total' : 0 }

    # get inputs for each sender
    senderConfigs = []
    for i in range(numSenders):
        tempAvgTime = int(input(f"Enter the average processing time for sender {i+1} (int): "))
        tempFailRate = int(input(f"Enter the failure rate for sender {i+1} (%): "))
        senderConfigs.append((tempAvgTime,tempFailRate))
    # start the producer
    producer = Producer(name='producer', args=[messageQueue, logging, totalMessages])
    producer.start()
    time.sleep(2)
    # start the senders
    threads = []
    for i in range(numSenders):
        avgSendTime, failureRate = senderConfigs[i]
        sender = Sender(name='sender', args=[messageQueue, logging, messageStats, failureRate, avgSendTime, sendTimes])
        sender.start()
        threads.append(sender)
        time.sleep(1)
    # start the monitor
    monitor = Monitor(name='monitor', args=[monitorInterval, messageStats, sendTimes, totalMessages])
    monitor.start()
    time.sleep(1)

    # clean up the threads
    producer.join()
    for thread in threads:
        thread.join()
    monitor.join()

    print("Done!")
