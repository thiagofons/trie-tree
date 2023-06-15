from trie import Trie
from os.path import abspath

path = abspath("src/trie.so")
trie = Trie(path)


def add(key: str, value: float):
    return trie.add_node(key, value)


def get_value(key: str):
    return trie.find_node(key)


def remove(key: str):
    return trie.remove_node(key)


def delete(key: str):
    return trie.flush_node(key)


print(add("a@b", 10))  # tests
print(get_value("a@b"))
print(trie.get_json_transaction(0))
