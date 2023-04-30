import numpy as np
import matplotlib.pyplot as plt

def a_0():
    return 0
    pass

def a_n(n):
    return 0
    pass

def b_n(n):
    return ((2 * (1 - np.cos(n* np.pi)))/(np.pi * n))
    pass

def fouierSeries(x, n):
    f_x = a_0() 
    for i in range(1,n):
        f_x = f_x + a_n(i) * np.cos(i * x) + b_n(i) * np.sin(i * x)
    return(f_x)

# Set the time and frequency domain parameters
t_start = 0
t_stop = 10 * np.pi
num_samples = 1000
t = np.linspace(t_start, t_stop, num_samples)

# Plot the time domain function
plt.figure()
plt.plot(t, fouierSeries(t,10000))
plt.title('Time Domain: f(t)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.show()