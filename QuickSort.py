#QuickSort 
# It is a Divide and Conquer algorithms
#   -Breaks down a problem into multiple subproblems recursively until they become simple to solve
#    -Solutions are conbined to solve original problem

#Running time
#   .O(n^2) worst case
#   .O(n * log(n))

#General Principle
# 1. Choose pivot element (Usually last or random)
# 2. Stores elements smaller than pivot in left subarray
#    Stores element greater than pivot in right subarray
# 3. Call quicksort recursively on left subarray
#    Call quicksort recursively on right subarray

#It uses two indexes, where:
#   - i goes from left to right -> Looks for element bigger than the pivot element
#   - j goes from right to left -> Looks for element smaller than the pivot element

# If i and j found an element bigger and smaller respectfully, then they switch places
# If one of them doesn't found an element bigger or smaller and j is on the left of i our quicksort algorithm stops
    #Swap element on index i with the element in the pivot, 
    #SO THE PIVOT IS IN ITS PLACE AND WE JUST HAVE TO ORDER THE REST OF THE ELEMENTS (LEFT TO 44 AND RIGHT TO 44)
    #So we can call recursively quicksort on both of the sides

#We also have to stop if j is equal to i at the end of the search
#If quicksort is called in only one element, it is automatically sorted

def QuickSort(nums):
    left = 0
    if len(nums) > 1:
        right = pivot - 1
    #If there is only one element left in the array
    else:
        #Return the only sorted
        return nums
        pass
    while left < right:
        if nums[left] < nums[pivot]:
            left += 1
        if nums[right] > nums[pivot]:
            right += 1
        if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
            nums[left], nums[right] = Swap(nums[left], nums[right])
    nums[left], nums[pivot] = Swap(nums[left], nums[right])
    
            


    pivot = len(nums) - 1

def Swap(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    return n1,n2

def main():
    print(QuickSort([22,11,88,66,55,77,33,44]))

main()