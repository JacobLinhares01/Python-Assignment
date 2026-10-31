#this function takes 3 integers, A and B which are within the range [0..2,000,000,000]
#and K which is within the range [1..2,000,000,000], with A <= B
# the goal is to figure out how many numbers in the range of A and B are divisible by K 

def soln(A, B, K):
  # we take B and floor divide it with K then subtract it to A-1 floor divide K
  # Ex: if A=5, B=25, and K = 10 then (B//K) = 2 and ((A-1)//K) = 0 so then 2-0 = 2 which is correct because there are only 2 numbers that fit 
  # [10, 20]
  return (B//K) - ((A-1)//K)
