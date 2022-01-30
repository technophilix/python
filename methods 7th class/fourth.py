def add(farg, *arg):
    sum = farg
    for i in arg:
        #sum = sum +i
        sum+=i
    print(sum)

add(1,2)        
add(1,2,4)        
add(1,2,5,6)        
add(1,2,7,8,9,13,56)    


f = lambda x:x*x

print(f(5))