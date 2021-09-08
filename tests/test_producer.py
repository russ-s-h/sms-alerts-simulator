import unittest
from producer import Producer
import queue

class ProducerTest(unittest.TestCase):
    def test_message_production(self):
        test_queue = queue.Queue()
        test_producer = Producer(name='test_producer', args=[test_queue, None, 10])
        test_producer.createBatchMessages()
        self.assertEqual(test_queue.qsize(), 10)

if __name__ == "__main__":
    unittest.main()