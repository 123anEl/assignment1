import datetime
import hashlib

'''def f1():
    list_of_nonce=[]
    while len(list_of_nonce)<(5):
        unique_nonce = randint(1, 5)
        if unique_nonce not in list_of_nonce:
            list_of_nonce.append(unique_nonce)
            return unique_nonce'''

class BlockChain:
    difficulty = 3
    index = -1
    blocks = []
    def __init__(self, sender, recipient, amount):
        BlockChain.index += 1
        self.index = BlockChain.index
        prev_index = self.index-1
        sender = sender
        recipient = recipient
        amount = amount
        if self.index>=1:
            previous_hash = BlockChain.blocks[prev_index].hash
            self.transaction_data = str(sender)+str(recipient)+str(amount)
           # previous_hash='0000'
        else:
            previous_hash = '0' # If index is 0, then it is genesis block. Genesis block's previous hash is 0. Because it has no previous block to reference to
            self.transaction_data = [] #For genesis block there is no transaction yet
        self.timeStamp = datetime.datetime.now()
        self.nonce = 0
        self.block_data = (str(previous_hash) + '+' + str(self.__dict__)).encode()
        self.hash = hashlib.sha256(self.block_data).hexdigest()
        BlockChain.blocks.append(self)

def get_info_to_add_block():
    sender = input('Enter sender:')
    recipient = input('Enter recipient:')
    amount = input('Enter amount:')
    block = BlockChain(sender, recipient, amount)
    answer = input('Want to add more blocks? (yes/no)')
    if answer=='yes':
        return get_info_to_add_block()
    else:
        print('Successful addition of blocks')



get_info_to_add_block()

for block in BlockChain.blocks:
    print(block.__dict__)
'''tr3 = 'b3 sends WWW 3.5 btc'
b3 = BlockChain(tr3)
print(b3.__dict__) # Print all attributes of an object
'''
