nums = [0,1,2,4,5] 
def missing_num(nums):
    for i in range(len(nums)):
        if i != nums[i]:
            return i

def missing_number(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number  


def missing_number(nums): 
    n = len(nums) 
    total = n*(n+1)/2
    sum_of_nums = sum(nums) 
    return total - sum_of_nums

sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""

def find_bigrams(sentence):

    sentenceList = sentence.strip().lower().split()
    bigramList = list()
    for i in range(len(sentenceList)-1):
        bigram = (sentenceList[i],sentenceList[i+1])
        bigramList.append(bigram)

    return bigramList


def merge_list(list1,list2):

    list1Idx = 0
    list2Idx = 0
    finalList = list()
    while list1Idx < len(list1) and list2Idx < len(list2) :

        if list1[list1Idx] < list2[list2Idx]:
            finalList.append(list1[list1Idx])
            list1Idx += 1

        else:
            finalList.append(list2[list2Idx])
            list2Idx += 1

    while list1Idx < len(list1):
        finalList.append(list1[list1Idx])
        list1Idx += 1

    while list2Idx < len(list2):
        finalList.append(list2[list2Idx])
        list2Idx += 1

    return finalList

list1 = [1,2,5]
list2 = [2,4,6]
    

str = 'carerac'
sss= "saippuakivikauppias"
str1 = "deed"
def perm_palindrome(str):
    from collections import Counter
    stringCounter = Counter(str)
    num_odds = 0

    for i in stringCounter:
        if stringCounter[i]%2 != 0:
            num_odds += 1

    return num_odds <= 1

nums = [1, 7, 3, 5, 6]
nums = [1,3,5]
def equivalent_index(nums):

    for i in range(len(nums)):

        if sum(nums[:i+1]) == sum(nums[i+1:]):
            return i

    return -1 

def equivalent_index(nums):
    total = sum(nums)
    leftsum = 0
    for index, x in enumerate(nums):
        # the formula for computing the right side
        rightsum = total - leftsum - x
        leftsum += x
        if leftsum == rightsum:
            return index
    return -1


import collections

def plan_trip(flights):
    trip_graph = collections.defaultdict(lambda: None)
    source_cities = set()
    destination_cities = set()
    for source, destination in flights:
        trip_graph[source] = destination
        source_cities.add(source)
        destination_cities.add(destination)
   
    start_city = (source_cities - destination_cities).pop()
    traversal = []
    start, end = start_city, trip_graph[start_city]
    while end is not None:
        traversal.append([start, end])
        start, end = end, trip_graph[end]
       
    return traversal


flights = [
    ['Chennai', 'Bangalore'], 
    ['Bombay', 'Delhi'], 
    ['Goa', 'Chennai'], 
    ['Delhi', 'Goa'], 
    ['Bangalore', 'Beijing']
]
output = [
    ['Bombay', 'Delhi'], 
    ['Delhi', 'Goa'], 
    ['Goa', 'Chennai'], 
    ['Chennai', 'Bangalore'], 
    ['Bangalore', 'Beijing'],
]


import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
 

#generate 1000 simulations of 100 trials
k= []
for i in range(1000):
  generated=random.choices([0,1],[0.5,0.5],k=100) 
  k.append(np.sum(generated))

plt.hist(k)
random.choice(k)


def normality_test_napkin(sample_list):
    list_avg = sum(sample_list)/len(sample_list)
    list_sigma = (sum((x-list_avg)**2 for x in sample_list) / len(sample_list)) ** .5
    
    perc_one_sigma = sum([1 if (x < list_sigma + list_avg) and (x > list_avg - list_sigma) else 0 for x in sample_list]) / len(sample_list)
    perc_two_sigma = sum([1 if (x < (2*list_sigma) + list_avg) and (x > list_avg - (2*list_sigma)) else 0 for x in sample_list]) / len(sample_list)
    perc_three_sigma = sum([1 if (x < (3*list_sigma) + list_avg) and (x > list_avg - (3*list_sigma)) else 0 for x in sample_list]) / len(sample_list)
    print(perc_one_sigma,perc_two_sigma, perc_three_sigma)
    evidence = 0
    if perc_one_sigma <= .72 and perc_one_sigma >= .64:
        evidence += 1
    if perc_two_sigma <= .96 and perc_two_sigma >= .94:
        evidence += 1
    if perc_three_sigma >= .98:
        evidence += 1
    
    if evidence == 3:
        return('There is strong evidence that this distribution is normal')
    elif evidence == 2:
        return('There is evidence that this distribution is normal')
    elif evidence == 1:
        return('There is little evidence that this distribution is normal')
    else:
        return('There is no evidence that this distribution is normal')


new_point = [0,1,0,1]

col =['Var1','Var2','Var3','Var4'] 

dp = [[1.0 ,1.0,   1.0,   0.0],   
[0.0,   0.0,   0.0,   0.0 ],    
[1.0,   0.0,   1.0,   0.0 ],      
[0.0,   1.0,   1.0,   1.0 ],     
[1.0 ,  0.0,   1.0,   0.0 ],
 [0,1,0,1]]   

import numpy as np
import pandas as pd
import itertools

df  =pd.DataFrame(dp,columns=col)

features = df.columns

all_permutations = itertools.permutations(features)
for i in all_permutations:
    print(i)
X =df
for col, i in zip(features,new_point):
    print(col,i)

X[X['Var1']==0].drop('Var1',axis=1)
X[X['Var4']==1].drop('Var4',axis=1)
X[X['Var2']==1].drop('Var2',axis=1)

X[X['Var2']==1].drop('Var2',axis=1).mode().values[0]

books = [(17,8), (9,4), (18,5), (11,9), (1,2), (13,7), (7,5), (3,6), (10,8)]
book_combo = itertools.combinations(books,2)

book_analysis = []
for book1,book2 in book_combo:
    price = book1[0]+book2[0]
    weight = book1[1]+book2[1]
    book_analysis.append([(book1,book2),price,weight])


book_analysis_df = pd.DataFrame(book_analysis,columns=['Books','Price','Weight'])
book_n_dollar = book_analysis_df[book_analysis_df.Price == 18]




min_weight = sum([book[1] for book in books])


def book_combinations(book_list, N):
    result_list = []
    min_weight = sum([book[1] for book in book_list])

    def recursive_traverse(index, remaining_credit, total_weight, choosen_books,recur):
        print(recur,index, remaining_credit, total_weight, choosen_books)
        nonlocal result_list, min_weight
        if remaining_credit == 0 and len(choosen_books) > 1 and total_weight < min_weight:
            result_list = choosen_books
            min_weight = total_weight
        if index >= len(book_list) or remaining_credit < 0 or total_weight > min_weight:
            return
        recursive_traverse(index+1, remaining_credit,
                           total_weight, choosen_books,recur=1)
        recursive_traverse(index+1, remaining_credit -
                           book_list[index][0], total_weight+book_list[index][1], choosen_books+[book_list[index]],recur=2)

    recursive_traverse(0, N, 0, [],0)
    return result_list

book_combinations(books, N=18)




def min_max_scale(value,minV,maxV):
    return (value -minV)/(maxV - minV)

def normalize_grades(grades):
    grades_list = [i[1]for i in grades]
    max_grade = max(grades_list)
    min_grade = min(grades_list)

    normalize_grade = [(i[0],min_max_scale(i[1],min_grade,max_grade))
                        for i in grades]
    return normalize_grade



num_employees = np.array( [[10, 20, 30, 30, 10], [15, 15, 5, 10, 5], [150, 50, 100, 150, 50], [300, 200, 300, 100, 100], [1, 5, 1, 1, 2]] )
[[0.1, 0.2, 0.3, 0.3, 0.1], [0.3, 0.3, 0.1, 0.2, 0.1], [0.3, 0.1, 0.2, 0.3, 0.1], [0.3, 0.2, 0.3, 0.1, 0.1], [0.1, 0.5, 0.1, 0.1, 0.2]]
np.divide(num_employees.T,num_employees.sum(axis=1)).T


def funct_x_y(x,y):
    return 5**x * 3**y

L = 0
R = 40
N = 1000
def get_possible_values(L, R, N):
    solution_range = list(range(L,R+1))
    print(solution_range)
    result_list = []
    for x in range(0,N+1):
        for y in range(0,N+1):
            if funct_x_y(x,y) in solution_range:
                result_list.append([x,y])
    return result_list

# BUsiuness Days
date1 = '2021-01-31'
date2 = '2021-02-18'
dates = pd.date_range(date1,date2)
sum(np.array([i.isoweekday() for i in dates]) <= 5)



dictionary = {
    'a' : ['b','c','e'],
    'm' : ['c','e'],
}
input = 'c'

def closest_key(dictionary, input):
    dict_pos ={}
    for k,v in dictionary.items():
        pos = v.index(input)
        dict_pos[k] = pos 

    min_val = min(dict_pos.values())
    min_key = [k for k,v in dict_pos.items() if v == min_val]
    return min_key[0]



ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]
from datetime import datetime 
from collections import defaultdict
def read_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def weeks_from_date(starting_date, date):
    delta = read_date(date) - read_date(starting_date)
    return delta.days // 7

def group_by_weeks(ts):
    starting_date = ts[0]
    grouped = defaultdict(list)
    for date in ts:
        grouped[weeks_from_date(starting_date, date)].append(date)
    return list(grouped.values())
 
group_by_weeks(ts)


def moving_window(input_list, window_size):

      s = input_list
      output=[]

      for i in range(len(s)):
           if i < window_size:
                 avg=sum(s[0:i+1])/(i+1)
           else:
                 avg=sum(s[i-window_size+1:i+1])/window_size
           output.append(avg)   
      return output 

nums = [1,2,3,4,5,6]
window_size = 3

moving_window(nums, 4)