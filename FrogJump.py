# the goal of this function is to figure out how many jumps it would take for the frog with its fixed distance to reach its target
# where X is the start position, Y is the target position and D is the fixed jump distance
def solution (X, Y, D):
  # we subtract the target distance by the start position before 
  # adding an extra jump just in case we fall short and if we dont, we subtract 1 off D because we floor divide this whole equation by D to find the amount of jumps
  # Ex X = 0, Y = 10, D = 1
  # (10 - 0) = 10; 10 + (1-1) = 10; 10 // 1 = 10 and this makes sense as the frog needs to jump 10 times to reach his target distance
  return ((Y - X) + (D - 1)) // D
