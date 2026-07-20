class LRUNode {
public:
    int key;
    int value;
    LRUNode* prev;
    LRUNode* next;

    LRUNode(int key, int value, LRUNode* prev = nullptr, LRUNode* next = nullptr) : 
        key(key), value(value), prev(prev), next(next) {}
};

class LRUCache {
public:
    LRUNode* head;
    LRUNode* tail;
    int capacity;
    unordered_map<int, LRUNode*> cache;

    LRUCache(int capacity) {
        head = new LRUNode(0, 0);
        tail = new LRUNode(0, 0);

        head->next = tail;
        tail->prev = head;

        this->capacity = capacity;
    }

    void remove(LRUNode* node) {
        node->next->prev = node->prev;
        node->prev->next = node->next;
    }

    void insert_at_end(LRUNode* node) {
        node->prev = tail->prev;
        node->next = tail;
        tail->prev->next = node;
        tail->prev = node;
    }

    int update_node(int key) {
        LRUNode* node = cache[key];
        remove(node);
        insert_at_end(node);
        return node->value;
    }
    
    int get(int key) {
        if (cache.contains(key)) return update_node(key);
        else return -1;
    }
    
    void put(int key, int value) {
        if (cache.contains(key)) {
            LRUNode* node = cache[key];
            node->value = value;
            update_node(key);
            return;
        }
        
        if ((int)capacity == cache.size()) {
            LRUNode* lru = head->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }

        LRUNode* node = new LRUNode(key, value);
        insert_at_end(node);
        cache[key] = node;
    }
};
