
import hashlib

NONCE_LIMIT = 2573394689

zeros = 3

def mine(block_number,transactions,previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        print(nonce)
        # if this hash_try which is a string starts with the character 0
        # four time then we are going to say 
        if hash_try.startswith('0' * zeros):
            print(f"Found Hash With Nonce: {nonce} ")
            return hash_try
        # if we go through all the numbers without finding such a hash
        # then we will return 
    return -1


# You can change the values of these three variables when you want a different nonce value . if you don't change any of these value no 
# matter how many times you run the the code the nonce value will be same.

block_number = 25
transactions = "7633731457844fcc378"
previous_hash = "87445efheyu7633735tg3"

combined_text = str(block_number) + transactions + previous_hash + str(3580)


# This code will generate nonce value

mine(block_number,transactions,previous_hash)
# output ->  3580

# This code will generate hash valueś

print(hashlib.sha256(combined_text.encode()).hexdigest())







        

'''


Explaination in Detail of the Code ->>>


This algorithm tries to find a nonce (a number) such that when combined with other data and hashed, the resulting hash starts 
with a certain number of zeros (specified by the zeros variable). This process is used to secure and validate transactions 
in a blockchain network.

Here's a step-by-step explanation of how the code works:

1.Constants and Variables:

NONCE_LIMIT = 100000000000: This constant represents the maximum value the nonce variable can take during the mining process.
zeros = 4: This variable determines how many leading zeros the hash must have for a successful mining attempt.

2.Mine Function:

This function takes three parameters:
block_number: An integer representing the block number.
transactions: A string representing the transactions in the block.
previous_hash: A string representing the hash of the previous block.
It iterates through nonce values from 0 to NONCE_LIMIT - 1.

2.Hash Computation:

Inside the loop, it constructs a base_text by concatenating block_number, transactions, previous_hash, and the current nonce as a string.
It then computes the SHA-256 hash of this base_text and stores it in the hash_try variable.

3.Checking for Valid Hash:

It checks if the hash_try starts with zeros number of consecutive zeros.
If it does, it means a valid hash has been found, and it prints the nonce and returns the hash.
If no valid hash is found after iterating through all nonce values, it returns -1 to indicate failure.

4.Main Part of the Code:

The main part of the code sets up some initial values for block_number, transactions, and previous_hash.
It then combines these values into a combined_text string and calculates the SHA-256 hash of this combined text, printing it.

5.Mining:

Finally, it calls the mine function with the provided parameters (block_number, transactions, and previous_hash).
The mine function tries to find a nonce that, when hashed with the other data, produces a hash with zeros leading zeros.
If it succeeds, it prints the nonce and the corresponding hash.



In a real blockchain network, mining is a computationally intensive process where miners compete to find a nonce that results in a 
valid hash. The difficulty of finding such a hash is determined by the number of leading zeros required (in this case, zeros).
As zeros increases, the difficulty increases, and it becomes harder to find a valid nonce. This proof-of-work mechanism is essential 
for ensuring the security and integrity of the blockchain.

'''

