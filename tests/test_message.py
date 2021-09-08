import unittest
from message import Message

class MessageTest(unittest.TestCase):
    def testMessageAccessors(self):
        test_message = Message('7175552368', 'THIS IS A TEST MESSAGE')
        self.assertEqual(test_message.getMessage(), '7175552368')
        self.assertEqual(test_message.getRecipient(), 'THIS IS A TEST MESSAGE')

    def testRandomMessageGenerator(self):
        test_message = Message()
        self.assertGreaterEqual(len(test_message.getMessage()), 1)

    def testRandomRecipientGenerator(self):
        test_message = Message()
        self.assertGreaterEqual(test_message.getRecipient(), 1000000000)
        self.assertLessEqual(test_message.getRecipient(), 9999999999)

if __name__ == "__main__":
    unittest.main()
