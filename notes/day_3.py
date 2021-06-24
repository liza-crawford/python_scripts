
Runestone Ch 6 Questions:

Join example: (Glue elements of a string together)

Print the list wds and remove the commas
wds = ["red", "blue", "green"]

print("".join(wds))

Len example: When using a string, it returns the number of characters.

fruit = "Banana"
print(len(fruit))

When using a list, it returns the number of items in the list.

alist =  ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))


Assign the number of elements in lst to the variable output.

lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]

output = len(lst)

Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

#extract last 3
last = sports[-3:]

OR

last = sports[len(sports)-3:]




Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy.

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + ", " + qy

OR




Write code to determine how many 9’s are in the list nums and assign that value to the variable how_many. Do not use a for loop to do this.

nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

how_many = nums.count(9)

OR





Assign the number of elements in lst to the variable num_lst.

lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

num_lst = len(lst)




CH 7  CHAPTER ASSESSMENT

https://runestone.academy/runestone/books/published/fopp/Iteration/week2a2.html

Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"

for state in my_str:
    print(state)




Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for stuff in several_things:
    print(stuff)

for stuff in several_things:
    print(type(stuff))




Write code that uses iteration to print out the length of each element of the list stored in str_list.


str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.

for greeting in str_list:
    print(len(greeting))




week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

sum_of_temps = 0

temps = week_temps_f.split(',')

for num in temps:
    sum_of_temps = sum_of_temps + float(num)

avg_temp = sum_of_temps/ len(temps)





CH 9 RUNESTONE ASSESSMENT


Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

above = 0

excel = scores.split(' ')

for num in excel:
    integer = int(num)
    if integer >= 90:
        above = above + 1

    #change to an int
    # determine which values are >= 90 (use an if statement)
    #if True increment the accum + 1

a_scores = above

Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

#change org to a list
#compare the lists using a for loop
#capture the comparison and compile into an accumulator

words = org.split()

comp = ""

for word in words:
    print(word)
    if word not in stopwords:
        print(True)
        comp = comp + word[0].upper()

acro = comp
Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
