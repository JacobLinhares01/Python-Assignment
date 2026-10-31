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
