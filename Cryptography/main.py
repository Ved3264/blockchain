import sys
from crypto_utils import sha256_hash, generate_key_pair, sign_message, verify_signature
from vehicle_registry import VehicleRegistry

def main():
    registry = VehicleRegistry()
    private_key, public_key = None, None

    while True:
        print("\n===== Blockchain Assignment 2 Menu =====")
        print("1. SHA-256 Hash a Message")
        print("2. Digital Signature (Generate/Sign/Verify)")
        print("3. Vehicle Registration System")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            msg = input("Enter message: ")
            print("SHA-256 Hash:", sha256_hash(msg))

        elif choice == "2":
            print("\n--- Digital Signature Menu ---")
            print("a. Generate Key Pair")
            print("b. Sign Message")
            print("c. Verify Signature")
            sub_choice = input("Select option: ").strip().lower()

            if sub_choice == "a":
                private_key, public_key = generate_key_pair()
                print("Key pair generated successfully.")
            elif sub_choice == "b":
                if not private_key:
                    print("Generate keys first!")
                    continue
                msg = input("Enter message to sign: ")
                signature = sign_message(private_key, msg)
                print("Signature (hex):", signature.hex())
                # store signature for verify step
                global last_signature, last_message
                last_signature, last_message = signature, msg
            elif sub_choice == "c":
                if not public_key:
                    print("Generate keys first!")
                    continue
                try:
                    valid = verify_signature(public_key, last_message, last_signature)
                    print("Signature valid:", valid)
                except NameError:
                    print("No signed message available. Sign a message first.")

        elif choice == "3":
            print("\n--- Vehicle Registry Menu ---")
            print("a. Register Vehicle")
            print("b. Get Vehicle Details")
            sub_choice = input("Select option: ").strip().lower()

            if sub_choice == "a":
                plate = input("Number Plate: ").upper()
                owner = input("Owner Name: ")
                model = input("Model: ")
                if registry.register_vehicle(plate, owner, model):
                    print("Vehicle registered successfully.")
                else:
                    print("Error: Number plate already exists!")
            elif sub_choice == "b":
                plate = input("Enter Number Plate: ").upper()
                details = registry.get_vehicle(plate)
                if details:
                    print(f"Owner: {details['owner']}, Model: {details['model']}")
                else:
                    print("Vehicle not found.")

        elif choice == "4":
            print("Exiting...")
            sys.exit(0)

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
