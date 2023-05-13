/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdbool.h>
#include <stdlib.h>


struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL) return NULL;
    struct ListNode* p = NULL;
    struct ListNode* c = head;
    struct ListNode* n = head->next;
    while (c != NULL) {
        c->next = p;
        p = c;
        c = n;
        if (n != NULL) n = n->next;
    }
    return p;
}

bool isPalindrome(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    slow->next = reverseList(slow->next);
    struct ListNode* start = head;
    struct ListNode* mid = slow->next;
    while (mid != NULL) {
        if (mid->val != start->val) return false;
        start = start->next;
        mid = mid->next;
    }
    slow->next = reverseList(slow->next);
    return true;
}

