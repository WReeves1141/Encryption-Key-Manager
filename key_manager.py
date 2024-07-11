""" Programmer: Walter Reeves """
from base64 import urlsafe_b64encode
from key import Key


class KeyManager:
    """ ? """
    @staticmethod
    def generate(num_keys) -> list:
        """ Generates keys. """
        keys = []
        for num in range(1, num_keys + 1):
            keys.append(Key.generate())
        return keys

    def to_json(self) -> dict[str, any]:
        """ Converts the key to .json file type. """
        key_dict = {}
        Key.to_json()

        return key_dict

    def get_encryption_key(self):
        """ ? """
        pass

    def get_encryption_keys(self) -> tuple:
        """ ? """
        pass

    def get_decryption_keys(self) -> tuple:
        """ ? """
        pass
