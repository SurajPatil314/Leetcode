class Solution {
    public int fib(int N) {
        if(N==0){return 0;}
        if(N==1){return 1;}
        int[] qw = new int[N+1];
        qw[0] = 0;
        qw[1] = 1;

        for(int i=2; i<=N; i++){
            qw[i] = qw[i-1] + qw[i-2];
        }

        return qw[N];
    }
}