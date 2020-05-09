def seletction_sort(nums):
    n = len(nums)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if nums[j] < nums[m]:
                m = j
        nums[i], nums[m] = nums[m], nums[i]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]

def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, len(nums), gap):
            for j in range(i, 0, -gap):
                if nums[j] < nums[j - gap]:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]
        gap = gap // 2

def merge_sort(nums):
    if not nums or len(nums) < 2:
        return
    mid = len(nums) // 2
    # notice the slice operation means create a new list : id(left) != id(nums)
    left = nums[0:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    # merge left and right
    left_index, right_index, nums_idex = 0, 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            nums[nums_idex] = left[left_index]
            left_index += 1
        else:
            nums[nums_idex] = right[right_index]
            right_index += 1
        nums_idex += 1

    while left_index < len(left):
        nums[nums_idex] = left[left_index]
        nums_idex += 1
        left_index += 1

    while right_index < len(right):
        nums[nums_idex] = right[right_index]
        nums_idex += 1
        right_index +=1

def quick_sort(nums, low, high):
    if not nums or len(nums) <= 2 or low >= high:
        return
    def partition(arr, low, high):
        i = low + 1
        j = high
        while i <= j :
            if arr[i] <= arr[low]:
                i += 1
                continue
            if arr[j] >= arr[low]:
                j -= 1
                continue
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    pi = partition(nums, low, high)
    quick_sort(nums, low, pi-1)
    quick_sort(nums, pi+1, high)

#this is better for array which contians a lot of deplicated numbers
def quick_3way_sort(nums, low, high):
    if low >= high:
        return
    i = low + 1
    left = low
    right = high
    pivot = nums[low]
    while i <= right:
        if nums[i] == pivot:
            i += 1
        elif nums[i] < pivot:
            nums[i], nums[left] = nums[left], nums[i]
            i += 1
            left += 1
        else:
            nums[i], nums[right] = nums[right],nums[i]
            right -= 1
    quick_3way_sort(nums,low, left-1)
    quick_3way_sort(nums, right+1, high)


if __name__ == "__main__":
    arr = [ 12, 34, 54, 2, 3]
    arr = [12, 7, 3, 1, 34, 54, 2, 5, 15, 13]
    # shell_sort(arr)
    # merge_sort(arr)
    # quick_sort(arr, 0, len(arr)-1)
    # print(arr)
    arr = [2,3,2,3,2,1,1,1,5,3,5,3,2,1,4]
    # quick_sort(arr, 0, len(arr)-1)
    quick_3way_sort(arr, 0, len(arr)-1)
    print(arr)
