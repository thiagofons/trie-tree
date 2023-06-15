#include <stdbool.h>

bool trie_start();

bool trie_add(const char *key, float value);

bool trie_remove(const char *key);

float trie_find(const char *key);

bool trie_flush(const char *key);
