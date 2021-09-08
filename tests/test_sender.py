import unittest
from sender import Sender
from message import Message
import queue

class SenderTest(unittest.TestCase):
    def test_message_sending(self):
        test_queue = queue.Queue()
        test_queue.put(Message('7175552368', 'THIS IS A TEST MESSAGE'))
        self.assertEqual(test_queue.qsize(), 1)

        test_times = []
        test_messageStats = { 'sent' : 0, 'failed' : 0, 'total' : 0 }
        test_failureRate = 0
        test_avgSendTime = 1

        test_sender = Sender(name='test_sender', args=[test_queue, None, test_messageStats, test_failureRate, test_avgSendTime, test_times])
        test_sender.sendMessages()
        
        # check if the message sent and the stats were populated correctly
        self.assertEqual(test_queue.qsize(), 0)

        self.assertEqual(test_messageStats['total'], 1)
        self.assertEqual(test_messageStats['sent'], 1)
        self.assertEqual(test_messageStats['failed'], 0)

        self.assertEqual(len(test_times), 1)
        self.assertGreater(test_times[0], 0)
        