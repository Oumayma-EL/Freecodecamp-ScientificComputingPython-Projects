import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self,**balls):
    self.contents=list()
    for key,value in balls.items():
        for i in range(value):
            self.contents.append(key)
    print(self.contents)

  def draw(self, number_of_draws):
    list_balls_removed=list()
    if number_of_draws<=len(self.contents):
      contents_copy = copy.deepcopy(self.contents)
      for number in range(number_of_draws):
        ball_removed=random.choice(self.contents)
        # print(ball_removed)
        list_balls_removed.append(ball_removed)
        self.contents.remove(ball_removed)
      return  list_balls_removed
    else:
      list_balls_removed=self.contents
      self.contents=[]
      # print(self.contents)
      # print(list_balls_removed)
    return list_balls_removed



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  M=0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    counts = dict()
    drawn=hat_copy.draw(num_balls_drawn)
    for element in drawn:
      counts[element]=counts.get(element,0)+1
    # print(counts)
    s = 0

    for key,value in expected_balls.items():
      if key in counts.keys():
        if expected_balls[key]<=counts[key]:
          s+=1
    if s==len(expected_balls):
      M+=1
  #     print(s)
  # print("M",M)
  return M/num_experiments

