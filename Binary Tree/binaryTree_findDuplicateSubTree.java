/**
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    List<TreeNode> ans = new ArrayList<TreeNode>();
    Map<String,Integer> coq = new HashMap<String,Integer>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {

        if(root==null){
            return ans;
        }
        helper(root);
        return ans;

    }

    public String helper(TreeNode root1){

    if(root1 == null){
        return null;
    }

    String left = helper(root1.left);
    String right = helper(root1.right);

    String path = ""+root1.val+""+left+""+right;
    //System.out.println(path);

    if(coq.containsKey(path)){
        coq.put(path,(coq.get(path)+1));
        if(coq.get(path)==2){
            ans.add(root1);


        }

    }
    else{
        coq.put(path,1);
    }
    return path;
    }
}