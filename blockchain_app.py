import streamlit as st
import hashlib
import time
import json
from tabulate import tabulate

# Initialize session state
if "blockchain" not in st.session_state:
    st.session_state.blockchain = [
        {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
        }
    ]

# Function to add block
def add_block(data):
    previous_block = st.session_state.blockchain[-1]
    index = previous_block["index"] + 1
    timestamp = time.time()
    previous_hash = previous_block["hash"]
    block_content = f"{index}{timestamp}{data}{previous_hash}"
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()

    new_block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    st.session_state.blockchain.append(new_block)
    st.success(f"✅ Block {index} added successfully!")

# Function to validate blockchain
def validate_blockchain():
    for i in range(1, len(st.session_state.blockchain)):
        current = st.session_state.blockchain[i]
        previous = st.session_state.blockchain[i - 1]

        expected_prev_hash = previous["hash"]
        if current["previous_hash"] != expected_prev_hash:
            return False, current["index"]
    return True, None

# Function to tamper a block
def tamper_block(index, new_data):
    if 0 < index < len(st.session_state.blockchain):
        st.session_state.blockchain[index]["data"] = new_data
        st.session_state.blockchain[index]["hash"] = hashlib.sha256(new_data.encode()).hexdigest()
        st.warning(f"🚨 Block {index} has been tampered!")

# App layout
st.title("🧱 Simple Blockchain Demo")

st.subheader("➕ Add a New Block")
data_input = st.text_input("Enter data for new block")
if st.button("Add Block"):
    if data_input:
        add_block(data_input)
    else:
        st.error("Please enter data to add a block.")

st.subheader("📜 View Blockchain")

# Table View
if st.checkbox("Show Table View"):
    table_data = [
        [
            blk["index"],
            blk["data"],
            time.ctime(blk["timestamp"]),
            blk["previous_hash"],
            blk["hash"]
        ]
        for blk in st.session_state.blockchain
    ]
    st.text("Blockchain Table View:")
    st.code(tabulate(table_data, headers=["Index", "Data", "Timestamp", "Prev Hash", "Hash"], tablefmt="fancy_grid"))

# JSON View
if st.checkbox("Show JSON View"):
    st.json(st.session_state.blockchain)

st.subheader("✅ Validate Blockchain")
if st.button("Validate Blockchain"):
    is_valid, invalid_block = validate_blockchain()
    if is_valid:
        st.success("✅ Blockchain is VALID! No tampering detected.")
    else:
        st.error(f"🚨 Blockchain is INVALID! Tampering detected at Block {invalid_block}")

st.subheader("🛠️ Tamper a Block")
tamper_index = st.number_input("Block index to tamper (excluding Genesis)", min_value=1, max_value=len(st.session_state.blockchain)-1, step=1)
tamper_data = st.text_input("New fake data:")
if st.button("Tamper Block"):
    tamper_block(tamper_index, tamper_data)

  
# Creating a simple block as a dictionary
block = {
    "index": 1,  # Block number
    "data": "Patient A - X-Ray Scan",  # Block content
    "timestamp": "2025-02-22 10:00:00",  # When the block was created
    "previous_block": None  # The first block has no previous block
}

# Display the block
print(block)

import time  # To add timestamp

# Function to create a block
def create_block(data, prev_hash):
    block = {
        "data": data,
        "timestamp": time.time(),  # Get the current time
        "previous_hash": prev_hash  # Link to previous block
    }
    return block

# Creating the first block (Genesis Block)
genesis_block = create_block("First Block", "None")

# Creating a second block linked to the first
second_block = create_block("Second Block", str(genesis_block))

# Printing the blocks
print("Genesis Block:", genesis_block)
print("Second Block:", second_block)

blockchain = []  # Our blockchain is just a list
blockchain.append(genesis_block)
blockchain.append(second_block)

# Print the blockchain
for block in blockchain:
    print("\nBlock:")
    print("Data:", block["data"])
    print("Timestamp:", block["timestamp"])
    print("Previous Hash:", block["previous_hash"])

    import hashlib  # Library for hashing

# Function to create a hashed block
def create_hashed_block(data, prev_hash):
    timestamp = str(time.time())  # Convert time to string for hashing
    block_data = data + timestamp + prev_hash  # Combine all info
    block_hash = hashlib.sha256(block_data.encode()).hexdigest()  # Generate hash

    block = {
        "data": data,
        "timestamp": timestamp,
        "previous_hash": prev_hash,
        "hash": block_hash  # Store the generated hash
    }
    return block

# Creating blocks with hashing
genesis_block = create_hashed_block("First Block", "None")
second_block = create_hashed_block("Second Block", genesis_block["hash"])

# Storing in blockchain list
blockchain = [genesis_block, second_block]

# Displaying blocks
for block in blockchain:
    print("\nBlock:")
    print("Data:", block["data"])
    print("Timestamp:", block["timestamp"])
    print("Previous Hash:", block["previous_hash"])
    print("Hash:", block["hash"])  # Display block hash

    import time  # To add timestamps

