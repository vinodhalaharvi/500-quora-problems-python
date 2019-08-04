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
    return None

def asser(cond, string): 
    if not cond: 
        print string
        import sys
        sys.exit(99)

def maxLengthSubArrayWithGivenSum(lst, givenSum): 
    def do(lst, givenSum): 
        i = 0
        j = len(lst)
        while i <= j: 
            while j >= i: 
                if sum(lst[i:j]) == givenSum: 
                    return lst[i:j]
                j -= 1
            j = len(lst)
            i += 1
        return []
    asser(do([1, 2], 3) == [1, 2], 
        " maxLengthSubArrayWithGivenSum not implementation not right")
    asser(do([1, 2, 2], 4) == [2, 2], 
        " maxLengthSubArrayWithGivenSum not implementation not right")
    return do(lst, givenSum)

def maxLengthSubArrayWithEqualZerosAndOnes(lst): 
    def ones(lst): 
        count = 0
        for i in range(len(lst)):
            if lst[i] == 1: 
                count += 1
        return count
    asser(ones([1,1,1,1]) == 4, "bad ones ")
    def zeros(lst): 
        count = 0
        for i in range(len(lst)):
            if lst[i] == 0: 
                count += 1
        return count
    asser(zeros([0,0,0,0]) == 4, "bad zeros ")
    def equalOnesZeros(lst, i, j): 
        return ones(lst[i:j]) == zeros(lst[i:j])
    asser(equalOnesZeros([0,0,1,1], 0, 4), "bad equalOnesZeros")
    def do(lst):
        i = 0 
        j = len(lst)
        while i <= j: 
            while j >= i: 
                if equalOnesZeros(lst, i, j+1):
                    return lst[i: j+1]
                j -= 1
            j = len(lst) 
            i += 1
        return []
    return do(lst)

def findLargestSubArrayConsecutiveIntegers(lst): 
    # TODO still buggy ? 
    store = {}
    for i in range(len(lst)): 
        store[lst[i]] = True

    def conseq(store, lst, i): 
        if (lst[i]-1) in store  or (lst[i]+1) in store:
            return True
        return False

    def uniq(lst): 
        store = {}
        rslt = [] 
        for i in range(len(lst)): 
            try:
                store[lst[i]]
            except:
                store[lst[i]] = True
                rslt.append(lst[i])
        return rslt 
    asser(uniq([1, 2, 2, 3]) == [1, 2, 3], "uniq implementation not right")

    i = len(lst)
    while True: 
        if not conseq(store, lst, i-1): 
            lst = lst[:i]
        i -= 1
        if i <= 0: 
            break
    return uniq(lst)

def sortZerosOnesTwos(lst): 
    def countZeros(lst): 
        count = 0
        for i in range(len(lst)): 
            if lst[i] == 0: 
                count += 1
        return count
    asser(countZeros([0,0,0,0]) == 4, "bad zeros")
    def countOnes(lst): 
        count = 0
        for i in range(len(lst)): 
            if lst[i] == 1: 
                count += 1
        return count
    asser(countOnes([1, 1]) ==  2, "bad countOnes")
    def countTwos(lst): 
        count = 0
        for i in range(len(lst)): 
            if lst[i] == 2: 
                count += 1
        return count
    asser(countTwos([2, 2, 2]) ==  3, "bad countTwos")
    zeros = countZeros(lst)
    ones = countOnes(lst)
    twos = countTwos(lst)
    return [0]*zeros + [1]*ones + [2]*twos

if __name__ == "__main__":
    print " sortZerosOnesTwos", sortZerosOnesTwos([0, 1, 2, 2, 1, 0, 0 , 2, 0 , 1, 1, 0])
    import sys
    sys.exit(0)
    print " maxLengthSubArrayWithEqualZerosAndOnes", maxLengthSubArrayWithEqualZerosAndOnes([0,0,1,0,1,0,0])
    print " maxLengthSubArrayWithGivenSum",  maxLengthSubArrayWithGivenSum([5, 6, -5, 5, 3, 5, 3, -2, 0], 19)
    print " findLargestSubArrayConsecutiveIntegers ..", findLargestSubArrayConsecutiveIntegers([2, 0, 2, 1, 4, 3, 1, 0])
    print " sum with given pair .. ",  pairWithGivenSum([1, 2, 3], 4)
    print " check subarray with  0 sum exist ..",  checkSubArrayWith([121, 1, -3, -2, -5, 5,  3, 32, 1, 2 ])
    print " check subarray with  0 sum exist ..",  checkSubArrayWith([4, 2, -3, -1, 0, 4])
    print " sort binary array in linear time",  sortBinaryArray([0, 1, 1, 0, 1, 1])
    print " duplicate element in array is ",  duplicate([0, 1, 1, 0, 1, 1])
