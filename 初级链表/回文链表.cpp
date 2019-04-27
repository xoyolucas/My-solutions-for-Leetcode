#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
bool isPalindrome(ListNode* head) {
    ListNode *fast=head,*slow=head,*newHead,*preSlow;
    if(head==NULL || head->next==NULL) return true;
    
    while(fast&&fast->next){
        fast=fast->next->next;
        preSlow=slow;
        slow=slow->next;
    }
    newHead=slow;
    preSlow->next=NULL;
    ListNode *x=NULL,*y=newHead,*z;
    while(y){
        z=y->next;
        y->next=x;
        x=y;
        y=z;
    }
    
    while(head){    
        if(x->val!=head->val) return false;
        head=head->next;
        x=x->next;
    }
    return true;
}