# Initialize an empty blockchain (list)
blockchain = []

# Function to create a block
def create_block(index, data, previous_hash):
    block = {
        "index": index,
        "data": data,
        "timestamp": time.time(),
        "previous_hash": previous_hash  # Stores the hash of the previous block
    }
    return block

# Creating the Genesis Block (First Block)
genesis_block = create_block(1, "Genesis Block", "0")  # Previous hash is "0" for the first block
blockchain.append(genesis_block)  # Add to the blockchain

# Print the Genesis Block
print("Genesis Block Created:")
print(genesis_block)

import hashlib  # To generate unique hashes

# Function to generate a unique hash for each block
def generate_hash(block):
    block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# Function to add a new block
def add_block(data):
    previous_block = blockchain[-1]  # Get the last block in the chain
    new_index = previous_block["index"] + 1  # New block index
    new_hash = generate_hash(previous_block)  # Hash of the last block

    # Create a new block
    new_block = create_block(new_index, data, new_hash)
    blockchain.append(new_block)  # Add to the blockchain

# Adding some new blocks
add_block("Patient A - MRI Scan")
add_block("Patient B - Blood Test")
add_block("Patient C - CT Scan")

# Print the blockchain
print("\nUpdated Blockchain:")
for block in blockchain:
    print("\nBlock Index:", block["index"])
    print("Data:", block["data"])
    print("Timestamp:", block["timestamp"])
    print("Previous Hash:", block["previous_hash"])

    # Function to display the blockchain
def display_blockchain():
    print("\n📜 Complete Blockchain:\n")
    for block in blockchain:
        print("=" * 40)
        print(f"🆔 Block Index: {block['index']}")
        print(f"📅 Timestamp: {time.ctime(block['timestamp'])}")
        print(f"📜 Data: {block['data']}")
        print(f"🔗 Previous Hash: {block['previous_hash']}")
        print("=" * 40)

# Call the function to display the blockchain
display_blockchain()

import json  # To format data nicely

# Function to display blockchain in JSON format
def display_blockchain_json():
    print("\n📜 Blockchain in JSON Format:\n")
    print(json.dumps(blockchain, indent=4))  # Pretty print with 4 spaces

# Call the function
display_blockchain_json()

from tabulate import tabulate  # Install using: pip install tabulate

# Function to display blockchain as a table
def display_blockchain_table():
    table_data = []
    for block in blockchain:
        table_data.append([
            block["index"],
            block["data"],
            time.ctime(block["timestamp"]),
            block["previous_hash"]
        ])

    print("\n📜 Blockchain Table View:\n")
    print(tabulate(table_data, headers=["Block Index", "Data", "Timestamp", "Previous Hash"], tablefmt="fancy_grid"))

# Call the function
display_blockchain_table()

import time
import hashlib

# Initialize blockchain with Genesis Block
blockchain = [
    {
        "index": 0,
        "timestamp": time.time(),
        "data": "Genesis Block",
        "previous_hash": "0",
        "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
    }
]

# Function to create a new block
def add_block(data):
    previous_block = blockchain[-1]  # Get last block
    index = previous_block["index"] + 1  # New block index
    timestamp = time.time()  # Current time
    previous_hash = previous_block["hash"]  # Hash of last block

    # Create block data as a string for hashing
    block_content = f"{index}{timestamp}{data}{previous_hash}"
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()  # Generate block hash

    # Create new block
    new_block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    blockchain.append(new_block)  # Add block to the blockchain
    print(f"\n✅ Block {index} added successfully!\n")


# Manually adding a block
user_data = input("Enter data for the new block: ")  # Taking input from user
add_block(user_data)

while True:
    user_data = input("\nEnter data for the new block (or type 'exit' to stop): ")
    if user_data.lower() == "exit":
        break
    add_block(user_data)

    import json

# Function to print blockchain in JSON format
def display_blockchain():
    print("\n📜 Final Blockchain:")
    print(json.dumps(blockchain, indent=4))

# Display blockchain
display_blockchain()

def validate_blockchain():
    for i in range(1, len(blockchain)):  # Start from the second block (index 1)
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        # Recalculate the hash of the previous block
        recalculated_prev_hash = previous_block["hash"]

        # If previous_hash stored in the current block doesn't match recalculated hash, the chain is broken
        if current_block["previous_hash"] != recalculated_prev_hash:
            print(f"\n🚨 Blockchain is INVALID! Tampering detected at Block {current_block['index']} 🚨")
            return False

    print("\n✅ Blockchain is VALID! No tampering detected.")
    return True

# Run blockchain validation
validate_blockchain()

# 🚨 Intentionally modifying a block to test validation 🚨
blockchain[1]["data"] = "Tampered Data"
blockchain[1]["hash"] = hashlib.sha256("Tampered Data".encode()).hexdigest()

print("\n🚨 Block 1 has been modified! 🚨")
validate_blockchain()  # Now the validation should fail