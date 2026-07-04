import matplotlib.pyplot as plt
import numpy as np

# plt.subplot(2,1,1)
# xs = np.array([1,2,3,7,10])
# ys = np.array([12,32,12,32,12])

# plt.plot(xs,ys, marker='o', markersize=10, color='red', linestyle='dashed', linewidth=2, label='Line 1')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.subplot(2,1,2)
# xs = np.array([1,2,3,7,10])
# ys = np.array([9,22,12,19,17])
# plt.plot(xs,ys, marker='o', markersize=10, color='blue', linestyle='dashed', linewidth=2, label='Line 2')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # plt.show()

xs = np.array([1,2,3,7,10])
ys = np.array([9,22,12,19,17])

# plt.scatter(xs, ys, color='green', marker='o', s=100)

# plt.bar(xs, ys, color='orange', width=0.5)

# plt.barh(xs, ys, color='purple', height=0.5)

# plt.pie(ys, labels=xs, autopct='%1.1f%%', startangle=90, shadow=True, explode=(0.1, 0, 0, 0, 0), colors=['red', 'blue', 'green', 'orange', 'purple'])

sampling_f = 1000
t = np.linspace(0, 1, sampling_f)
f =5 
y = np.sin(2 * np.pi * f * t)
plt.figure(1)
plt.plot(t, y, color='blue', linewidth=2)
plt.grid(True)
plt.show()
plt.title
plt.figure(2)
square_wave = np.sign(y)
plt.plot(t, square_wave, color='red', linewidth=2)
plt.grid(True)
plt.show()


plt.figure(3)
plt.stem(t,y)
plt.show()