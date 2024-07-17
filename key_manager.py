"""Key Manager class for the Key objects."""

__all__ = ["KeyManager"]
__author__ = "Walter Reeves"

from key import Key
import secrets


class KeyManager:
    """Manages the Key objects."""

    @staticmethod
    def generate(num_keys):
        """Generates a list of keys and returns a KeyManager object."""
        key_bytes = 64

        return KeyManager([Key.generate(key_bytes) for _ in range(1, num_keys + 1)])

    def __init__(self, keys):
        self.keys = keys

    def to_json(self):
        """Converts a Key object to JSON and returns a dictionary."""

        return {"keys": [key.to_json() for key in self.keys]}

    def get_encryption_key(self):
        """Gets a random key and returns a Key object."""

        return secrets.choice(self.get_encryption_keys())

    def get_encryption_keys(self):
        """Gets all active encryption keys and returns a tuple."""

        return tuple(key for key in self.keys if key.is_activated()
                     and not key.is_deactivated())

    def get_decryption_keys(self):
        """Gets all active decryption keys and returns a tuple."""

        return tuple(key for key in self.keys if key.is_activated()
                     or key.is_deactivated() and not key.is_expired())
