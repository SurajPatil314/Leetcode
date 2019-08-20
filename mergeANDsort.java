class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        List<Integer> list = new ArrayList<>();
        int[] ans = new int[m+n];
        for(int i=0;i<m;i++)
        {
            list.add(nums1[i]);
        }
        for(int i=0;i<n;i++)
        {
            list.add(nums2[i]);
        }
        list.sort(Comparator.naturalOrder()); 
        for(int i=0;i<ans.length;i++)
        {
            ans[i]= list.get(i);
            System.out.println("ans::"+ans[i]);
        }
        nums1=ans;
        
        
    }
}