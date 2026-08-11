#A simple app to perform the desired calculations in the console
def calculator():
   i = 0
   for x in operators:
      if x in expression:
        segments = expression.split(x)
        y = int(segments[0])
        z = int(segments[1])
        operators_in_action = [y*z, y^z, y/z, y*z, y+z, y-z]
        print(operators_in_action[i])

      i = i+1

operators = [")", "^", "/", "*", "+", "-"]


print("Hello, welcome to my Calculator App")


expression = input("input a mathmatical expression here >>>")

calculator()
