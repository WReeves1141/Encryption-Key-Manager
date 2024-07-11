""" Programmer: Walter Reeves """
from key_manager import KeyManager
# from key import Key

NUMBER_OF_BYTES = 64


key_manager = KeyManager


keys_to_generate = int(input("Enter the number of keys to generate > "))
key = key_manager.generate(num_keys=keys_to_generate)

print(key)

# if key.status():
#     print("Key is active.")
# elif not key.status():
#     print("Key is deactivated.")
# else:
#     print("Key is expired.")
