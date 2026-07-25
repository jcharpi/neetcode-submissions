class ListNode {
public:
    int val = 0;
    ListNode* next = nullptr;

    ListNode() = default;
    ListNode(int val) : val(val) {}
    ListNode(int val, ListNode* next) : val(val), next(next) {}
};

class LinkedList {
private:
    ListNode* head;

public:
    LinkedList() : head(new ListNode()) {}

    int get(int index) {
        ListNode* curr = head->next;
        for (int i = 0; i < index; i++) {
            if (!curr) return -1;
            curr = curr->next;
        }
        return curr ? curr->val : -1;
    }

    void insertHead(int val) {
        head->next = new ListNode(val, head->next);
    }
    
    void insertTail(int val) {
        ListNode* curr = head;
        while (curr->next) {
            curr = curr->next;
        }
        curr->next = new ListNode(val);
    }

    bool remove(int index) {
        ListNode* prev = head;
        for (int i = 0; i < index; i++) {
            if (!prev->next) return false;
            prev = prev->next;
        }
        if (!prev->next) return false;
        ListNode* target = prev->next;
        prev->next = target->next;
        delete target;
        return true;
    }

    vector<int> getValues() {
        ListNode* curr = head->next;
        vector<int> out;
        while (curr) {
            out.push_back(curr->val);
            curr = curr->next;
        }
        return out;
    }
};
