import matplotlib.pyplot as plt
import numpy as np
import data_import
import euler

## Define the dimension of diffential equations
n = 3

## Define initial conditions of time and time-integration steps
t0 = 0.0
ti = 0.0
dt = 0.5
tmax = 40.0

# Initial conditions of chemical concentrations
x0 = [50.0, 0.0, 0.0]
xi = np.zeros(n)     ## This array will be the simulation result at each time-step, but it will be updated at each time-step

# Create dynamic array to store all the simulation results 
nrow = int((tmax - t0)/dt + 1)
j = 0
t_out = np.zeros((nrow))
x_out = np.zeros((nrow, n))

# Import the k1 and k2 from "Reaction rate constant csv file"
data_len = data_import.import_data()[0]
k1 = np.zeros(data_len)
k2 = np.zeros(data_len)
for i in range(data_len):
    k1[i] = data_import.import_data()[1][i]
    k2[i] = data_import.import_data()[2][i]


# Intergration to solve diffential equations
while ti <= tmax:

    j = j + 1
    
    for jj in range(data_len):
        ti = t0 + dt

        # Call Euler method to solve differential equations
        if(ti >= (jj-1) and ti <= jj):
            sim_euler = euler.euler_OEK(t0, ti, x0, xi, n, k1[jj], k2[jj])
            #print(ti, sim_euler[2][0], sim_euler[2][1], sim_euler[2][2])
            print(sim_euler[2][0] + sim_euler[2][1] + sim_euler[2][2])

            # Fill the time step into the dynamic array defined previously
            t_out[j-1] = ti

            # Fill the simulation results into the nrow * n array 
            for ii in range(n):
                x_out[j-1][ii] = sim_euler[2][ii]
    
            # Adjust the time step and initial conditions
            t0 = ti
            for i in range(0, n):
                xi[i] = sim_euler[2][i]
                x0[i] = xi[i]
        else:
            continue

plt.plot(t_out, x_out[:,0], color='red', marker='o')
plt.plot(t_out, x_out[:,1], color='red', marker='o')
plt.plot(t_out, x_out[:,2], color='green', marker='o')
plt.xlim(0, 41)
plt.ylim(0.1, 52)
plt.show()







