/**

https://leetcode.com/problems/count-good-nodes-in-binary-tree/


Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



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
    public int ans = 0;

    public int goodNodes(TreeNode root) {

        if(root == null){return 0;}
        if(root.left == null && root.right == null){return 1;}

        rec(root, Integer.MIN_VALUE);

        return ans;


    }

    public void rec(TreeNode root1, int maxi){
        //System.out.println(maxi);
        if(root1 == null){
            return;
        }
        if(root1.left == null && root1.right == null){
            if(root1.val>=maxi){
            ans++;
        }
           return;
        }


        if(root1.val>=maxi){
            ans++;
            maxi = root1.val;
        }



        rec(root1.left,maxi);
        rec(root1.right,maxi);

    }


}