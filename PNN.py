import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import csv

x = []
y = []
z = []

with open('data_train_PNN.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    z = [float(line.split()[2]) for line in lines]

fig = pyplot.figure()
ax = Axes3D(fig)

ax.scatter(x, y, z)
pyplot.show()


# pyplot.scatter(x,y, label='skitscat', color='k', s=25, marker="o")
#
# pyplot.title('Visualisasi data training')
# pyplot.legend()
# pyplot.show()