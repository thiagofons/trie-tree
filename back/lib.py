from trie import Trie


path = "src/trie.so"
trie = Trie(path)


def add(key: str, value: float):
    return trie.add_node(key, value)


def get_value(key: str):
    return trie.find_node(key)


def remove(key: str):
    return trie.remove_node(key)


def delete(key: str):
    return trie.flush_node(key)


print(add("ab", 10))  # tests
print(add("abc", 10))  # tests
print(get_value("ab"))
print(get_value("abc"))
print(remove("ab"))
print(get_value("ab"))
print(get_value("abc"))
