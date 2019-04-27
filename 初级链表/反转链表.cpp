#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
ListNode* reverseList(ListNode* head) {
    if(head==NULL)
        return NULL;
    ListNode* front=NULL;
    ListNode *p=head, *q=head->next;
    while(q!=NULL){
        p->next=front;
        front=p;
        p=q;
        q=q->next;
    }
    p->next=front;
    return p;
}

