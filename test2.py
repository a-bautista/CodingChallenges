# # def solve(nums):
# #     res = []
# #     nums.sort()
# #
# #     # 2. Iterate through the array with range(len(nums-2))
# #     for i in range(len(nums) - 2):
# #
# #         # edge case
# #         if i > 0 and nums[i] == nums[i - 1]:
# #             continue
# #
# #         # 3. Define the two pointers
# #         left = i + 1
# #         right = len(nums) - 1
# #
# #         # 4. Start the while loop and do the sort of binary search
# #         while left < right:
# #
# #             currentSum = nums[left] + nums[right] + nums[i]
# #
# #             if currentSum > 0:
# #                 right -= 1
# #             elif currentSum < 0:
# #                 left += 1
# #             # 5. Define the logic when you have found a 0,i.e, append the value and increase pointers
# #             else:
# #                 res.append([nums[i], nums[left], nums[right]])
# #
# #                 # edge case, avoid duplicate values
# #                 while left <= right and nums[left] == nums[left + 1]:
# #                     left += 1
# #                 while left <= right and nums[right] == nums[right - 1]:
# #                     right -= 1
# #
# #                 right -= 1
# #                 left += 1
# #
# #     return res
# #
# #
# # def main():
# #     nums = [-1, 0, 1, 2, -1, -4]
# #     res = solve(nums)
# #     print(res)
# #
# #
# # main()
#
# # class Node:
# #     def __init__(self, key):
# #         self.val = key
# #         self.left = None
# #         self.right = None
# #
# # class Solution:
# #     def __init__(self):
# #         self.res = []
# #
# #     def print_preorder(self, root):
# #         # root - left -right
# #         if root:
# #             self.res.append(root.val)
# #             self.print_preorder(root.left)
# #             self.print_preorder(root.right)
# #
# # def main():
# #     root = Node(1)
# #     root.left = Node(7)
# #     root.right = Node(8)
# #     root.left.left = Node(9)
# #     root.left.right = Node(10)
# #     root.right.left = Node(11)
# #     root.right.right = Node(15)
# #     solution = Solution()
# #     print(solution.res)
# #
# # main()
#
# # class Node:
# #     def __init_(self, key):
# #         self.val = key
# #         self.left = None
# #         self.right = None
#
# # class Solution:
# #     def find_path(self, root):
# #         allPaths = []
# #         self.find_all_paths(root, [], allPaths)
# #         return sum(allPaths)
# #
# #     def find_all_paths(self, root, currentPath, allPaths):
# #
# #         if not root:
# #             return
# #
# #         # append the current root to the path
# #         currentPath.append(str(root.val))
# #
# #         # if you have found the target and the root has no children
# #         if root.left is None and root.right is None:
# #             temp = list(map(int, currentPath))
# #             #print(sum(temp))
# #             #print(currentPath)
# #             allPaths.append(sum(temp))
# #             #print(allPaths)
# #
# #         else:
# #             self.find_all_paths(root.left, currentPath, allPaths)
# #             self.find_all_paths(root.right, currentPath, allPaths)
# #
# #         # backtrack, delete the last inserted value
# #         del currentPath[-1]
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# class Solution:
#     def solve(self, root, target):
#         allPaths = []
#         self.backtrack(root, target, [], allPaths)
#         return allPaths
#
#     def backtrack(self, root, target, currentPath, allPaths):
#         if root is None:
#             return
#
#         currentPath.append(root.val)
#
#         if target == root.val and root.left is None and root.right is None:
#             allPaths.append(list(currentPath))
#
#         else:
#             self.backtrack(root.left, target - root.val, currentPath, allPaths)
#             self.backtrack(root.right, target - root.val, currentPath, allPaths)
#
#         del currentPath[-1]
#
# def main():
#     root = Node(3)
#     root.left = Node(4)
#     root.right = Node(5)
#     root.left.left = Node(1)
#     root.right.left = Node(2)
#     #root.right.right = Node(5)
#     target = 9
#     solution = Solution()
#     print("Tree paths with targetSum " + str(target) +
#           ": " + str(solution.solve(root, target)))
#
#
# main()

from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, p, q):
    if not root:
        return None
    if root.val in (p.val, q.val):
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right


def bfs(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        temp = []
        for _ in range(size):
            currentNode = queue.popleft()
            if currentNode:
                temp.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        # only get the last subtree from the deepest level, the subtree should be either a pair or just a single value
        if len(temp)>2:
            temp.pop()
        res.append(temp)
    return res[-1]

    # delete the all the nodes [:-1] the last pair are the last nodes

def main():
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.right.right.right = Node(10)
    #root.right.right.right.right = Node(11)

    res = bfs(root)
    sol = None
    if len(res)>=2:
        p = Node(res[0])
        q = Node(res[1])
        sol = lca(root, p, q)
    elif len(res)==1:
        p = q = Node(res[0])
        sol = lca(root, p, q)
    print(res)
    print(sol.val)
    #print(res)

main()