/*
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
*/

class NumArray {

    int[] arr;
    public NumArray(int[] nums) {
        this.arr = new int[nums.length];
        for(int i=0;i<=nums.length-1;i++){
            this.arr[i]= nums[i];
            System.out.println(this.arr[i]);
        }

    }

    public int sumRange(int i, int j) {
        int sum = 0;
        if(i<0 || j>this.arr.length-1){
            System.out.println(this.arr.length);
            return sum;
        }
        else{

            for(int k=0;k<this.arr.length;k++){
                if(k>=i && k<=j){
                    sum=sum+this.arr[k];
                }
                if(k>j){
                    break;
                }

            }

        }
        return sum;

    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */