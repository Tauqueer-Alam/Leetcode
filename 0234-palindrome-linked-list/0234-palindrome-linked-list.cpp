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
    bool isPalindrome(ListNode* head) {
        vector <int> arr1;

        ListNode* current= head;
        while(current!=NULL){
            arr1.push_back(current->val);
            current=current->next;
        }    

        vector <int> arr2=arr1;
        reverse(arr2.begin(),arr2.end());

        if(arr1==arr2){
            return true;
        }

        else{
            return false;
        }

    }
};