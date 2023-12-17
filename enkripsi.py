# encryption.py
from cryptography.fernet import Fernet
import os
import time

def generate_key():
    return Fernet.generate_key()

def load_key_from_file(filename):
    return open(filename, 'rb').read()

def save_key_to_file(key, filename):
    with open(filename, 'w') as key_file:
        key_file.write(key.decode())  # Decode the key to convert bytes to string

def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    start_time = time.time()  # Record the start time
    cipher_text = cipher_suite.encrypt(data.encode())
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    return cipher_text, execution_time

def main():
    # Memeriksa apakah kunci sudah ada atau perlu dibuat baru
    if not os.path.exists('secret.key'):
        key = generate_key()
        print("Kunci baru telah dibuat:", key)
        save_key_to_file(key, 'secret.key')
    else:
        key = load_key_from_file('secret.key')

    # Menampilkan kunci saat ini
    print("Kunci saat ini:", key)

    # Simpan kunci terenkripsi ke dalam file
    save_key_to_file(key, 'secret_key.txt')

    # Memasukkan data dari pengguna
    data_to_encrypt = input("Masukkan data yang ingin dienkripsi: ").strip()

    # Proses enkripsi
    encrypted_data, execution_time = encrypt_data(key, data_to_encrypt)
    print("Data setelah dienkripsi:", encrypted_data)

    # Simpan data terenkripsi ke dalam file
    with open('encrypted_data.txt', 'wb') as file:
        file.write(encrypted_data)

    # Menampilkan waktu eksekusi
    print("Waktu eksekusi enkripsi:", execution_time, "detik")

if __name__ == "__main__":
    main()
