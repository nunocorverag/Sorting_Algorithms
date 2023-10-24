#Insertion Sort

#The array is split into a sorted and unsorted part. 
#The values from the unsorted part are picked and placed at the correct position in the sorted part

#Iterates over the arre and compares the kurrent element to its predecessor,
#if the key element is smaller than its predecessor, it compares it to the elements before.

def InsertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key
    return(nums)
def main():
    print(InsertionSort([5,1,7,4,9,12,2,3]))

main()