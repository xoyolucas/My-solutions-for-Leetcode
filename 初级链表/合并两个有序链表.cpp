#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if(l1==NULL) return l2;
    if(l2==NULL) return l1;
    ListNode* begin=NULL,*next=NULL;
    if(l1->val<=l2->val){
        begin=l1;
        l1=l1->next;
    }
    else{
        begin=l2;
        l2=l2->next;
    }
    next=begin;
    while(l1!=NULL&&l2!=NULL){
        if(l1->val<=l2->val){
            next->next=l1;
            next=next->next;
            l1=l1->next;
        }
        else{
            next->next=l2;
            next=next->next;
            l2=l2->next;
        }
    }
    while(l1!=NULL){
        next->next=l1;
        next=next->next;
        l1=l1->next;
    }
    while(l2!=NULL){
        next->next=l2;
        next=next->next;
        l2=l2->next;
    }
    return begin;
}

