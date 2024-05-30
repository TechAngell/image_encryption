## Overview

## Image Encryption and Decryption Tool
This Python program provides a simple tool for encrypting and decrypting images using pixel manipulation techniques.

## Features
* Encrypts images using XOR or shifting operations on pixel values.
* Decrypts images encrypted with the same method and key.
* User-friendly interface for choosing encryption/decryption mode, image path, and key.
* Saves encrypted/decrypted images with informative suffixes.
  
## Installation
* This program requires the Pillow library for image processing. You can install it using pip:

Bash
pip install Pillow

## Usage
- Clone or download this repository.
- Run the program using Python:
  Bash
python image_encryption.py

- The program will prompt you for the following:
  Mode (encrypt 'e' or decrypt 'd')
  Image path
  Encryption/Decryption key (integer)
  Pixel manipulation operation (XOR or Shift)
- Follow the prompts and provide the necessary information.
- The program will process the image and save the encrypted/decrypted version with a suffix indicating the operation used.

## Example Usage
Encrypting an image:

Enter 'e' to encrypt or 'd' to decrypt: e
Enter the image path: path/to/image.jpg
Enter the encryption/decryption key (integer): 123
Choose pixel manipulation operation:
  1. XOR
  2. Shift
Enter your choice (1-2): 1
Image encrypted and saved with suffix 'encrypted'.
The original image will remain unchanged, and a new encrypted version named "encrypted.jpg" will be created in the same location.

Decrypting an encrypted image:

Enter 'e' to encrypt or 'd' to decrypt: d
Enter the image path: path/to/image_encrypted.jpg
Enter the encryption/decryption key (integer): 123
Choose pixel manipulation operation:
  1. XOR
  2. Shift
Enter your choice (1-2): 1
Image decrypted and saved with suffix 'decrypted'.
The encrypted image will be decrypted and saved as "decrypted.jpg".

## Limitations
This program offers a basic level of encryption and might not be suitable for highly sensitive data.
It modifies pixel values, potentially affecting image quality. Consider working on a copy of the original image.
