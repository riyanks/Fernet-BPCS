# FERNET with BPCS
This project demonstrates how to use the Fernet symmetric key encryption scheme for encrypting and decrypting data in Python.
This project demonstrates BPCS (Bit-Plane Complexity Segmentation) steganography using Python. It includes encryption and decryption scripts and uses the cryptography library for message encryption.

## Installation
Make sure you have Python installed. You can install the required packages using:

```bash
pip install -r requirements.txt
```
## Run App

Run this for encryption process
```bash
python enkripsi.py
```
Run this for decryption process
```bash
python dekripsi.py
```
Run this for eknripsi to BPCS process
```bash
python stegano.py
```
run this for BPCS to dekripsi process
```bash
python steganodecr.py
```

## Change Picture
Open stegano.py file and change this path

````python
image_path = 'GambarBefore/parrots.jpeg'# change to your path
message_path = 'encrypted_data.txt' 
output_path = 'GambarAfter/parrots1.jpeg' #change to your path
````
