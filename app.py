import datetime
import hashlib
import json

class Block:
    index_counter = -1
    def __init__(self, nonce,transactions,  timeStamp,previous_hash ):
        Block.index_counter+=1
        self.index = Block.index_counter
        self.nonce = nonce
        self.transactions = transactions
        self.timeStamp = timeStamp
        self.previous_hash = previous_hash
        self.block_data = json.dumps(self.__dict__, sort_keys=True, default=str).encode()
        self.hash = hashlib.sha256(self.block_data).hexdigest()
        Blockchain.blocks.append(self)

class Blockchain:
    index_counter=0
    blocks=[]

    @staticmethod
    def create_genesisBlock():
        genesis_block = Block(0,[], datetime.datetime.now(), '0' )

    def add_block(self):
        Blockchain.index_counter += 1
        self.index = Blockchain.index_counter
        self.nonce = 0
        self.transactions = '0'
        self.timeStamp = datetime.datetime.now()
        self.previous_hash = '0'
        self.block_data = json.dumps(self.__dict__, sort_keys=True, default=str).encode()
        self.hash = hashlib.sha256(self.block_data).hexdigest()
        Blockchain.blocks.append(self)



def get_transaction_info():
    sender = input('Enter sender:')
    recipient = input('Enter recipient:')
    amount = input('Enter amount:')
    if len(Blockchain.blocks)>1:
        add_transaction(sender, recipient, amount)
        answer = input("Want to add more block? (yes/no)")
        if answer == "yes":
            return get_transaction_info()
        else:
            print("Transaction was successfully added")
        return sender, recipient, amount
    else:
        print('You cannot add transactions to genesis block')

def add_transaction(sender, recipient, amount):
    last_block = Blockchain.blocks[-1].transactions
    transaction_data = (str(sender)+str(recipient)+str(amount)).encode()
    last_block.append(transaction_data)
    print(transaction_data)




Blockchain.create_genesisBlock()
for b in Blockchain.blocks:
    print(b.__dict__)
print()
get_transaction_info()
for i in Blockchain.blocks[-1].transactions:
    print(i)


def validate(nonce, last_block_transaction, last_block_hash):
    answer = (str(last_block_transaction) + str(last_block_hash) + str(nonce)).encode()
    answer_hash = hashlib.sha256(answer).hexdigest()
def calculate_nonce():
    nonce = 0
    last_block_transaction = Blockchain.blocks[-1].transactions
    last_block_hash = Blockchain.blocks[-1].hash





