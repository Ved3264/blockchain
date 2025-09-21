import hashlib
import json
import time


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        new_block = Block(len(self.chain), transactions, self.get_latest_block().hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}:")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Transactions: {block.transactions}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")


class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.candidates = {}
        self.voters = {}

    def add_candidate(self):
        candidate_id = input("Enter Candidate ID: ")
        if candidate_id in self.candidates:
            print("Candidate ID already exists!")
            return
        name = input("Enter Candidate Name: ")
        self.candidates[candidate_id] = {"id": candidate_id, "name": name}
        print("Candidate added successfully!")

    def add_voter(self):
        voter_id = input("Enter Voter ID: ")
        if voter_id in self.voters:
            print("Voter ID already exists!")
            return
        name = input("Enter Voter Name: ")
        self.voters[voter_id] = {"id": voter_id, "name": name, "has_voted": False}
        print("Voter added successfully!")

    def cast_vote(self):
        voter_id = input("Enter Voter ID: ")
        if voter_id not in self.voters:
            print("Voter not found!")
            return
        if self.voters[voter_id]["has_voted"]:
            print("This voter has already voted!")
            return

        print("\nCandidates:")
        for cid, cinfo in self.candidates.items():
            print(f"{cid}: {cinfo['name']}")

        candidate_id = input("Enter Candidate ID to vote for: ")
        if candidate_id not in self.candidates:
            print("Invalid Candidate ID!")
            return

        # Record vote
        transaction = {
            "voter_id": voter_id,
            "voter_name": self.voters[voter_id]["name"],
            "candidate_id": candidate_id,
            "candidate_name": self.candidates[candidate_id]["name"]
        }
        self.blockchain.add_block(transaction)
        self.voters[voter_id]["has_voted"] = True
        print("Vote successfully cast!")

    def menu(self):
        while True:
            print("\n--- Voting Management System ---")
            print("1. Add Candidate")
            print("2. Add Voter")
            print("3. Cast Vote")
            print("4. Print Blockchain")
            print("5. Validate Chain")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_candidate()
            elif choice == "2":
                self.add_voter()
            elif choice == "3":
                self.cast_vote()
            elif choice == "4":
                self.blockchain.print_chain()
            elif choice == "5":
                print("Blockchain valid:", self.blockchain.is_chain_valid())
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    VotingSystem().menu()
