/*
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
*/
class Twitter {
   
     Map<Integer, ArrayList<Integer>> followermap = new HashMap<Integer, ArrayList<Integer>>();
     Map<Integer,ArrayList<tweet>> tweetmap = new HashMap<Integer, ArrayList<tweet>>();
    public static int tweetnumber=0;
    private static class tweet{
        
        int tweetid;
        String tweets;
        int userid;
        int tweetn;
        
        public tweet(int userid,int tweetid,int tweetnumberk)
        {
            this.userid=userid;
            this.tweetid=tweetid;
            this.tweetn=tweetnumberk;
        }
        
    
    }
    /** Initialize your data structure here. */
    public Twitter() {
        
        
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        
        tweet ntweet=new tweet(userId,tweetId,tweetnumber++);
        
        if (tweetmap.get(userId) == null) {
         tweetmap.put(userId, new ArrayList<tweet>());
        }
        tweetmap.get(userId).add(ntweet);
        
    }
    
   
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        
        List<Integer> anst= new ArrayList<Integer>();
        Map<Integer, Integer> ans1 = new HashMap<Integer, Integer>();
        if (tweetmap.containsKey(userId))
        {
            ArrayList<tweet> anstw= new ArrayList<tweet>();
            anstw= tweetmap.get(userId);
            
            for(tweet sample: anstw)
            {
                System.out.println("userid :" + userId + " tweet id: " + sample.tweetid);
                ans1.put(sample.tweetn, sample.tweetid);
            }
            Map<Integer, Integer> reverseSortedMap = new TreeMap<Integer, Integer>(Collections.reverseOrder());
 
            reverseSortedMap.putAll(ans1);
            for (Map.Entry<Integer, Integer> entry : reverseSortedMap.entrySet())  
            {
                            
                 anst.add(entry.getValue());
            }
            if(anst.size()>0)
                return anst;
            
                 
        }        
        else
        {
            return anst;
        }
        return anst;
    }
    
     //Map<Integer, List<Integer>> followermap = new HashMap<Integer, List<Integer>>();
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if (followermap.get(followerId) == null) {
         followermap.put(followerId, new ArrayList<Integer>());
        }
        followermap.get(followerId).add(followeeId);
        
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
         if (followermap.containsKey(followerId))
        {
            
            ArrayList<Integer> fol= new ArrayList<Integer>();
            fol= followermap.get(followerId);
            fol.remove(Integer.valueOf(followeeId));
             followermap.put(followerId,fol);
           
         }
        
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */