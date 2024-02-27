def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2


# 1. Best case in this scenario would be when none of the elements in the list are greater
#   than 5 because this loop would not execute and the function will only perform a single 
#   pass through the outer loop. O(n)
#   Worst case would be when all of the elements are greater than 5, resulting in both inner 
#   and outer loops to iterate over all elements in the list. O(n^2)
#   Average case would also result in O(n^2) because a good portion of the list will contain  
#   elements greater than 5. 

# 2. No they are not the same as I have shown above, they don't all have the same complexity.
# modified version of code:

def processdata(li):
    for i in range(len(li)):
        li[i] *= 2             

# With this modification the complexity for best, wordt, and average is all O(n).
# since the for loop will always be run. 

