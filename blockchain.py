import datetime
import json
import hashlib

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "data": self.data,
            "timestamp": self.timestamp,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(prev_block.index + 1, data, prev_block.hash)
        self.chain.append(new_block)
        return new_block

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            block = chain[block_index]
            if block.prev_hash != previous_block.hash:
                return False
            previous_block = block
            block_index += 1
        return True

# Example usage:
blockchain = Blockchain()
blockchain.add_block("eshat")
blockchain.add_block("tonu")
blockchain.add_block("tanvir")
blockchain.add_block("asif")
blockchain.add_block("olin")
blockchain.add_block("parvej")

difficulty = 4
for block in blockchain.chain:
    block.mine_block(difficulty)

is_valid = blockchain.chain_valid(blockchain.chain)
print(f"Is the blockchain valid? {is_valid}")

for block in blockchain.chain:
    print(f"Block Number: {block.index}")
    print(f"Block Nonce :{block.nonce}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Block Data: {block.data}")
    print(f"Block Hash: {block.hash}")
    print(f"Previous Hash: {block.prev_hash}")

    print()
