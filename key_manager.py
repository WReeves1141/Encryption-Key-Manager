""" Programmer: Walter Reeves """
from base64 import urlsafe_b64encode
from key import Key
import secrets


class KeyManager:
    """ Man the keys created in the Key class. """
    @staticmethod
    def generate(num_keys):
        """ Generates the keys in a list. """

        return KeyManager([Key.generate() for _ in range(1, num_keys + 1)])

    def __init__(self, keys):
        self.keys = keys

    def to_json(self) -> dict[str, any]:
        """ Converts the key to .json file type. """

        return {"keys": [key.to_json() for key in self.keys]}

    def get_encryption_key(self) -> Key:
        """ Provides a random key to the user. """

        return secrets.choice(self.get_encryption_keys())

    def get_encryption_keys(self) -> tuple:
        """ Gets all possible encryption keys  """

        return tuple(key for key in self.keys if key.is_activated()
                     and not key.is_deactivated())

    def get_decryption_keys(self) -> tuple:
        """ Gets all active decryption keys. """

        return tuple(key for key in self.keys if key.is_activated()
                     or key.is_deactivated() and not key.is_expired())
