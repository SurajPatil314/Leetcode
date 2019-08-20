//Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.	
    public int removeDuplicates(int[] nums) {
	    	List<Integer> unique = new ArrayList<Integer>();
	       for(int i =0; i<nums.length;i++)
	       {
	    	   for(int j=0; j<nums.length;i++)
	    	   {
	    		   if(nums[i]!=nums[j])
	    		   {
	    			   if(unique.contains(nums[j]))
	    			   {
	    				   
	    			   }
	    			   else
	    			   {
	    				   unique.add(nums[i]);  
	    			   }
	    			   
	    		   }
	    	   }
	       }
		return unique.size();
	    
	}