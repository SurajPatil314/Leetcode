/

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.


**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


class Solution {
    TreeNode ans;
    public TreeNode searchBST(TreeNode root, int val) {
        
        if(root==null)
        {
            return null;
        }
        
        if(root.val==val)
        {
            return root;
        }
        
        
        inorder(root,val);
        return ans;
        
    }
    
    public void inorder(TreeNode root, int val)
    {
        if(root==null)
        {
            return;
        }
        inorder(root.left,val);
        System.out.println(root.val);
        if(root.val==val)
        {
            ans= root;
        }
        inorder(root.right,val);
    }
}