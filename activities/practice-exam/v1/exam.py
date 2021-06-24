#!/usr/bin/env python3

def q1(floatstr):
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the
    argument as elements in the list.
    '''
    return [float(x) for x in floatstr.split(",")]


def q2(*args):
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    a=0
    for x in args:
        a+=x
    return a/len(args)
    #pass

def q3(lst,n):
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new
    list containing the last n entries in lst.
    '''
    return lst[len(lst)-n:len(lst)]

def q4(strng):
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of
    each character in the string in the order found in the input string.
    '''
    return [ord(x) for x in strng]

def q5(strng):
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    return tuple(strng.split(" "))

def q6():
    '''
    TLO: 112-SCRPY006, LSA 4
    Given an input string similar to the below, craft a regular expression
    pattern to match and extract the date, time, and temperature in groups
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''
    #import re

    #a=input()
    return "Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F"


def q7(filename):
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line
    in the file excluding the line terminator.
    '''
    a=open(filename,"r")
    b=len(a.readline())
    a.close()
    return b-1
    #pass

def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in
    the list. If "stop" is not found in the list, write the entire list to
    the file on separate lines.
    '''
    a=open(filename,"w")
    for x in lst:
        if(x.lower()=="stop"):
            return lst
        a.write(x+"\n")

    return lst

def q9(miltime):
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    time=int(miltime)
    if(time>=300 and time<=1159):
        return "Good Morning"
    elif(time>=1200 and time<=1559):
        return "Good Afternoon"
    elif(time>=1600 and time<=2059):
        return "Good Evening"
    else:
        return "Good Night"
    pass

def q10(numlist):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    for x in numlist:
        if x<0:
            return False
    return True
