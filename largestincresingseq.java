class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int k=0;
        int m=1;
       int count=1;
        if(nums.length>0)
        {
            for(int j=0;j<nums.length-1;j++)
            {
                count=1;
                for(int kt=j;kt<nums.length-1;kt++)
                {
                    if(nums[kt]<nums[kt+1])
                    {
                        count++;
                        System.out.println("count::"+count+"::nums[kt]::"+nums[kt]);
                    }
                    else
                    {
                        break;
                    }
                }
                 System.out.println("next element");
                if(m<count)
                {
                    m=count;
                }
            }
        return m;
        }
        return 0;
    }
}