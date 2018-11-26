##creating an initial file to see what happens.

print ("Hello World")

def sum_nubmers(num_one, num_two):
    ans = num_one + num_two
    return  ans

print (sum_nubmers(4,132))

def sum_recursive(num_one, num_two):
    num_one += 1
    ans = 0
    if num_two > 1:
        num_two-=1
        print(num_two)
        ans = sum_recursive(num_one, num_two)
    else:
        ans = num_one
    return ans

test = sum_recursive(6,7)

print(test)
