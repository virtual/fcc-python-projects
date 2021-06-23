import copy
import random
# Consider using the modules imported above.

class Hat:
  contents = []

# red=0, orange=0, black=0, blue=0, pink=0, green=0, striped=0
  def __init__(self, **kwargs):
    self.contents = [] # Need to reset for some reason
    for arg in kwargs:
      if (kwargs[arg] > 0):
        # print('!',arg, kwargs[arg])
        for iter in range(0, kwargs[arg]):
          self.contents.append(arg)  
    
    print('created',self.contents)
    
    return None

  def __str__(self):
    return 'mew'
  
  def draw(self, count = 0):
    '''
    The `Hat` class should have a `draw` method that accepts an argument indicating 
    the number of balls to draw from the hat.
    This method should remove balls at random from `contents` and return those balls 
    as a list of strings.
    The balls should not go back into the hat during the draw, similar to an urn 
    experiment without replacement.
    If the number of balls to draw exceeds the available quantity, return all the balls.
    '''
    contents = copy.copy(self.contents)
    # comparator = set(contents)
    randoBalls = []
    if (count < len(randoBalls)):
      return randoBalls
    elif (count > len(contents)):
      return contents
    else:
      for iter in range(0, count):
        while len(randoBalls) < count:
          randomSelection = random.choice(contents)
          print('r',randomSelection)
          contents.remove(randomSelection)
          randoBalls.append(randomSelection)
        else:
          break
     
    self.contents = contents
    randoBalls = sorted(randoBalls, key = str)
    print ('plucked out', randoBalls)
    return randoBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  return expected_balls