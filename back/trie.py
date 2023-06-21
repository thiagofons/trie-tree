from ctypes import CDLL, c_bool, c_char_p, c_float
from os.path import abspath
import json


class JsonCall:
    def __init__(self, type: str, sender: str, reciever: str) -> None:
        self.type = type
        self.sender = sender
        self.reciever = reciever

    def __dict__(self):
        return {"type": self.type, "sender": self.sender, "reciever": self.reciever}

    def to_json(self):
        return json.dumps(self.__dict__())


class Report(JsonCall):
    def __init__(self, sender: str, reciever: str) -> None:
        super().__init__("report", sender, reciever)


class Transaction(JsonCall):
    @staticmethod
    def from_key(key: str, value: float):
        try:
            f, t = key.split("@")
            return Transaction(f, t, value)
        except:
            print("Invalid Transaction.")

    def __init__(self, sender: str, reciever: str, value: float) -> None:
        super().__init__("transaction", sender, reciever)
        self.value = f"{value}"

    def __dict__(self):
        return {
            "type": self.type,
            "sender": self.sender,
            "reciever": self.reciever,
            "value": self.value,
        }


class Trie:
    def __init__(self, path: str) -> None:
        self.lib = CDLL(abspath(path))

        self.transactions: list[Transaction] = []

        self.lib.trie_start()
        self.adjust_functions()

    def adjust_functions(self):
        self.add_func = self.lib.trie_add
        self.add_func.argtypes = [c_char_p, c_float]
        self.add_func.restype = c_bool

        self.find_func = self.lib.trie_find
        self.find_func.argtypes = [c_char_p]
        self.find_func.restype = c_float

        self.remove_func = self.lib.trie_remove
        self.remove_func.argtypes = [c_char_p]
        self.remove_func.restype = c_bool

        self.delete_func = self.lib.trie_flush
        self.delete_func.argtypes = [c_char_p]
        self.delete_func.restype = c_bool

    def add_node(self, key: str, value: float):
        sucess = self.add_func(key.encode(), value)
        if sucess:
            self.transactions.append(Transaction.from_key(key, value))
        return sucess

    def find_node(self, key: str):
        return self.find_func(key.encode())

    def remove_node(self, key: str):
        return self.remove_func(key.encode())

    def flush_node(self, key: str):
        return self.delete_func(key.encode())
