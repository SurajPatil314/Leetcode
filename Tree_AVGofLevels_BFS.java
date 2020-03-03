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
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> ans = new ArrayList<>();
        Stack<TreeNode> tmp = new Stack<TreeNode>();

        if(root==null){
            return ans;
        }

        tmp.push(root);
        while(!tmp.empty()){
            Double ans1 = 0.00;
            int siz = tmp.size();
            Stack<TreeNode> tmp1 = new Stack<TreeNode>();
            while(!tmp.empty()){
                TreeNode e = tmp.pop();
                tmp1.push(e);
                ans1 = ans1 + e.val;
            }
            ans1 = ans1/siz;
            ans.add(ans1);
            while(!tmp1.empty()){
                TreeNode e = tmp1.pop();
                if(e.left!=null){
                    tmp.push(e.left);
                }
                if(e.right!=null){
                    tmp.push(e.right);
                }
            }
        }
        return ans;
    }
}