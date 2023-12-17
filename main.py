from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key_from_file(filename):
    return open(filename, 'rb').read()

def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt_data(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

def change_key():
    new_key = generate_key()
    save_key_to_file(new_key, 'secret.key')
    return new_key

# Memeriksa apakah kunci sudah ada atau perlu dibuat baru
if not os.path.exists('secret.key'):
    key = generate_key()
    print("Kunci baru telah dibuat:", key)
    save_key_to_file(key, 'secret.key')
else:
    key = load_key_from_file('secret.key')

# Menampilkan kunci saat ini
print("Kunci saat ini:", key)

# Menanyakan apakah pengguna ingin mengubah kunci
change_key_response = input("Apakah Anda ingin mengubah kunci? (y/n): ").strip().lower()

if change_key_response == 'y':
    key = change_key()

# Memasukkan data dari pengguna
data_to_encrypt = input("Masukkan data yang ingin dienkripsi: ").strip()

# Proses enkripsi
encrypted_data = encrypt_data(key, data_to_encrypt)
print("Data setelah dienkripsi:", encrypted_data)

# Proses dekripsi
decrypted_data = decrypt_data(key, encrypted_data)
print("Data setelah didekripsi:", decrypted_data)
