import random
import string

class Message:
    def __init__(self, message=None, recipient=None):
        if message is None:
            self.message = self.generateRandomMessage() 
        else:
            self.message = message
        if recipient is None:
            self.recipient = self.generateRandomRecipient()
        else: 
            self.recipient = recipient

    def generateRandomMessage(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,100)))

    def generateRandomRecipient(self):
        return random.randint(1000000000, 9999999999)

    def getMessage(self):
        return self.message

    def getRecipient(self):
        return self.recipient
