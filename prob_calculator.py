import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = []
    self.balls = balls
    for ball_color,ball_amount in self.balls.items():
      for i in range(ball_amount):
        self.contents.append(ball_color)
    print(self.contents)

  def draw(self, draw_amount):
    draw_list = []
    if draw_amount > len(self.contents):
      draw_list = self.contents
    else:
      for i in range(draw_amount):
        random_number = random.randint(0,len(self.contents)-1)
        random_color = self.contents[random_number]
        self.contents.remove(random_color)
        draw_list.append(random_color)
    return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  probability_count = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    count = 0
    drawn_balls = hat_copy.draw(num_balls_drawn)
    for expected_color,expected_value in expected_balls.items():
      if drawn_balls.count(expected_color) >= expected_value:
        count += 1
    if count == len(expected_balls):
      probability_count += 1
  probability_final = probability_count/num_experiments
  return probability_final
