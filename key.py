""" Programmer: Walter Reeves """
import datetime as date
import secrets
from base64 import urlsafe_b64encode


class Key:
    """ Represents each encryption key made. """

    @staticmethod
    def generate(num_bytes=64):
        """ Creates a new key. """
        now = date.datetime.now()

        return Key(secrets.token_bytes(num_bytes),
                   now + date.timedelta(seconds=1_000),
                   now + date.timedelta(seconds=10_000_000),
                   now + date.timedelta(seconds=1_000_000_000))

    def __init__(self, obj_bytes, activates_on, deactivates_on, expires_on):
        self.bytes = obj_bytes
        self.activates_on = activates_on
        self.deactivates_on = deactivates_on
        self.expires_on = expires_on

    def __bytes__(self) -> bytes:
        return self.bytes

    def to_json(self) -> dict[str, any]:
        """ Converts the key to .json file type. """
        return {"k": str(self.as_base64url(), "utf-8")}

    def as_base64url(self) -> bytes:
        """ Converts the object to base 64. """
        return urlsafe_b64encode(self.bytes)

    def status(self) -> bool or None:
        """ Determines if key is activated, deactivated, or expired. """
        if self.is_activated():
            return True
        elif self.is_deactivated():
            return False
        elif self.is_expired():
            return None
        else:
            return self.activates_on

    def is_activated(self):
        """ Checks to see if the key is activated. """
        if self.activates_on > date.datetime.now():
            return True
        else:
            return False

    def is_deactivated(self):
        """ Checks to see if the key is deactivated. """
        if self.deactivates_on > date.datetime.now():
            return True
        else:
            return False

    def is_expired(self):
        """ Checks to see if the key is expired. """
        if self.expires_on > date.datetime.now():
            return True
        else:
            return False
