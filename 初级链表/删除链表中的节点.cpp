#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
void deleteNode(ListNode* node) {
    ListNode *tmp=node;
    while(tmp->next!=NULL){
        if(tmp->next->next!=NULL){
            tmp->val=tmp->next->val;
            tmp=tmp->next;
        }
        else{
            tmp->val=tmp->next->val;
            tmp->next=NULL;
        }
    }
}

