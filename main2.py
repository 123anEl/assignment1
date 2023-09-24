import datetime
import hashlib
import json

'''def f1():
    list_of_nonce=[]
    while len(list_of_nonce)<(5):
        unique_nonce = randint(1, 5)
        if unique_nonce not in list_of_nonce:
            list_of_nonce.append(unique_nonce)
            return unique_nonce'''

class BlockChain:
    difficulty = 2
    index = -1
    blocks = []
    transactions=[]
    def __init__(self, sender, recipient, amount, nonce):
        BlockChain.index += 1
        self.index = BlockChain.index
        prev_index = self.index-1
        sender = sender
        recipient = recipient
        amount = amount
        if self.index>=1:
            self.previous_hash = BlockChain.blocks[prev_index].hash
            self.transaction_data = str(sender)+str(recipient)+str(amount)
           # previous_hash='0000'
        else:
            self.previous_hash = '0' # If index is 0, then it is genesis block. Genesis block's previous hash is 0. Because it has no previous block to reference to
            self.transaction_data = [] #For genesis block there is no transaction yet
        self.timeStamp = datetime.datetime.now()
        self.nonce = nonce
        self.block_data = json.dumps(self.__dict__, sort_keys=True, default=str).encode()
        self.hash = hashlib.sha256(self.block_data).hexdigest()
        BlockChain.transactions.append(self.transaction_data) #Add transaction to the list
        BlockChain.blocks.append(self)#Add block to the list of blocks

genesis_block = BlockChain('','', 0, 0)

def validate(transactions, last_block_hash, nonce ):
    answer = (str(transactions)+str(last_block_hash)+str(nonce)).encode()
    answer_hash= hashlib.sha256(answer).hexdigest()
    #print(answer_hash)
    return answer_hash[0:2]=='00'

def calculate_nonce():
    nonce = 0
    last_block = BlockChain.blocks[-1]
    last_block_hash = BlockChain.blocks[-1].hash
    while not validate(BlockChain.transactions, last_block_hash, nonce):
        nonce+=1
    return nonce


#calculate_nonce()
#print(calculate_nonce())
def get_transactionInfo_to_add_block():
    sender = input('Enter sender:')
    recipient = input('Enter recipient:')
    amount = input('Enter amount:')
    nonce = calculate_nonce()
    block = BlockChain(sender, recipient, amount, nonce)
    answer = input('Want to add more blocks? (yes/no)')
    if answer=='yes':
        return get_transactionInfo_to_add_block()
    else:
        print('Successful addition of blocks')



get_transactionInfo_to_add_block()

for block in BlockChain.blocks:
    print(block.__dict__)

'''tr3 = 'b3 sends WWW 3.5 btc'
b3 = BlockChain(tr3)
print(b3.__dict__) # Print all attributes of an object
'''
