'''
Created on 2018. 7. 25.

@author: user
'''
import tensorflow as t
hello=t.constant("Hello tensorflow")
sess=t.Session()
print(sess.run(hello))