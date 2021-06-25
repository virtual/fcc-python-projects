import copy
import random
import operator
# for truly random use sr
sr = random.SystemRandom()
# Consider using the modules imported above.

class Hat:
  contents = []

# red=0, orange=0, black=0, blue=0, pink=0, green=0, striped=0
  def __init__(self, **kwargs):
    self.contents = [] # Need to reset for some reason
    for arg in kwargs:
      if (kwargs[arg] > 0):
        for iter in range(0, kwargs[arg]):
          self.contents.append(arg)  
    return None
  
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
    # print(count)
    if (count < len(randoBalls)):
      return randoBalls
    elif (count > len(contents)):
      return contents
    else:
      for iter in range(0, count):
        while len(randoBalls) < count:
          # for truly random use sr
          randomSelection = random.choice(contents)
          # randomSelection = sr.choice(contents)
          contents.remove(randomSelection)
          randoBalls.append(randomSelection)
        else:
          break
     
    self.contents = contents
    randoBalls = sorted(randoBalls, key = str)
    return randoBalls

  # returns a dictionary of
  # balls and their counts from a 
  # list of balls
  def countBalls(self, picks):
    uniquePicks = list(set(copy.copy(picks)))
    balls = {}
    for iter in range(0, len(uniquePicks)):
      ballType = uniquePicks[iter]
      count = picks.count(ballType)
      balls[ballType] = count
    sortedList = dict(sorted(balls.items(), key=operator.itemgetter(0)))
    return sortedList

  def listBallsFromCount(self, dictPicks):
    newDict = []
    for (key, count) in dictPicks.items():
    # Add each value 'count' times to list 
      for iter in (range(0, count)):
        newDict.append(key)
    return newDict

# Check if the given list (listIn) is a complete subset of listFull
def compareLists(listIn, listFull):
  matches = 0
  for iter in range(0, len(listIn)):
    if(set([listIn[iter]]).issubset(set(listFull))):
      listFull.remove(listIn[iter])
      matches = matches + 1
  if (matches == len(listIn)):
    return True
  else: 
    return False

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''
  * `hat`: A hat object containing balls that should be copied inside the function.

  * `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.

  * `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.

  * `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

  probability = experiment(hat=hat, 
  expected_balls={"red":2,"green":1},
  num_balls_drawn=5,
  num_experiments=2000)
  '''
  matches = 0
  expected_balls = hat.listBallsFromCount(expected_balls)
  for iter in range(0, num_experiments):
    hatObj = copy.copy(hat)
    randomSet = hatObj.draw(num_balls_drawn)

    #if expected_balls is a partial set of randomSet
    if compareLists(expected_balls, randomSet):
      matches = matches + 1

  return matches/num_experiments