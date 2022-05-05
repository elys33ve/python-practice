#tiny bit of statistics stuff? idkr what I was going for but i didn't get too far apparently

import math as m
import statistics as s

#stuff
list_ = [1,2,3]                     #list
sum_ = 0
len_ = len(list_)                   #list length

#MEAN

for i in range(len_):
    list_[i] = int(list_[i])        #convert to int
    sum_ = sum_ + list_[i]          #sum of values

mean = sum_/len_                    #mean
mean_test = s.mean(list_)

print(mean)
print(mean_test)
print("\n")

#STANDARD DEVIATION

sd_sum = 0

for i in range(len_):
    x = (list_[i] - mean)**2        
    sd_sum = sd_sum + x             #sum

st_dev = (sd_sum/len_)**(1/2)       #standard deviation
st_dev_test = s.stdev(list_)        #rounds to int

print(f"{st_dev:.2f}")
print(st_dev_test)
