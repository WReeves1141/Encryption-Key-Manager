""" Programmer: Walter Reeves """
from base64 import urlsafe_b64encode
from math import floor

import datetime as date

import secrets


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
        """ Converts a key to JSON. """

        return {"k": str(self.as_base64url(), "utf-8"),
                "activatesOn": floor(self.activates_on.timestamp()),
                "deactivatesOn": floor(self.deactivates_on.timestamp()),
                "expiresOn": floor(self.expires_on.timestamp())}

    def as_base64url(self) -> bytes:
        """ Converts a key to base64. """

        return urlsafe_b64encode(self.bytes)

    def is_activated(self) -> bool:
        """ Checks if a key is activated. """

        return (self.activates_on <= date.datetime.now()
                and not self.is_deactivated())

    def is_deactivated(self) -> bool:
        """ Checks if a key is deactivated. """

        return (self.deactivates_on <= date.datetime.now()
                and not self.is_expired())

    def is_expired(self) -> bool:
        """ Checks if a key is expired. """

        return self.expires_on <= date.datetime.now()
