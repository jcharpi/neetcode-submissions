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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dummy = ListNode(-1, head);
        int n = right - left;

        // Get pre_swap
        ListNode* node_before_left = &dummy;
        for(int i = 0; i < left - 1; i++) {
            node_before_left = node_before_left->next;
        }

        ListNode* tail = node_before_left->next;
        ListNode* curr = tail;
        ListNode* prev = nullptr;
        while (n > -1) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
            n--;
        }

        tail->next = curr;
        node_before_left->next = prev;

        return dummy.next;
    }
};