def solution(A):
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
