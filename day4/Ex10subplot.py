import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0,5.0)
x2 = np.linspace(0.0,2.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2,1,2)
plt.plot(x2,y2,'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.tight_layout()
plt.show()

# x 좌표 공유, y 다름
fig, ax0 = plt.subplots()
ax1 = ax0.twinx()
ax0.set_title('twin y')
ax0.plot([10,5,2,9,7],'r-',label='y0')
ax0.set_ylabel('y0')
ax1.plot([100,200,220,180,120],'g:',label='y1')
ax1.set_ylabel('y1')
ax1.set_xlabel('x')
plt.show()
