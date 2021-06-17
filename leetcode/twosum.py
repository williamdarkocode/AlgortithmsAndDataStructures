def twoSum(nums, target):
    for i in range(len(nums)):
        other = target - nums[i]
        idx = list(nums[i+1:]).index(other)
        if(idx):
            return [i,idx+1]
    

def main():

    arr = input("enter list: ")
    tag = input("enter target: ")

    arr = arr.split(',')

    arr = list(arr)

    twoSum(arr, tag)


if __name__ == "__main__":
    main()