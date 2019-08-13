import numpy as np

x = np.arange(6)
print("x   =", x)
print("x+5 =", x+5, "np.add()=", np.add(x, 5))
print("x-5 =", x-5, "np.subtract()=", np.subtract(x, 5))
print("x*2 =", x*2, "np.multiply()=", np.multiply(x, 2))
print("x/2 =", x/2, "np.divide()=", np.divide(x, 2))
print("x//2=", x//2, "np.floor_divide()=", np.floor_divide(x, 2))
print("-x  =", -x,  "np.negative()=", np.negative(x))
print("x**2=", x**2, "np.power()=", np.power(x, 2))
print("x%2=",  x % 2, "np.mod()=", np.mod(x, 2))

print("abs==================================================")
x = np.array([-1, 2, 3, 0, 44, -66])
print(abs(x))
print(np.absolute(x))
print(np.abs(x))

print("tan==================================================")
theta = np.linspace(0, np.pi, 3)
print("theta", theta)
print("sin", np.sin(theta))
print("cos", np.cos(theta))
print("tan", np.tan(theta))

print("arctan===============================================")
x = [-1, 0, 1]
print("x", x)
print("arcsin", np.arcsin(x))
print("arccos", np.arccos(x))
print("arctan", np.arctan(x))

print("指數、對數============================================")
x = [1, 2, 3]
print("x", x)
print("e^x", np.exp(x))
print("2^x", np.exp2(x))
print("3^x", np.power(x, 3))
print("ln(x)", np.log(x))
print("log2(x)", np.log2(x))
print("log10(x)", np.log10(x))
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))  