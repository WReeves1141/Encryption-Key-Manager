from datetime import datetime

class Key:

    @staticmethod
    def generate(num_bytes: int) -> Key:
        pass

    def __init__(self, obj_bytes: bytes, activates_on: datetime,
                 deactivates_on: datetime, expires_on: datetime):
        self.bytes = bytes
        self.activates_on = activates_on
        self.deactivates_on = deactivates_on
        self.expires_on = expires_on

    def __bytes__(self) -> bytes:
        pass

    def to_json(self) -> dict[str, any]:
        pass

    def as_base64url(self) -> bytes:
        pass

    def is_activated(self) -> bool:
        pass

    def is_deactivated(self) -> bool:
        pass

    def is_expired(self) -> bool:
        pass
