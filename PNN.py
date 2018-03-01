import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

x = []
y = []
z = []
q = []
class0 = []
class1 = []
class2 = []

file = open('data_train_PNN.txt')

with open('data_train_PNN.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    z = [float(line.split()[2]) for line in lines]
    q = [int(line.split()[3]) for line in lines]

for i in range(len(q)) :
    # print(i)
    if (q[i] == 0):
        class0.append([x[i],y[i],z[i]])
    elif (q[i] == 1):
        class1.append([x[i],y[i],z[i]])
    elif (q[i] == 2):
        class2.append([x[i],y[i],z[i]])


fig = pyplot.figure()
ax = Axes3D(fig)


ax.set_xlabel("atribut 1")
ax.set_ylabel("atribut 2")
ax.set_zlabel("atribut 3")
for i in range(len(class0)):
    ax.scatter(class0[i][0], class0[i][1], class0[i][2], color='r')
    ax.scatter(class1[i][0], class1[i][1], class1[i][2], color='g')
    ax.scatter(class2[i][0], class2[i][1], class2[i][2], color='b')
pyplot.title('Visualisasi data training')
pyplot.show()

