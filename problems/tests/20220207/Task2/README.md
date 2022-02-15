# Task 2

## Problem Description

A transportation company wishes to begin service in the city of Nazeriana. The company has a base location where it parks all its vehicles. They have identified some pickup locations where the vehicles will collect passengers. Now the company wishes to identify the straight line routes from the base location to the pickup locations. They wish to minimize the number of routes while ensuring that all the pickup locations are covered.

Write an algorithm to help the company identify the minimum number of straight line routes from the base location to the

pickup locations covering every pickup location.

**Input**

The first line of the input consists of two space-separated integers *num* and *numCord*, representing the number of pickup locations (N) and number of coordinates for a pick up location (numCord (P) is always equal to two), respectively. The next N lines consist of P space separated integers - *pickX* and *pickY* representing the X and Y coordinates of a pickup location, respectively. 
The next line consists of an integer *baseX* representing the X coordinate of the base location.

The next line consists of an integer *baseY* representing the Y coordinate of the base location.

**Output**

Print an integer representing the minimum number of routes connecting all the pickup locations to the base location.

**Constraints**

- 1 <= num <= 10^5
- -10^3 <= pickX, pickY, baseX, baseY <= 10^3

**Example**

Input:
3 2
1 1
-1 1
2 3
0
0

Output:
3

Explanation:
From the base coordinate (0, 0), three different routes will cover all the pickup locations.