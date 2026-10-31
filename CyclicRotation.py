# the goal of this function is to shift A list of A to the right K number of times
# where A is the list that will be shifted/rotated and K is the number of rotations that are going to be made
# K is an integer within the range [0..100] and each element of array A is an integer within the range [−1,000..1,000]
def solution(A, K):
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
