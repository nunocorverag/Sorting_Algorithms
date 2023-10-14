#Selection sort: We go from start from start to end and find the min or max value depending on the implementation
#In each iteration, we will find the min value
#Swap the min value, with the corresponding element

def Selection_Sort(nums):
    #We want the sorting decrease by -1
    for i in range(len(nums)):
        minValueIndex = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minValueIndex]:
                minValueIndex = j
        temp = nums[i]
        nums[i] = nums[minValueIndex]
        nums[minValueIndex] = temp
    return(nums)

def main():
    print(Selection_Sort([5,3,8,6,7,2]))

main()