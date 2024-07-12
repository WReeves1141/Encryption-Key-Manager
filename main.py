""" Programmer: Walter Reeves """
# Testing Document
from key_manager import KeyManager

keys_to_generate = int(input("Enter the number of keys to generate > "))

print(KeyManager.generate(num_keys=keys_to_generate).get_encryption_keys())

