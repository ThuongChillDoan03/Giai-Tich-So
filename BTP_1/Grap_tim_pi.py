import numpy as np
import matplotlib.pyplot as plt

#Hàm f(x) - sửa một hàm bất kì mà bạn muốn
def f(x):
    return np.sin(x)

# Vẽ đồ thị hàm số
plt.xlabel("Giá trị x biến thiên")
plt.ylabel("Giá trị y biến thiên")
plt.title("Đồ thị hàm số của phương trình f(x) ")
x = np.linspace(3,3.5 , 1000)
plt.plot(x, f(x))
plt.plot(0, 0, '+')
plt.plot(0, )
plt.grid()
plt.show()