import pandas as pd
import matplotlib.pyplot as plt

data = {'Length':['1', '2', '3', '4'], 'Crack Time':[0.001, 0.01, 0.1, 1]} 
df = pd.DataFrame(data, columns=['Length', 'Crack Time']) 
df.plot(x="Length", y="Crack Time", kind="line")
plt.show()

# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import style
# style.use('ggplot')

# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')

# x3 = [1,2,3,4,5,6,7,8,9,10]
# y3 = [1,2,3,4,5,6,7,8,9,10]
# z3 = [1,2,3,4,5,6,7,8,9,10]

# dx = np.ones(10)
# dy = np.ones(10)
# dz = [0.0000005,0.00000963,0.00482373,0.07647466,2.09032659,10,20,100,500,2000]

# ax1.bar3d(x3, y3, z3, dx, dy, dz)


# ax1.set_xlabel('Password Length')
# ax1.set_ylabel('Algorithm Type')
# ax1.set_zlabel('Cracking Time')

# plt.show()