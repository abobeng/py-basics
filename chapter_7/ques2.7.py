
import random
rlist = random.sample(range(1, 100), 20)
print(rlist)

average_lst = sum(rlist)/len(rlist)
print(average_lst)

print('the maximum element is :',max(rlist))
print('the minimum element is : ',min(rlist))

rlist.sort()
print("the second largest element is:", rlist[len(rlist)-2])
print("the second smallest element is:", rlist[1])

even = [num for num in rlist if num % 2 == 0]
print(len (even))
