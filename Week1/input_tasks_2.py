robot_template = """
##########
#  {eye}  {eye}  #
#  ----  #
##########
"""

print("Please enter a character for the eye")
eye_char = input()
print("The robot's expression is now as follows:")
print(robot_template.format(eye=eye_char))
