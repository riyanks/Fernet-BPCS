# decryption.py
from cryptography.fernet import Fernet
import os
import time

def load_key_from_file(filename):
    return open(filename, 'r').read().encode()  # Encode the key to convert string to bytes

def decrypt_data(key, cipher_text):
    cipher_suite = Fernet(key)
    start_time = time.time()  # Record the start time
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    return plain_text, execution_time

def main():
    # Memeriksa apakah kunci sudah ada atau perlu dibuat baru
    key_filename = 'secret_key.txt'
    if not os.path.exists(key_filename):
        print("File kunci tidak ditemukan. Silakan buat kunci terlebih dahulu.")
        return
    else:
        key = load_key_from_file(key_filename)

    # Menanyakan apakah pengguna ingin mengubah kunci
    change_key_response = input("Apakah Anda ingin mengubah kunci? (y/n): ").strip().lower()

    if change_key_response == 'y':
        key = change_key()

    # Baca data terenkripsi dari file
    with open('encrypted_data.txt', 'rb') as file:
        encrypted_data = file.read()

    # Proses dekripsi
    decrypted_data, execution_time = decrypt_data(key, encrypted_data)
    print("Data setelah didekripsi:", decrypted_data)

    # Menampilkan waktu eksekusi
    print("Waktu eksekusi dekripsi:", execution_time, "detik")

if __name__ == "__main__":
    main()
