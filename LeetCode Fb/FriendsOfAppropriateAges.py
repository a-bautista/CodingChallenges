'''
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

    age[B] <= 0.5 * age[A] + 7
    age[B] > age[A]
    age[B] > 100 && age[A] < 100

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.



Notes:

    1 <= ages.length <= 20000.
    1 <= ages[i] <= 120.


'''

from collections import Counter
class Solution:
    def numFriendsRequests(self, ages):
        # translation of the initial requirements for making the age request valid
        def friendRequest( a,b):
           if b <= .5 *a+7:
               return True
           if b > a:
               return False
           return True


        age_groups = Counter(ages)
        total_req = 0
        # for every person's age, you need to check if you can make a friend request
        # with the rest of the people in the array, so that's why we make a double
        # for loop [16,17,18], so 16 is going to check with 16, 17, 18 then 17 will
        # check with 16, 17 and 18 and so on
        for a, num_a in enumerate(age_groups.values()):
            for b, num_b in enumerate(age_groups.values()):
                if friendRequest(a,b):
                    # store the number of current requests
                    total_req += num_a * num_b
                    # when you compare the same person in the array, you need to
                    # subtract it
                    if a == b:
                        total_req -= num_a
        return total_req


def main():
    ages = [16, 17, 18]
    solution = Solution()
    res = solution.numFriendsRequests(ages)
    print(res)

main()

'''
Time complexity: O(N) where N is the number of people 
Space complexity: O(A) where A is the number of ages
'''

