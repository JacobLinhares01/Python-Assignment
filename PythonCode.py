#This Function is given the Array A and trys to find the missing element in the array
#with all distinct elements in A
#and each element of array A is an integer within the range [1..(N + 1)]
# and N is an integer within the range [0..100,000]
def PermMissingElem_solution(A):
  #checks if the list is empty
  # if so it returns the default value of 1
  if len(A) == 0:
      return 1
    
  #grabs the length of the list
  #then it finds the expected sum from the length + 1 and + 2
  # after it calculates the actual sum of A
  N = len(A)
  ExSum = ((N + 1) * (N + 2)) // 2
  ActSum = sum(A)

  # it returns the difference between the 2 sums
  return (ExSum - ActSum)

##\\_______________________________________________________________________________________________________//##

# the goal is to find the smallest positive integer that does not occur the list A.
# where each element of array A is an integer within the range [−1,000,000..1,000,000]
def MissingInteger_solution(A):

  # we convert the list A into a set for set operations
  # then we check if the max value is below 0 Ex: [-1,-2,-3,..............-n]
  #if so then we return the lowest positive number of 1
  A = set(A)
  if max(A) < 0:
      return 1

  # we create a new set called B which holds every positive number from 1 to the max of A
  B = set(range(1, max(A) + 1))

  # we return the min of the set (B - A) if and only if the missing int is between A and B
  # otherwise we return the max of A + 1;
  return min(B - A) if (B - A) else (max(A) + 1)

##\\_______________________________________________________________________________________________________//##

# the goal of this function is to figure out how many jumps it would take for the frog with its fixed distance to reach its target
# where X is the start position, Y is the target position and D is the fixed jump distance
def FrogJump_solution(X, Y, D):
  # we subtract the target distance by the start position before 
  # adding an extra jump just in case we fall short and if we dont, we subtract 1 off D because we floor divide this whole equation by D to find the amount of jumps
  # Ex X = 0, Y = 10, D = 1
  # (10 - 0) = 10; 10 + (1-1) = 10; 10 // 1 = 10 and this makes sense as the frog needs to jump 10 times to reach his target distance
  return ((Y - X) + (D - 1)) // D

##\\_______________________________________________________________________________________________________//##

# the goal of this function is to shift A list of A to the right K number of times
# where A is the list that will be shifted/rotated and K is the number of rotations that are going to be made
# K is an integer within the range [0..100] and each element of array A is an integer within the range [−1,000..1,000]
def CyclicRotation_solution(A, K):
  # check to see if A is an empty list; if it is then return the empty list
  if not A:
    return A
  # grab the length of the list and call it N    
  N = len(A)

  # reduce unnecessary rotations if K is greater than the array length; and if K = 0 after the reduction then we dont change the list and return it
  K = K % N
  if K == 0: 
    return A
  # Slice the array and join together the rotated parts
  return A[-K:] + A[:-K]

##\\_______________________________________________________________________________________________________//##

#this function takes 3 integers, A and B which are within the range [0..2,000,000,000]
#and K which is within the range [1..2,000,000,000], with A <= B
# the goal is to figure out how many numbers in the range of A and B are divisible by K 

def CountDiv_solution(A, B, K):
  # we take B and floor divide it with K then subtract it to A-1 floor divide K
  # Ex: if A=5, B=25, and K = 10 then (B//K) = 2 and ((A-1)//K) = 0 so then 2-0 = 2 which is correct because there are only 2 numbers that fit 
  # [10, 20]
  return (B//K) - ((A-1)//K)

##\\______________________________________________Test Section_____________________________________________//##
#PermMissingElem_solution()
#MissingInteger_solution()
#FrogJump_solution
#CyclicRotation_solution()
#CountDiv_solution()
