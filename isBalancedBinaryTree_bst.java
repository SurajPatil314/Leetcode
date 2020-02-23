/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {



        if(root == null){
            return true;
        }

        int lhight = ht(root.left);
        int rhight =ht(root.right);
        return((Math.abs(lhight-rhight)<=1) && isBalanced(root.left) && isBalanced(root.right));
    }

    public int ht(TreeNode nod){

        if(nod == null){
            return 0;
        }
        else{
            int lsub = ht(nod.left);
            int rsub = ht(nod.right);
            return(1 + Math.max(lsub,rsub)) ;
        }

    }
}