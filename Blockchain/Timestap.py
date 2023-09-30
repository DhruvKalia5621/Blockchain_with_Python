'''
HOW TO CALCULATE TIMESTAP->>>

It's important to note that the timestamp in a blockchain is typically 
recorded in Unix timestamp format, which represents the number of seconds 
since January 1, 1970 (the Unix epoch). This standardized format makes 
it easy to compare and verify timestamps across different systems and 
nodes within the blockchain network.

In summary, a timestamp in a blockchain is a critical piece of 
metadata associated with blocks, transactions, or events. It helps 
establish order, provides proof of time, contributes to consensus 
mechanisms, and plays a fundamental role in maintaining the 
blockchain's integrity and security.


'''

import datetime

current_datetime = datetime.datetime.now()
# print(current_datetime)
# output -> 2023-09-25 10:45:12.635526

unix_epoch = datetime.datetime(1970, 1, 1)
# print(unix_epoch)
# output -> 1970-01-01 00:00:00

timestamp = (current_datetime - unix_epoch).total_seconds()
# print(timestamp)
# output -> 1695638815.375689

# Rounding to 3 decimal places
timestamp = round(timestamp, 3)
# print(timestamp)
# output -> 1695638920.864

# Converting to an integer (remove fractions)
timestamp = int(timestamp)
# print(timestamp)
# output -> 1695638968




