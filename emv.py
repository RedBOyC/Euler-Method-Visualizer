import numpy as num
import matplotlib.pyplot as plt

dydx=input("Enter the dy/dy equation: ") #i.e dy/dy = x+y
x0=int(input("Enter initial x value: "))
y0=int(input("Enter initial y value: "))
n=int(input("Enter number of terms: "))
h=int(input("Enter the step size: "))
f=str(input("Enter the graph format: ")) #ro- gives red line with o for points and a solid line -
x_axis=str(input("Enter x-axis label: "))
y_axis=str(input("Enter y-axis label: "))


def f(x,y):
    return eval(dydx)

x_arr=np.arange(x0, (n+1)*h, h)
y_arr=np.zeros(n+1)
y_arr[0]=y0

for i in range(n):
    y_arr[i+1 ]= y_arr[i] + h*f(x_arr[i], y_arr[i])



##Plot
plt.plot(x_arr, y_arr, f, label="Euler approximation" )

plt.title("Euler method for"+dydx)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.legend()
plt.grid(True)

#Show plot
plt.show()
