import pandas as pd #work with data
import numpy as np #use number matrices
import matplotlib.pyplot as plt
import tensorflow as tf


dataframe=pd.read_csv('data.csv')
#print(dataframe.columns.values)
dataframe=dataframe.drop(['index','price','sq_price'], axis=1)
#print(dataframe.columns.values)

dataframe=dataframe[0:10]
#print(dataframe)

#Steps 2 -add labels
#1 is good and 0 is bad
dataframe.loc[:,('y1')]=[1,1,1,0,0,1,0,1,1,1]
dataframe.loc[:,('y2')]=dataframe['y1']==0
#print(dataframe)
dataframe.loc[:,('y2')]=dataframe['y2'].astype(int)
#print(dataframe)


#Steps 3 - Prepare data for tensorflow
#convert features to input tenson
inputX=dataframe.loc[:, ['area' ,'bathroom']].as_matrix()
#convert labels to input tensors
inputY=dataframe.loc[:,['y1','y2']].as_matrix()


#Steps 4 write out hyperparameters
learning_rate =0.000001
training_epochs =2000
display_step =50
n_samples=inputY.size


#Step 5 Create computational graph
x=tf.placeholder(tf.float32,[None,2])

#Create weights
#2*2

W=tf.Variable(tf.zeros([2,2]))

#add biases

b=tf.Variable(tf.zeros([2])

#multiply our weights
# mutply input by weight and add biases
xxx = tf.matmul(x, W)
y_values = tf.add(xxx, b)  

#apply softmmax
y=tf.nn.softmax(y_values)

#Feed in a matrix of labels
y_=tf.placeholder(tf.float32,)


#Step 6 Perform traing
#Create cost function, mean squared error
cost=tf.reduce_sum(tf.pow(y_ -y,2))/(2*n_samples)

#Gradient descent
optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimise(cost)


#initialise variable and tensorflow session

init =tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)


#training lloop

for i in range (training_epochs):
	sess.run(optimizer,feed_dict=(x:inputX,y_:inputY))

	if(i)%display_step==0:
		cc=sess.run(cost,feed_dict(x:inputX,y_:inputY))
		print('training steps')

print "Optimization Finished!"
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print "Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n'		