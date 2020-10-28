### 2) Create a Module in Visual Studio Code and Import It <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a room <br>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

def sq_room(length,width):
    return int(length)*int(width)

from math import pi
def cir_circle(radius):
    return 2*int(pi)*int(radius)





