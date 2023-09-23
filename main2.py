import datetime
from random import randint
import hashlib

'''def f1():
    list_of_nonce=[]
    while len(list_of_nonce)<(5):
        unique_nonce = randint(1, 5)
        if unique_nonce not in list_of_nonce:
            list_of_nonce.append(unique_nonce)
            return unique_nonce'''

class BlockChain:
    index = 0
    blocks = []
    def __init__(self, data=str):
        BlockChain.index += 1
        self.index = BlockChain.index
        prev_index= self.index-1
        if self.index>1:
            previous_hash = BlockChain.blocks[prev_index-1].hash
           # previous_hash='0000'
        else:
            previous_hash = '0000'
        self.timeStamp = datetime.datetime.now()
        self.data = data
        self.nonce = randint(0, 2**32)
        self.block_data = (str(previous_hash) + '+' + str(data)).encode()
        self.hash = hashlib.sha256(self.block_data).hexdigest()
        BlockChain.blocks.append(self)

tr1 = 'b1 sends MMM 2.5 btc'
b1 = BlockChain(tr1)
print(b1.index)
print(b1.timeStamp)
print(b1.data)
print(b1.nonce)
print(b1.block_data)
print(b1.hash)
print()

tr2 = 'b2 sends YYY 2.5 btc'
b2 = BlockChain(tr2)
print(b2.index)
print(b2.timeStamp)
print(b2.data)
print(b2.nonce)
print(b2.block_data)
print(b2.hash)

print()
print(BlockChain.blocks[0].index)

tr3 = 'b3 sends WWW 3.5 btc'
b3 = BlockChain(tr3)
print(b3.index)
print(b3.timeStamp)
print(b3.data)
print(b3.nonce)
print(b3.block_data)
print(b3.hash)

