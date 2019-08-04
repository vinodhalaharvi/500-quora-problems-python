# find-pair-with-given-sum-array
# using hashing
def pairWithGivenSum(lst, s):
    dct = {}
    for i in range(len(lst)): 
        try: 
            dct[s-lst[i]]
            return lst[i], (s-lst[i])
        except: 
            dct[lst[i]] = True
    return None, None

# /check-subarray-with-0-sum-exists-not/
def checkSubArrayWith(lst):
    dct = {} 
    # hash i, j
    sum = 0 
    for i in range(len(lst)): 
        sum += lst[i]
        try:
            dct[sum]
            return True
        except: 
            dct[sum] = True
    return False

def printSubArraysZeroSum(lst):
   pass 

def sortBinaryArray(lst):
    countZeros = 0
    rslt = []
    for i in range(len(lst)): 
        if  lst[i] == 0:
            countZeros += 1 
    for i in range(countZeros): 
        rslt.append(0)
    for i in range(len(lst) - countZeros): 
        rslt.append(1)
    return rslt


def duplicate(lst): 
    def already(lst, i): 
        try: 
            dct[lst[i]]
            return True
        except:
            return False

    dct = {}
    for i in range(len(lst)):
        if already(lst, i): 
            return lst[i]
        else: 
            dct[lst[i]] = True
    return False




if __name__ == "__main__":
    print " sum with given pair .. ",  pairWithGivenSum([1, 2, 3], 4)
    print " check subarray with  0 sum exist ..",  checkSubArrayWith([121, 1, -3, -2, -5, 5,  3, 32, 1, 2 ])
    print " check subarray with  0 sum exist ..",  checkSubArrayWith([4, 2, -3, -1, 0, 4])
    print " sort binary array in linear time",  sortBinaryArray([0, 1, 1, 0, 1, 1])
    print " duplicate element in array is ",  duplicate([0, 1, 1, 0, 1, 1])
