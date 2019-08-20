class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        	HashMap<Integer, String> count = new HashMap<>();
        int q=0;
       // Set<String> set1 = new HashSet<String>();
         List<String> list1 = new ArrayList<String>();
            String[] words=paragraph.split("\\W+");
       
        for(int i=0;i<words.length;i++)
        {
            words[i]= words[i].toLowerCase();
        }
        for(int i=0;i<banned.length;i++)
        {
            banned[i]= banned[i].toLowerCase();
        }
        for(int i=0;i<words.length;i++)
        {
            q=1;
            for(int j=0; j<banned.length;j++)
            {
                
                if(words[i].equals(banned[j]))
                {
                    q=0;
                    System.out.println("in else for word::"+words[i]);
                    break;
                }
            }
            if(q==1)
            {
                list1.add(words[i]);
                System.out.println("word::"+words[i]);
            }
          
        }
          Map<String, Integer> seussCount = new HashMap<String,Integer>();
        long number1 = list1
            .stream()
            .filter(p -> p.equals(list1.get(0)))
            .count();
        String qe=list1.get(0);
    for(String t: list1) {
       long number = list1
            .stream()
            .filter(p -> p.equals(t))
            .count();
        if(number1<number)
        {
            number1=number;
            qe=t;
            
        }
        System.out.println("word count ::"+t+"::is::"+number);
        
        }
          
        return qe;
    }
}