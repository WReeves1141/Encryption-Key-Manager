from key import Key

class KeyManager:

    @staticmethod
    def generate(num_keys: int) -> KeyManager:
        pass

    def __init__(self, keys: list[Key]) -> None:
        self.keys = Key

    def to_json(self) -> dict[str, any]:
        pass

    def get_encryption_key(self) -> Key:
        pass

    def get_encryption_keys(self) -> tuple:
        pass

    def get_decryption_keys(self) -> tuple:
        pass
