//Given an array, rotate the array to the right by k steps, where k is non-negative.
class Solution {
  public void rotate(int[] nums, int k) {
    if(k!=0)
    {
    List<Integer> sol = new ArrayList<Integer>();
     List<Integer> sol1 = new ArrayList<Integer>();
       List<Integer> sol2 = new ArrayList<Integer>();
     int counter=0;
    for(int i=0; i<k+1 ;i++)
    {
        sol1.add(nums[i]);
        counter++;
    }
      System.out.println("counter"+counter);
      System.out.println("sol1"+sol1);
    for(int i=counter; i<nums.length ;i++)
    {
        sol.add(nums[i]);
    }
       System.out.println("sol"+sol);
    sol2.addAll(sol);
      sol2.addAll(sol1);
      System.out.println("sol2"+sol2);
    }
    
}
}