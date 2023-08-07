# Leet Code exercices

## Arrays and hashing

- [x] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (5th August 2023)
- [x] [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (5th August 2023)
- [x] [Two Sum](https://leetcode.com/problems/two-sum/) (5th August 2023)
- [x] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (6th August 2023)
- [x] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (7th August 2023)
- [ ] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [ ] [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (WIP)
- [ ] [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- [ ] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Two pointers

- [ ] Valid Palindrome
- [ ] Sum II Input Array Is Sorted
- [ ] 3Sum
- [ ] Container With Most Water
- [ ] Trapping Rain Water

## Stack

- [ ] Valid Parentheses
- [ ] Stack
- [ ] Evaluate Reverse Polish Notation
- [ ] Generate Parentheses
- [ ] Daily Temperatures
- [ ] Car Fleet
- [ ] Largest Rectangle In Histogram

## Binary search

- [ ] Binary Search
- [ ] Search a 2D Matrix
- [ ] Koko Eating Bananas
- [ ] Find Minimum In Rotated Sorted Array
- [ ] Search In Rotated Sorted Array
- [ ] Time Based Key Value Store
- [ ] Median of Two Sorted Arrays

## Linked List

- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Reorder List
- [ ] Remove Nth Node From End of List
- [ ] Copy List With Random Pointer
- [ ] Add Two Numbers
- [ ] Linked List Cycle
- [ ] Find The Duplicate Number
- [ ] LRU Cache
- [ ] Merge K Sorted Lists
- [ ] Reverse Nodes In K Group

## Trees

- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Diameter of Binary Tree
- [ ] Balanced Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor of a Binary Search Tree
- [ ] Binary Tree Level Order Traversal
- [ ] Binary Tree Right Side View
- [ ] Count Good Nodes In Binary Tree
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element In a Bst
- [ ] Construct Binary Tree From Preorder And Inorder Traversal- [ ]
- [ ] Binary Tree Maximum Path Sum
- [ ] Serialize And Deserialize Binary Tree

Tries

- [ ] Implement Trie Prefix Tree
- [ ] Design Add And Search Words Data Structure
- [ ] Word Search II

Heap and priority queue

- [ ] Kth Largest Element In a Stream
- [ ] Last Stone Weight
- [ ] K Closest Points to Origin
- [ ] Kth Largest Element In An Array
- [ ] Task Scheduler
- [ ] Design Twitter
- [ ] Find Median From Data Stream

## BackTracking

- [ ] Subsets
- [ ] Combination Sum
- [ ] Permutations
- [ ] Subsets II
- [ ] Combination Sum II
- [ ] Word Search
- [ ] Palindrome Partitioning
- [ ] Letter Combinations of a Phone Number
- [ ] N Queens

## Graphs

- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Max Area of Island
- [ ] Pacific Atlantic Water Flow
- [ ] Surrounded Regions
- [ ] Rotting Oranges
- [ ] Walls And Gates
- [ ] Course Schedule
- [ ] Course Schedule II
- [ ] Redundant Connection
- [ ] Number of Connected Components In An Undirected Graph
- [ ] Graph Valid Tree
- [ ] Word Ladder

## Advanced graphs

- [ ] Reconstruct Itinerary
- [ ] Min Cost to Connect All Points
- [ ] Network Delay Time
- [ ] Swim In Rising Water
- [ ] Alien Dictionary
- [ ] Cheapest Flights Within K Stops

## 1D Dynamic programing

- [ ] Climbing Stairs
- [ ] Min Cost Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Longest Palindromic Substring
- [ ] Palindromic Substrings
- [ ] Decode Ways
- [ ] Coin Change
- [ ] Maximum Product Subarray
- [ ] Word Break
- [ ] Longest Increasing Subsequence
- [ ] Partition Equal Subset Sum

## 2D Dynamic programing

- [ ] Unique Paths
- [ ] Longest Common Subsequence
- [ ] Best Time to Buy And Sell Stock With Cooldown
- [ ] Coin Change II
- [ ] Target Sum
- [ ] Interleaving String
- [ ] Longest Increasing Path In a Matrix
- [ ] Distinct Subsequences
- [ ] Edit Distance
- [ ] Burst Balloons
- [ ] Regular Expression Matching

## Greedy

- [ ] Maximum Subarray
- [ ] Jump Game
- [ ] Jump Game II
- [ ] Gas Station
- [ ] Hand of Straights
- [ ] Merge Triplets to Form Target Triplet
- [ ] Partition Labels
- [ ] Valid Parenthesis String

## Intervals

- [ ] Insert Interval
- [ ] Merge Intervals
- [ ] Non Overlapping Intervals
- [ ] Meeting Rooms
- [ ] Meeting Rooms II
- [ ] Minimum Interval to Include Each Query

## Math and geometry

- [ ] Rotate Image
- [ ] Spiral Matrix
- [ ] Set Matrix Zeroes
- [ ] Happy Number
- [ ] Plus One
- [ ] Pow(x, n)
- [ ] Multiply Strings
- [ ] Detect Squares

## Bit manipulation

- [ ] Single Number
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Reverse Bits
- [ ] Missing Number
- [ ] Sum of Two Integers
- [ ] Reverse Integer

## Other exercices

## List :

- [x] [lengthOfLongestSubstring](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (4th
  August 2023)
- [x] [findMedianSortedArrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (4th August 2023)


```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            tmp = 1
            for j in range(l):
                if i == j:
                    continue
                tmp *= nums[j]
            res[i] = tmp
        return res
```