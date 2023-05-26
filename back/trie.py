from ctypes import CDLL, c_bool, c_char_p, c_float


class Trie:
    def __init__(self, path: str) -> None:
        self.lib = CDLL(path)
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
        return self.add_func(key.encode(), value)

    def find_node(self, key: str):
        return self.find_func(key.encode())

    def remove_node(self, key: str):
        return self.remove_func(key.encode())

    def flush_node(self, key: str):
        return self.delete_func(key.encode())
