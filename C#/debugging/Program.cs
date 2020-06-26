using System;
using System.Collections.Generic;
namespace debugging
{

    public class heapq{
        List<int> h = new List<int>();
        public int lastidx = -1;
        public void heappush(int num){
            h.Add(num);
            lastidx ++;
            int parent = lastidx / 2;
            int curidx = lastidx;
            while(num > h[parent]){
            // switch if parent is smaller
                h[curidx] = h[parent];
                h[parent] = num;
                curidx = parent;
                parent = parent / 2;
            }
        }
        public int heappop(){
            int to_return = h[0];
            h[0] = h[lastidx];
            // O(1) according to MSDN https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.removeat?view=netcore-3.1
            h.RemoveAt(lastidx);
            lastidx --;
            if(lastidx < 1){
                return to_return;
            }
            if(lastidx == 1){
                h.Sort((x, y) => -x.CompareTo(y));
                return to_return;
            }
            // if len(list) > 2
            shift_down(0);
            return to_return;
        }
        public void shift_down(int parent){
            int left_child = 2 * parent + 1;
            int right_child = 2 * parent + 2;
            int curlargest = h[parent];
            if(right_child <= lastidx){
                if(h[left_child] > curlargest && h[left_child] > h[right_child]){
                    h[parent] = h[left_child];
                    h[left_child] = curlargest;
                    shift_down(left_child);
                }
                else if(h[right_child] > curlargest && h[right_child] >= h[left_child]){
                    h[parent] = h[right_child];
                    h[right_child] = curlargest;
                    shift_down(right_child);
                }
            }
            else if(left_child == lastidx){
                if(h[left_child] > curlargest){
                    h[parent] = h[left_child];
                    h[left_child] = curlargest;
                }
            }
        }
}
    class Program
    {
        public int NumTrees(int n) {
            List<int> dp = new List<int>();
            dp.Add(1);
            dp.Add(1);
            for(int curend = 1;curend < n; curend++){
                int Cnum = 0;
                for(int i = 0; i <= curend; i++){
                    Cnum += dp[i] * dp[curend - i];
                }
                dp.Add(Cnum);
            }
            return dp[n];
        }
        static void Main(string[] args)
        {
            var a = new Program();
            int b = 3;
            var c = a.NumTrees(b);
            Console.Write(c);
            
        }
    }
}
