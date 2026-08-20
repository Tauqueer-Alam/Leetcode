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
    ListNode* sortList(ListNode* head) {
        vector <int> arr;
        ListNode* current=head;
        while(current!=NULL){
            arr.push_back(current->val);
            current=current->next;
        }

        sort(arr.begin(),arr.end());
        if (arr.empty()){
            return NULL;
        }
        ListNode* new_head=new ListNode(arr[0]);
        current=new_head;

        for(int i=1;i<arr.size();i++){
            current->next=new ListNode(arr[i]);
            current=current->next;

        }

        return new_head;
        
    }
};