/*A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
*/
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        
        List<Integer> ans =new ArrayList<Integer>();
        int j=0;
        
        for(int i=left; i<=right; i++)
        {
            if(i>0 && i<10)
            {
                ans.add(i);
            }
            else
            {
                String anum= String.valueOf(i);
                char[] q= anum.toCharArray();
                if(anum.contains("0"))
                {
                    System.out.println("in first if"+i);
                    continue;
                }
                else
                {
                    System.out.println("in first else"+i);
                    j=0;
                    for(char w:q)
                    {
                        int a=Character.getNumericValue(w) ;
                        System.out.println("value of a"+a);
                        if(i%a!=0)
                        {
                            System.out.println("in second if"+i);
                            j=1;
                            break;
                        }
                    }
                    if(j==0)
                    {
                        System.out.println("in third if"+i);
                        ans.add(i);
                    }
                }
            }
        }
        
        return ans;
        
    }
}