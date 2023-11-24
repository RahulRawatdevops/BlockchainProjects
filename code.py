import hashlib
import time

class Block:
  def --init--(self, index, previous_hash, timestamp, data, hash):
  self.index = index
  self.previous_hash = previous_hash
  self.timestamp = timestamp
  self.data = data
  self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
  value = str(index) + str(previous_hash) + str(timestamp) + str(data)
  return hashlib.sha256(value.encode()).hexdgest()

def create_genesis_blockk():
  return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Gebesis Block"))

def create_new_block(previous_block, data):
  index = previous_block.index + 1
  timestamp = time.time()
  hash = calculate_hash(index, prvious_block.hash, timestamp, data)
  return Block(index, previous_block.hash, timestamp, data, hash)

#Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]


#Add blocks to the blockchain

num_blocks_to_add = 10
for i in range(num_blocks_to_add):
  data = f"Block #{i+1} data"
  new_block = create_new_block(previous_block, data)
  blockchain.append(new_block)
  previous_block = new_block
  print(f"Blcok)
  print(f"Hash)





