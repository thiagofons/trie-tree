// A node being terminal means that it represents a key in the datastructure
// instead of just being there to support other keys.
// This struct actually takes 16 bytes because of alignment.
typedef struct TrieNode
{
    struct TrieNode **children;

    // This pesky little flag adds 8 bytes because of alignment
    bool is_terminal;
} TrieNode;

TrieNode *create_trie_node();

void destroy_trie_node(TrieNode *node);

TrieNode *add_node(TrieNode *base, const char *key);

void remove_node(TrieNode *base, const char *key);

TrieNode *find_node(TrieNode *base, const char *key);

bool is_in_trie(TrieNode *base, const char *key);