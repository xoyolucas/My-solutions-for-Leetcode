#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *node1=head,*node2=head;
    for(size_t i = 0; i < n; i++){
        node2=node2->next;
    }
    if(node2==NULL)
        return head->next;
    while(node2->next!=NULL){
        node1=node1->next;
        node2=node2->next;
    }
    node1->next=node1->next->next;
    return head;
}

