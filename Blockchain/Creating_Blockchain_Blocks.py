import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))
        self.chain.append(genesis_block)

    def add_block(self, data):
        
        previous_block = self.chain[-1]
        index = len(self.chain)
        timestamp = int(time.time())
        hash = self.calculate_hash(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + str(timestamp) + data
        return hashlib.sha256(value.encode()).hexdigest()

my_blockchain = Blockchain()
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")


for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print()
