from PIL import Image
import numpy as np

def bpcs_steganography(image_path, message_path, output_path):
    # Load image
    image = Image.open(image_path)

    # Convert image to RGB mode (if it's not already)
    image = image.convert('RGB')

    # Convert image to NumPy array of int16
    pixel_array = np.array(image, dtype=np.int16)

    # Read the message from the file
    with open(message_path, 'r') as file:
        message = file.read()

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Perform BPCS steganography for all bit-planes
    for i in range(len(binary_message)):
        row, col, channels = pixel_array.shape
        for bit_plane in range(channels):
            pixel_array[:, :, bit_plane] = (pixel_array[:, :, bit_plane] & ~1).astype(np.int16)  # Clear the least significant bit
            if i < len(binary_message):
                pixel_array[:, :, bit_plane] |= (int(binary_message[i]) & 1)  # Set the bit to the message bit

    # Convert back to uint8 before saving
    pixel_array = pixel_array.astype(np.uint8)

    # Save the steganographic image
    stego_image = Image.fromarray(pixel_array)
    stego_image.save(output_path)

# Example usage for JPEG image
image_path = 'GambarBefore/parrots.jpeg'
message_path = 'encrypted_data.txt'  # Assuming 'encrypt.txt' contains the secret message
output_path = 'GambarAfter/parrots1.jpeg'
bpcs_steganography(image_path, message_path, output_path)


