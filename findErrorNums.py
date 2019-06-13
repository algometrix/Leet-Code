from collections import Counter

def findErrorNums(nums):
    counter = Counter(nums)
    length = len(nums)
    dup_num = 0
    missing_num = 0
    for i in range(1, length + 1):
        if counter[i] == 2:
            dup_num = i
        elif counter[i] == 0:
            missing_num = i

    return [dup_num, missing_num]

if __name__ == "__main__":
    nums = [1,1]
    print(findErrorNums(nums))
