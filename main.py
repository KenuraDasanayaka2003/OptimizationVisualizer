#Importing necessary libraries
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#defining symbols
symbol_x = sp.Symbol('x')

#Getting user inputs for function
user_expr = input("Enter a function in terms of x (eg: x**2+4*x+4) : ")
expr = sp.sympify(user_expr)

#Converting the given function into numeric
f = sp.lambdify(symbol_x, expr,"numpy")

#defining the derivative
df_expr = sp.diff(expr,symbol_x)
df = sp.lambdify(symbol_x, df_expr,"numpy")

#asking a random point for x and a random value for alpha
x = float(input("Enter a value for x: "))
alpha = float(input("Enter a value for alpha: "))

points = []

#Defining the Gradient Descent loop
for i in range(30):
    points.append(x)

    grad = df(x)

    if abs(grad) < 1e-6:
        break

    x = x - alpha * grad

#Preparing the plot
fig, ax = plt.subplots()

#creating an array for x values
x_values = np.linspace(-10,10,100)

#Computing y values according to the function
y_values = f(x_values)

ax.plot(x_values, y_values)
text = ax.text(0,0,"")
point, = ax.plot([],[],'ro')

#Initializing the animation function
def init():
    point.set_data([],[])
    return point,text

#Defining the update function
def update(i):
    x = points[i]
    y = f(x)
    point.set_data([x],[y])
    text.set_position((x,y))
    text.set_text(f"x = {round(x,3)}")
    return point,text

#Running the animation
ani = (animation.FuncAnimation
(
    fig,
    update,
    frames=len(points),
    init_func=init,
    interval=500,
    blit=True
))
plt.show()
