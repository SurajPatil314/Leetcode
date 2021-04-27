/**

https://leetcode.com/problems/binary-tree-pruning/

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)


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
    public TreeNode pruneTree(TreeNode root) {

        if(root==null){return null;}

        int retleft = 0;
        int retright = 0;
        if(root.left !=null){
            retleft = rec(root.left);
            if(root.left.val==1){
                       retleft = 1;
            }
        }
        if(root.right !=null){
            retright = rec(root.right);
            if(root.right.val==1){
                       retright = 1;
            }
        }

        if(retleft == 0 && retright == 0 ){
            return null;
        }
        else{
            if(retleft == 0){root.left = null;}
            if(retright == 0){root.right = null;}

            return root;
        }



    }

    public int rec(TreeNode root1){

        if(root1.left == null && root1.right == null){

            if(root1.val ==  0){
                return 0;
            }
            else{
                return 1;
            }
        }

        else{

            int retleft = 0;
            int retright = 0;
            if(root1.left !=null){
                retleft = rec(root1.left);
                if(root1.left.val==1){
                       retleft = 1;
                }
            }
            if(root1.right !=null){
                retright = rec(root1.right);
                if(root1.right.val==1){
                       retright = 1;
                }
            }


            if(retleft == 0 && retright == 0){

                root1.left = null;
                root1.right = null;
                return 0;
            }
            else{

                if(retleft == 0){root1.left = null;}
                if(retright == 0){root1.right = null;}
                return 1;
            }

        }


    }
}