'''
Created on 2018. 7. 30.

@author: user
'''
import tensorflow as tf
import matplotlib.pyplot as plt

x=[1,2,3]
y=[1,2,3]

w=tf.placeholder(tf.float32)
hypothesis=x*w

cost=tf.reduce_mean(tf.square(hypothesis-y))

sess=tf.Session()
sess.run(tf.global_variables_initializer())

W_val=[]
Cost_val=[]
for i in range(-30,50):
    feed_W=i*0.1
    curr_cost, curr_W=sess.run([cost,w],feed_dict={w:feed_W})
    W_val.append(curr_W)
    Cost_val.append(curr_cost)
    
plt.plot(W_val,Cost_val)
plt.show()