from PIL import Image
import numpy as np

def bpcs_decrypt(image_path):
    # Load steganographic image
    stego_image = Image.open(image_path)

    # Convert image to NumPy array of int16
    pixel_array = np.array(stego_image, dtype=np.int16)

    # Initialize an empty string to store the extracted binary message
    extracted_binary_message = ''

    # Extract BPCS steganography for all bit-planes
    row, col, channels = pixel_array.shape
    for bit_plane in range(channels):
        for i in range(row):
            for j in range(col):
                extracted_binary_message += str(pixel_array[i, j, bit_plane] & 1)  # Extract the least significant bit

    # Convert the binary message to ASCII characters
    extracted_message = ''.join([chr(int(extracted_binary_message[i:i+8], 2)) for i in range(0, len(extracted_binary_message), 8)])

    return extracted_message

# Example usage for decrypting JPEG image
stego_image_path = 'GambarAfter/parrots1.jpeg'
extracted_message = bpcs_decrypt(stego_image_path)

print("Extracted Message:", extracted_message)
