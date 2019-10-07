/**
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    public boolean flag=true;
    public boolean isSymmetric(TreeNode root) {

        TreeNode rside;
        TreeNode lside;

        if(root==null)
        {
            return true;
        }
        rside = root.right;

        lside= root.left;

        if(rside==null && lside==null)
        {
            return true;
        }

        inroder(rside,lside);

        return flag;

    }

    public void inroder(TreeNode rside, TreeNode lside)
    {
        if((rside!=null && lside==null) || (rside==null && lside!=null))
        {
            flag=false;
            return;
        }

        if(rside==null && lside==null)
        {
            return;
        }

        inroder(rside.right, lside.left);

        if(rside.val!=lside.val)
        {
            flag=false;
            return;
        }
        else
        {
            System.out.println(rside.val);
        }

        inroder(rside.left, lside.right);
    }
}