/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<HeapEntry> minimum_elements;
        for (int list_index = 0; list_index < ssize(lists); list_index++) {
            ListNode* head = lists[list_index];
            if (head) {
                minimum_elements.push_back({head->val, list_index, head->next});
            }
        }

        priority_queue<HeapEntry, vector<HeapEntry>, greater<HeapEntry>> min_heap(minimum_elements.begin(), minimum_elements.end());

        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (!min_heap.empty()) {
            HeapEntry min_entry = min_heap.top();
            min_heap.pop();
            tail->next = new ListNode(min_entry.val);
            tail = tail->next;
            if (min_entry.next_node) {
                min_heap.push({min_entry.next_node->val, min_entry.list_index, min_entry.next_node->next});
            }
        }
        return dummy.next;
    }

private:
    struct HeapEntry {
        int val;
        int list_index;
        ListNode* next_node;

        auto operator<=>(const HeapEntry&) const = default;
    };
};
