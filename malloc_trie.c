#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

#define ALPHABET_SIZE 128

// A node being terminal means that it represents a key in the datastructure
// instead of just being there to support other keys.
// This struct actually takes 16 bytes because of alignment.
typedef struct TrieNode
{
    struct TrieNode **children;

    // This pesky little flag adds 8 bytes because of alignment
    bool is_terminal;
} TrieNode;

// Creates a empty non-terminal node, returns NULL on error
TrieNode *create_trie_node()
{
    TrieNode *node = (TrieNode *)malloc(sizeof(TrieNode));
    if (node == NULL)
        return NULL;

    // Node is empty and non-terminal initially
    node->children = NULL;
    node->is_terminal = false;
    return node;
}

void destroy_trie_node(TrieNode *node)
{
    if (node->children != NULL)
    {
        for (int i; i < ALPHABET_SIZE; i++)
        {
            if (node->children[i] != NULL)
            {
                destroy_trie_node(node->children[i]);
            }
        }
    }

    free(node);
}

// Adds a teminal node that represents key, and all intermediary if necessary.
// Returns NULL on error
TrieNode *add_node(TrieNode *base, const char *key)
{
    if (strlen(key) == 0)
    {
        // This node represents the key
        base->is_terminal = true;
        return base;
    }

    if (base->children == NULL)
    {
        // We need to allocate the children first (calloc to initialize all to NULL)
        base->children = (TrieNode **)calloc(ALPHABET_SIZE, sizeof(TrieNode *));
        if (base->children == NULL)
            return NULL;
    }

    const char prefix = key[0];

    if (base->children[prefix] == NULL)
    {
        // This path in the tree doesn't exist yet
        base->children[prefix] = create_trie_node();
    }

    const char *sufix = &key[1];
    return add_node(base->children[prefix], sufix);
}

// Makes the node that represents key a non-terminal
// If the node doesn't exist nothing is made
void remove_node(TrieNode *base, const char *key)
{
    if (strlen(key) == 0)
    {
        // This node represents the key
        base->is_terminal = false;
        return;
    }

    if (base->children == NULL)
        return;

    const char prefix = key[0];
    if (base->children[prefix] == NULL)
        return;

    const char *sufix = &key[1];
    remove_node(base->children[prefix], sufix);
}

TrieNode *find_node(TrieNode *base, const char *key)
{
    // This node represents this key
    if (strlen(key) == 0 && base->is_terminal)
        return base;

    // This node doesn't have children so there is no path
    if (base->children == NULL)
        return NULL;

    // The node doesn't have the needed child
    const char prefix = key[0];
    if (base->children[prefix] == NULL)
        return NULL;

    const char *sufix = &key[1];
    return find_node(base->children[prefix], sufix);
}

// True if key is represented by a node in base
bool is_in_trie(TrieNode *base, const char *key)
{
    return find_node(base, key) != NULL;
}

void test_add_and_search_key()
{
    TrieNode *trie = create_trie_node();
    add_node(trie, "asdf");
    assert(is_in_trie(trie, "asdf"));

    assert(!is_in_trie(trie, "a"));
    assert(!is_in_trie(trie, "as"));
    assert(!is_in_trie(trie, "asd"));
    assert(!is_in_trie(trie, "b"));
    assert(!is_in_trie(trie, "fdsa"));

    destroy_trie_node(trie);
    printf("Tested add and search\n");
}

void test_add_and_remove()
{
    TrieNode *trie = create_trie_node();
    add_node(trie, "asdf");

    assert(is_in_trie(trie, "asdf"));

    remove_node(trie, "asdf");

    assert(!is_in_trie(trie, "asdf"));

    destroy_trie_node(trie);
    printf("Tested add and remove\n");
}

void run_tests()
{
    test_add_and_search_key();
    test_add_and_remove();
}

int main()
{
    run_tests();

    return 0;
}