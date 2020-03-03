/**
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth
 d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes
 with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree
  of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If
   depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the
   whole original tree, and the original tree is the new root's left subtree.
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode addOneRow(TreeNode root, int v, int d) {

        if(root==null){
            TreeNode nroot = new TreeNode(v);
            return nroot;
        }

        if(d==1){
            TreeNode n = new TreeNode(v);
            n.left = root;
            return n;
        }
        TreeNode tmp = root;
        addrow(tmp,v,2,d);

        return root;


    }

    public void addrow(TreeNode rtc, int v, int level, int d){

        if(rtc == null){
            return;
        }
        //System.out.println("at::"+rtc.val+"::level is::"+level);
        if(d == level){
            TreeNode nrootl = new TreeNode(v);
            TreeNode nrootr = new TreeNode(v);
            TreeNode lq = rtc.left;
            TreeNode rq = rtc.right;
            rtc.left = nrootl;
            rtc.right = nrootr;
            nrootl.left = lq;
            nrootr.right = rq;

        }
        else{
            addrow(rtc.left,v,level+1,d);
            addrow(rtc.right,v,level+1,d);
        }

    }
}