/**
https://leetcode.com/problems/deepest-leaves-sum/submissions/
Given a binary tree, return the sum of values of its deepest leaves.


 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = 0;
    public int deepestLeavesSum(TreeNode root) {

        if(root==null)return 0;

        Queue<TreeNode> qw1 = new LinkedList<>();
        Queue<TreeNode> qw2 = new LinkedList<>();
        qw1.add(root);

        while(qw1.size()>0 || qw2.size()>0){
            ans = 0;
            while(qw1.size()>0){
                TreeNode temp = qw1.remove();
                ans = ans+ temp.val;
                if(temp.left!=null){qw2.add(temp.left);}
                if(temp.right!=null){qw2.add(temp.right);}
            }

            if(qw2.size() == 0){
                return ans;
            }
            else{
                ans = 0;
                qw1.clear();
            }
            while(qw2.size()>0){
                TreeNode temp = qw2.remove();
                ans = ans+ temp.val;
                if(temp.left!=null){qw1.add(temp.left);}
                if(temp.right!=null){qw1.add(temp.right);}

            }
            if(qw1.size() == 0){
                return ans;
            }
            else{
                ans = 0;
                qw2.clear();
            }

        }

        return ans;

    }

}