# ALGO ENGINEERING
 
The Alternating Disks Problem involves arranging a set of alternating dark and light disks into a configuration where all the light disks are on the left and all the dark disks are on the right. The disks start in an alternating pattern, and the goal is to solve the problem using a minimum number of swaps, where the only allowed move is swapping two adjacent disks.

This document covers two algorithms that solve this problem:

Left-to-Right Algorithm 
Lawnmower Algorithm
Both algorithms operate in O(n²) time, where n is the number of dark (and light) disks. The total number of disks is 2n.



Algorithm 1: Left-to-Right Algorithm
The Left-to-Right Algorithm works by iterating through the disks n times. During each iteration, the algorithm sweeps from left to right, comparing adjacent pairs of disks and swapping them if the left disk is dark and the right disk is light. After n iterations, all the dark disks will have been moved to the right, and all the light disks will be on the left.

Algorithm 2: Lawnmower Algorithm
The Lawnmower Algorithm is more efficient in terms of movement as it uses bidirectional sweeps. In each iteration, the algorithm first performs a left-to-right pass (like the Left-to-Right Algorithm), then immediately follows it with a right-to-left pass, pushing the light disks toward the left and the dark disks toward the right simultaneously.


Efficiency and Comparison
Both the Left-to-Right Algorithm and the Lawnmower Algorithm have a time complexity of 
𝑂(𝑛^2). However, the Lawnmower Algorithm tends to be faster in practice because it moves disks in both directions, reducing the number of necessary passes.

Both algorithms solve the alternating disks problem with a time complexity of O(n^2) which is optimal for the nature of the problem
