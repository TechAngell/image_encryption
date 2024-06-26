from PIL import Image

def encrypt_image(image_path, key):
  
  img = Image.open(image_path)
  pixels = img.load()
  width, height = img.size

  for y in range(height):
    for x in range(width):
      red, green, blue = pixels[x, y]
      new_red = red ^ key
      new_green = green ^ key
      new_blue = blue ^ key
      pixels[x, y] = (new_red, new_green, new_blue)

  img.save("encrypted.png")

def decrypt_image(image_path, key):
  
  img = Image.open(image_path)
  pixels = img.load()
  width, height = img.size

  for y in range(height):
    for x in range(width):
      red, green, blue = pixels[x, y]
      new_red = red ^ key
      new_green = green ^ key
      new_blue = blue ^ key
      pixels[x, y] = (new_red, new_green, new_blue)

  img.save("decrypted.png")

def main():
 
  while True:
    print("Enter 'e' to encrypt or 'd' to decrypt:")
    mode = input().lower()
    if mode in ('e', 'd'):
      break
    else:
      print("Invalid mode. Please enter 'e' or 'd'.")

  print("Enter the image path:")
  image_path = input()
  print("Enter the encryption/decryption key (integer):")
  key = int(input())

  if mode == 'e':
    encrypt_image(image_path, key)
    print("Image encrypted and saved as 'encrypted.png'.")
  else:
    decrypt_image(image_path, key)
    print("Image decrypted and saved as 'decrypted.png'.")

if __name__ == "__main__":
  main() 