import datetime
import hashlib
import json

class Block:
    index_counter = -1
    def __init__(self, nonce,transactions,  timeStamp,previous_hash, hash ):
        Block.index_counter+=1
        self.index = Block.index_counter
        self.nonce = nonce
        self.transactions = transactions
        self.timeStamp = timeStamp
        self.previous_hash = previous_hash
        #self.block_data = json.dumps(self.__dict__, sort_keys=True, default=str).encode()
        self.block_data = (str(self.index) + str(self.nonce) + str(self.transactions) + str(self.timeStamp) + str(self.previous_hash)).encode()
        self.hash=hash
        self.merkle_root = None
        Blockchain.blocks.append(self)





#    def hash(self):


class Blockchain:
    index_counter=0
    blocks=[]

    @staticmethod
    def create_genesisBlock():
        genesis_block = Block(0, [], datetime.datetime.now(), '0', '0000')

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
        answer = input("Want to add more transactions? (yes/no)")
        if answer == "yes":
            return get_transaction_info()
        else:
            print("Transaction was successfully added")
        return sender, recipient, amount, func()
    else:
        print('You cannot add transactions to genesis block')
        return func()

def add_transaction(sender, recipient, amount):
    last_block = Blockchain.blocks[-1].transactions
    transaction_data = (str(sender)+str(recipient)+str(amount)).encode()
    last_block.append(transaction_data)
    print(transaction_data)





def validate(last_block):
    last_block = last_block
    answer = (str(last_block.index)+str(last_block.nonce)+str(last_block.transactions)+str(last_block.timeStamp)+str(last_block .previous_hash)).encode()
    answer_hash = hashlib.sha256(answer).hexdigest()
    print(answer_hash)
    if answer_hash[0:2]=='00':
        return answer_hash

'''def calculate_nonce():
    nonce = 0
    last_block=Blockchain.blocks[-1]
    last_block_transaction = Blockchain.blocks[-1].transactions
    last_block_hash = Blockchain.blocks[-1].hash
    correct_hash = '0'
    while not validate(last_block):
        nonce+=1
    return nonce'''





def calculate_nonce():
    nonce = 0
    while True:
        if len(Blockchain.blocks) == 1:
            last_block = str(Blockchain.blocks[0]) + str(nonce)
        else:
            last_block = str(Blockchain.blocks[-1]) + str(nonce)

        calculated_hash = hashlib.sha256(last_block.encode()).hexdigest()
        if calculated_hash[:2] == '00':
            return calculated_hash, nonce
        nonce += 1

def calculate_merkle_root(transactions):
    if len(transactions) == 0:
        return hashlib.sha256(b'').hexdigest()
    elif len(transactions) == 1:
        return hashlib.sha256(transactions[0].encode()).hexdigest()
    else:
        while len(transactions) > 1:
            temp_transactions = []
            for i in range(0, len(transactions) - 1, 2):
                combined = transactions[i] + transactions[i + 1]
                root = hashlib.sha256(combined.encode()).hexdigest()
                temp_transactions.append(root)
            if len(transactions) % 2 != 0:
                temp_transactions.append(transactions[-1])
            transactions = temp_transactions
        return transactions[0]
def mine_or_add_block():
    hash, nonce = calculate_nonce()
    timeStamp = datetime.datetime.now()
    transactions = []
    if len(Blockchain.blocks) == 1:
        previous_hash = '0000'
    else:
        previous_hash = Blockchain.blocks[-1].hash
    merkle_root = calculate_merkle_root(transactions)
    new_block = Block(nonce, transactions, timeStamp, previous_hash, hash)
    new_block.merkle_root = merkle_root
    print("Block was successfully added")
    return func()

'''def mine_or_add_block():
    hash, nonce = calculate_nonce()
    timeStamp = datetime.datetime.now()
    transactions=[]
    if len(Blockchain.blocks) == 1:
        previous_hash = '0000'
    else:
        previous_hash = Blockchain.blocks[-1].hash
   # previous_hash = Blockchain.blocks[-1].hash
    new_block = Block(nonce, transactions, timeStamp, previous_hash, hash)
    print("Block was succesfully added")
    return func()'''




Blockchain.create_genesisBlock()
def func():
    while True:
        print("Choose 1 - to add transaction")
        print("Choose 2 - to add block")
        print("Choose 3 - to see the blockchain")
        choice = input("Enter your choice:")
        if (choice == "1"):
            get_transaction_info()
            break
        elif (choice == "2"):
            mine_or_add_block()
            break
        elif (choice == "3"):
            for b in Blockchain.blocks:
                print('Block: ', b.index)
                print('nonce: ', b.nonce)
                print('transactions: ', b.transactions)
                print('timeStamp: ' ,b.timeStamp)
                print('previous_hash: ' ,b.previous_hash)
                print( 'hash: ',b.hash)
                print('merkle root:', b.merkle_root)
                print()
            return func()
            #break
        else:
            print("Enter correct option")

func()

#block2=Block(10, [], datetime.datetime.now(), '0', '0' )






