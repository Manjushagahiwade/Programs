from itertools import count

a = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
for element in a:
    i = 1
    count=0
    while i < 9:
        c = element%i
        if c==0:
            count+=1
        i= i+1
        print(count)