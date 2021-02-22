def main():
    result1 = solve([8,3,4,5],2)
    result2 = solve_pythonistic([8,3,4,5],2)
    #result3 = my_solution([8,3,4,5],2)
    print(result1)
    print(result2)
    #print(result3)

def solve_pythonistic(nums,k):
    n = len(nums)
    if n * k == 0:
       return []
    return [max(nums[i:i + k]) for i in range(n - k + 1)]


def solve(nums, k):
    n = len(nums)
    if n * k == 0: # base case when k is given as a zero value
        return []
    values = []
    for i in range(n -k +1):
        values.append(max(nums[i:i+k]))
    return values

def my_solution(nums, k):
    '''Needs debugging'''
    list1 = []
    list2 = []
    window = 0
    for i in range(len(nums)):
        list1.append(nums[i])
        if window >= k-1:
            list2.append(max(list1[i:k]))
            list1 = []
            window = 0
        window += 1
    return list2


if __name__ == '__main__':
    main()
'''
  Given an array of n elements and an integer k, 
  return the max values from n elements based on the scope of k, that is:

  [8,4,6,12] and k=2

  then the result will be 8,12

  1. Only integer values in the array and k.
  
  2. k is always positive.

  3. If k > len(array) throw exception index out of bounds

  4. If 1 < k < len(array)-1 then do a double pointer solution to keep the time complexity in the O(n) time complexity.

  5. While the first pointer <  len(array)-1 then set the subarray to the k-1 length and then do an increment after each pass.

  6. Max value will be obtained by using the max function or printing 

  Complexity Analysis

  Time complexity : O(Nk)\mathcal{O}(N k)O(Nk), where N is number of elements in the array.
  
  
  Test cases
  
  I. [8, 4, 7, 9, 6 ]
      0  1  2  3  4
      
      k = 2 (even)
      n = 5
      n - k = 3
      n - k + 1 = 4 (you will generate 4 subarrays) 
     
      i: i + k
      0: 0 + 2 = 2  (from the first element to the non-touching 2 element)
      1: 1 + 2 = 3  (from the first element to the non-touching 3 element)
      2: 2 + 2 = 4  (from the first element to the non-touching 4 element)
      3: 3 + 2 = 5  (from the first element to the non-touching 5 element)
      
  II. [8, 4, 7, 9, 6 ]
       0  1  2  3  4
      
      k = 3 (odd)
      n = 5
      n - k = 2
      n - k + 1 = 3 (you generate subarrays with this formula) 
     
      i: i + k
      0: 0 + 3 = 3  (from the first element to the non-touching 3 element)
      1: 1 + 3 = 4  (from the first element to the non-touching 4 element)
      2: 2 + 3 = 5  (from the first element to the non-touching 5 element)
      
      
  III. [8, 4, 7, 9 ]
        0  1  2  3 
      
      k = 3 (odd)
      n = 4 (even)
      n - k = 2
      n - k + 1 = 2 (you generate subarrays with this formula) 
     
      i: i + k
      0: 0 + 3 = 3  (from the first element to the non-touching 3 element)
      1: 1 + 3 = 4  (from the first element to the non-touching 4 element)
      
      
  IV. [8, 4, 7, 9 ]
       0  1  2  3 
      
      k = 2 (even)
      n = 4 (even)
      n - k = 2
      n - k + 1 = 3 (you generate subarrays with this formula) 
     
      i: i + k
      0: 0 + 2 = 2  (from the first element to the non-touching 2 element)
      1: 1 + 2 = 3  (from the first element to the non-touching 3 element)
      2: 2 + 2 = 4  (from the first element to the non-touching 4 element)


'''