import random

def main():
    array = [-1,1,4,3,4.5,5,6,7,8,200]
    random.shuffle(array)
    bubblesort(array)
    print(array)


'''
bubblesort:
take in jumbled array
check the first value against the second
if the value is greater, swap them
else if the value is less, leave them be
compare the second one to the one after it
keep looping from 0 to n then 0 to n-1
when n-1 is 0 stop looping
'''
def bubblesort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


'''
selection sort:
take jumbled array
create sorted & unsorted array
find smallest value from unsorted and move
continue til end
'''
def selectionsort(arr):
    sorted = []
    unsorted = arr
    for j in range(len(arr)):
        small = 100
        for i in range(len(unsorted)):
            if small >= unsorted[i]:
                small = unsorted[i]
        sorted.append(small)
        unsorted.remove(small)
    arr[:] = sorted

'''
mergesort:
take in jumbled array
find middle and split array
keep splitting until 1 value remains
merge values by creating a new array and
taking the lowest value of the two merging arrays
'''

def mergesort(arr):
    def split(split_arr):
        split_val = len(split_arr)//2
        return split_arr[:split_val], split_arr[split_val:]
    def merge(farr, sarr):
        merged = []
        while True:
            if not len(farr):
                merged += sarr
                break
            elif not len(sarr):
                merged += farr
                break
            else:
                if farr[0] < sarr[0]:
                    merged.append(farr.pop(0))
                elif sarr[0] < farr[0]:
                    merged.append(sarr.pop(0))
                else:
                    merged.append(sarr.pop(0))
                    merged.append(farr.pop(0))
        return merged
    print("splitting", arr)
    if len(arr) > 1:
        left, right = split(arr)
        print("merging", left, right)
        arr = merge(mergesort(left), mergesort(right))
        print("arr=", arr)
    print("done")
    return arr













if __name__ == "__main__":
    main()
