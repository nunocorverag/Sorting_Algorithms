def Bubble_Sort(nums):
    #We want the sorting decrease by -1 until it reaches the last element
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return(nums)

def main():
    print(Bubble_Sort([6,9,4]))

main()