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
def solution(A):

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

