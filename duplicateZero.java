/*
https://leetcode.com/problems/duplicate-zeros/submissions/

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
*/


class Solution {
    public void duplicateZeros(int[] arr) {

        List<Integer> place = new ArrayList<Integer>();

        int q = arr.length;
        int i = 0;
        int found = 0;
        while(i<arr.length){
            //System.out.println("i::"+i+"::found::"+found);
           //System.out.println(place);
            if(found > 0 ){
                int temp = arr[i];
                arr[i] = 0;
                if(temp == 0){
                    place.add(temp);
                    found--;
                    i++;
                }
                else{
                    place.add(temp);
                    found--;
                    i++;
                }
            }
            else{
                if(place.size()>0){
                    int temp  = place.remove(0);
                    if(temp == 0 ){
                        found++;
                        int temp1 = arr[i];
                        arr[i] = 0;
                        if(temp1 == 0 ){
                        place.add(0);
                        i++;
                        }
                        else{
                            arr[i] = temp;
                            place.add(temp1);
                            i++;
                        }
                    }
                    else{
                        int temp1 = arr[i];
                        arr[i] = temp;
                        place.add(temp1);
                        i++;
                    }


                }
                else{
                    if(arr[i] == 0){
                        found++;
                        i++;
                    }
                    else{
                        i++;
                    }
            }
            }
        }

    }
}
