'''

BLOCKCHAIN IN PYTHON

Today we build a simple blockchain, which represents a fictional cryptocurrency in Python.

Cryptocurrency -> NeuralCoin(NC)

NC has transactions for example 

(t1 -> transaction 1)

t1: anna sends bob 2 NC
t2: bob send daniel 4.3 NC
t3: mark sends charlie 3.2 NC



these are three basic transaction and these three transactions can be 
stored in a block lets say we have a block->

B1 which is initial block and this block has information about those 
three transactions because it is an initial block it doesn't have any
hash information

B1("AAA",t1,t2,t3) -> certain hash output 76f45h (hexadecimal number)
B2("76f45h",t4,t5,t6) -> 8923ft
     PH->Previous hash of previous block
B3("8923FH",t7,t8,t9) -> 8975fe


WE ARE GOING TO USE ->

1.hashlib -> is a Python library that provides a common interface to various hash functions. Hash functions are algorithms 
that take an input (or "message") and return a fixed-size string of bytes, which is typically a hexadecimal number.

2.SHA-256 ->  (Secure Hash Algorithm 256-bit) is one specific hash function that is a part of the SHA-2 (Secure Hash Algorithm 2) 
family of cryptographic hash functions. SHA-256 takes an input message and produces a 256-bit (32-byte) fixed-size hash value.

In Python, you can use the hashlib library to compute the SHA-256 hash of a message or data.

'''
import hashlib


class NeuralCoinBlock:
    
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        # data string
        # we are going to use dash(-) as a separator and join all the 
        # transactions from the transaction list into one string plus
        # previous_block_hash in the end

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() 
        # this is how we calculate hash



# Transactions ->

t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Charly"
t6 = "Mike sends 5.4 NC to Daniel"

# creating initial block ->

initial_block = NeuralCoinBlock("Initial String",[t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)


second_block = NeuralCoinBlock(initial_block.block_hash,[t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block =  NeuralCoinBlock(second_block.block_hash,[t5,t6])

print(third_block.block_data)
print(third_block.block_hash)















































































 
