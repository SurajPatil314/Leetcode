class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        int[] q1= new int[nums1.length];
        Set<Integer> set1 = new HashSet<Integer>();
        if(nums1.length>0 && nums2.length>0)
        {
            
            for(int i=0;i<nums1.length;i++)
            {
                for(int j=0;j<nums2.length;j++)
                {
                    if(nums1[i]==nums2[j])
                    {
                        set1.add(nums2[j]);
                    }
                }
            }
            q1 = set1.stream()
							.mapToInt(Integer::intValue)
							.toArray();
        
        }
        int [] answer = new int[q1.length];
        int i = 0;
        for(int oneNum : q1) {
            answer[i++] = oneNum;
        }
      
        return answer;
    }
}