#!/usr/bin/env python3


def guess_number(n):
    while True:
        a=int(input("Guess a number"))
        if(a<n):
            print("Too Low!")
        elif(a>n):
            print("Too High!")
        else:
            print("WIN")
            return
guess_number(23)
