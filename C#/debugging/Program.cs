﻿using System;
using System.Collections;
using System.Collections.Generic;
namespace debugging
{
    class Program
    {

    public IList<int> LexicalOrder(int n) {
        var ls = new List<int>();
        for(int i = 1; i < n + 1; i ++){
            ls.Add(i);
        }
        Quicksort(ref ls, 0, n - 1);
        return ls;
    }
    public void Quicksort(ref List<int> ls, int l, int r){
        if(l < r){
            int base_num = ls[l];
            int next_start = l;
            int next_end = r;
            while(l < r){
                while(l < r && Comparerule(ls[r], base_num)){
                    r -= 1;
                } 
                ls[l] = ls[r];
                while(l < r && Comparerule(ls[l], base_num) == false){
                    l += 1;
                }
                ls[r] = ls[l];
            }
            ls[r] = base_num;
            Quicksort(ref ls, next_start, l - 1);
            Quicksort(ref ls, l + 1, next_end);
        }
    }
    // compare a and b, if a >= b return true else false
    public bool Comparerule(int a, int b){
        Stack<int> digits_a = new Stack<int>();
        Stack<int> digits_b = new Stack<int>();
        while(a > 0){
            digits_a.Push(a % 10);
            a = a / 10;
        }
        while(b > 0){
            digits_b.Push(b % 10);
            b = b / 10;
        }
        while(digits_a.Count > 0 && digits_b.Count > 0){
            int dig_a = digits_a.Pop();
            int dig_b = digits_b.Pop();
            if(dig_a > dig_b) return true;
            if(dig_b > dig_a) return false;
        }
        if(digits_a.Count > 0) return true;
        else return false;
    }
        static void Main(string[] args)
        {
            var a = new Program();
            int b = 13;
            var c = a.LexicalOrder(b);
            foreach(int i in c){
                Console.WriteLine(i);
            }
            // int x = 2;
            // int y = 12;
            // var c = a.Comparerule(x, y);
            // Console.Write(c);
            
        }
    }
}