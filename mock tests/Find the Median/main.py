# function to find the median in a range of values
def find_median(arr):
    nums = sorted(arr)
    index = int((len(nums) - 1) / 2)
    return nums[index]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    
    if len(nums) % 2 == 0:
        print('Total amount of inputted number is not odd...')
    else:
        median = find_median(nums)
        print(f'sorted = {sorted(nums)}')
        print(f'median = {median}')

