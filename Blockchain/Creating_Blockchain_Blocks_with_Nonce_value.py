import hashlib
import time

NONCE_LIMIT = 2573394689

zeros = 3

class Blockchain:
    def __init__(self, Block_number,No_Of_Transactions,timestap,data,PH,hash,nonce,chain):
        self.Block_number = Block_number
        self.No_Of_Transactions = No_Of_Transactions
        self.timestap = timestap
        self.data = data
        self.PH = PH
        self.hash = hash
        self.nonce = nonce
        self.chain = chain
       
        
    def mine(self):
        for self.nonce in range(NONCE_LIMIT):
            base_text = str(self.Block_number) + self.No_Of_Transactions + self.timestap + self.data +  self.PH + str(self.nonce)
            hash_try = hashlib.sha256(base_text.encode()).hexdigest()
            # print(self.nonce)


            # if this hash_try which is a string starts with the character 0
            # four time then we are going to say 
            if hash_try.startswith('0' * zeros):
                print(f"Found Hash With Nonce: {self.nonce} ")
                print()
                return hash_try
        # if we go through all the numbers without finding such a hash
        # then we will return 
        return -1
    def hash_value(self):
        # for printing hash value
        combined_text = str(self.Block_number) + self.No_Of_Transactions + self.timestap + self.data +  self.PH + str(self.nonce)
        self.hash = hashlib.sha256(combined_text.encode()).hexdigest()

        # Creating the initial block and storing it in the chain
        genesis_block = Blockchain(self.Block_number,self.No_Of_Transactions,self.timestap,self.data,self.PH,self.hash,self.nonce,self.chain)
        self.chain.append(genesis_block)

    
    def add_blocks_to_the_genesis_block(self):
        self.mine()
        previous_hash = self.chain[-1]
        new_hash = str(self.Block_number) + self.No_Of_Transactions + self.timestap + self.data +  self.PH + str(self.nonce)
        self.hash = hashlib.sha256(new_hash.encode()).hexdigest()
        new_block = Blockchain(self.Block_number,self.No_Of_Transactions,self.timestap,self.data,previous_hash.hash,self.hash,self.nonce,self.chain)
        self.chain.append(new_block)




timestap = int(time.time())
PH = "0"
hash = 0
nonce = []
chain = []
obj1 = Blockchain(1,"1",str(timestap),"Genesis Block",PH,hash,nonce,chain)
obj2 = Blockchain(2,"123",str(timestap),"transaction 1",PH,hash,nonce,chain)
obj3 = Blockchain(3,"345",str(timestap),"transaction 2",PH,hash,nonce,chain)
obj1.mine()
obj1.hash_value()
obj2.add_blocks_to_the_genesis_block()
obj3.add_blocks_to_the_genesis_block()


for block in obj1.chain:
    print(f"Block_Number:{block.Block_number}")
    print(f"Nonce: {block.nonce}")
    print(f"No_Of_Transactions: {block.No_Of_Transactions}")
    print(f"Timestap: {block.timestap}")
    print(f"Data: {block.data}")
    print(f"PH : {block.PH} ")
    print(f"hash: {block.hash}")
    print()








