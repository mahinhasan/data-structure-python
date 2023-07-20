def isSumZero(nums):

    for i in range(len(nums)):
        lst = []
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            lst.append(nums[j])
            if total == 0:
                print("Found",(i,j))
                
                print(lst)
    
if __name__=="__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    isSumZero(nums)