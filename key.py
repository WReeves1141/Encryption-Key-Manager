"""Key class to create the Key objects."""

__all__ = ["Key"]
__author__ = "Walter Reeves"

from base64 import urlsafe_b64encode
from datetime import datetime, timedelta
from math import floor
from secrets import token_bytes


class Key:
    """Creates the Key object."""

    @staticmethod
    def generate(num_bytes=64):
        """Creates a new Key object and returns a Key object."""
        now = datetime.now()

        return Key(token_bytes(num_bytes),
                   now + timedelta(seconds=1_000),
                   now + timedelta(seconds=10_000_000),
                   now + timedelta(seconds=1_000_000_000))

    def __init__(self, obj_bytes, activates_on, deactivates_on, expires_on):
        self.bytes = obj_bytes
        self.activates_on = activates_on
        self.deactivates_on = deactivates_on
        self.expires_on = expires_on

    def __bytes__(self):
        return self.bytes

    def to_json(self):
        """Converts the Key object to JSON and returns a dictionary."""

        return {"k": str(self.as_base64url(), "utf-8"),
                "activatesOn": floor(self.activates_on.timestamp()),
                "deactivatesOn": floor(self.deactivates_on.timestamp()),
                "expiresOn": floor(self.expires_on.timestamp())}

    def as_base64url(self) -> bytes:
        """Creates a Base64 URL and returns a bytes object."""

        return urlsafe_b64encode(self.bytes)

    def is_activated(self) -> bool:
        """Checks if the Key object is active and returns a bool."""

        return (self.activates_on <= datetime.now()
                and not self.is_deactivated())

    def is_deactivated(self) -> bool:
        """Checks if the Key object is deactivated and returns a bool."""

        return (self.deactivates_on <= datetime.now()
                and not self.is_expired())

    def is_expired(self) -> bool:
        """Checks if the Key object is expired and returns a bool."""

        return self.expires_on <= datetime.now()
