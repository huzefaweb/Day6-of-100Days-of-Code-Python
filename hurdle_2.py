def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()

# ------- hurdle 2 ----------
while num_hurdles>0:
   jump()
   num_hurdles-=1
   if at_goal()==True:
      break
