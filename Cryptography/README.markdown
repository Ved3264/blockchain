# Blockchain Assignment 2

## Overview
This project is a Python-based application demonstrating basic blockchain-related functionalities, including SHA-256 hashing, digital signatures using RSA encryption, and a simple vehicle registry system. The application provides an interactive command-line interface to perform these operations.

### Features
1. **SHA-256 Hashing**: Generate a SHA-256 hash for any input message.
2. **Digital Signatures**: Generate RSA key pairs, sign messages, and verify signatures.
3. **Vehicle Registry**: Register vehicles with a unique number plate and retrieve their details.

## Prerequisites
- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`

## Installation
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   ```
   cryptography
   ```

## Project Structure
- `main.py`: The main script containing the interactive CLI menu.
- `crypto_utils.py`: Utility functions for SHA-256 hashing and RSA digital signatures.
- `vehicle_registry.py`: Implementation of the vehicle registry system.
- `requirements.txt`: Lists the required Python packages.

## How to Run
1. Ensure all dependencies are installed (see Installation section).
2. Navigate to the project directory.
3. Run the main script:
   ```bash
   python main.py
   ```

4. Follow the interactive menu to:
   - Compute SHA-256 hashes for messages.
   - Generate RSA key pairs, sign messages, or verify signatures.
   - Register vehicles or retrieve vehicle details.
   - Exit the program by selecting option 4.

## Usage
Upon running `python main.py`, you will see a menu like this:
```
===== Blockchain Assignment 2 Menu =====
1. SHA-256 Hash a Message
2. Digital Signature (Generate/Sign/Verify)
3. Vehicle Registration System
4. Exit
```

### Example Interactions
1. **Hash a Message**:
   - Select option `1`, enter a message, and get its SHA-256 hash.

2. **Digital Signature**:
   - Select option `2`, then:
     - Choose `a` to generate a key pair.
     - Choose `b` to sign a message (requires key pair).
     - Choose `c` to verify the last signed message.

3. **Vehicle Registry**:
   - Select option `3`, then:
     - Choose `a` to register a vehicle with a number plate, owner name, and model.
     - Choose `b` to retrieve vehicle details by number plate.

4. **Exit**:
   - Select option `4` to exit the program.

## Notes
- The vehicle registry uses a simple in-memory dictionary, so data is not persisted between runs.
- The digital signature feature requires generating a key pair before signing or verifying messages.
- Ensure you have the `cryptography` package installed, as it is essential for RSA key generation and signing.

## Troubleshooting
- If you encounter a `ModuleNotFoundError`, ensure all dependencies are installed using `pip install -r requirements.txt`.
- If the program exits unexpectedly, verify your input matches the expected format (e.g., valid strings for messages or plate numbers).

