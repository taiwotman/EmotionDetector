from scipy import misc 
import numpy as np 
import matplotlib.cm as cm 
import tensorflow as tf 
from matplotlib import pyplot as plt 
import matplotlib.image as mpimg 
import EmotionDetectorUtils 
from EmotionDetectorUtils import testResult 
 
 
def rgb2gray(rgb): 
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114]) 
 
img = mpimg.imread('Taiwo_Adetiloye.jpg')      
gray = rgb2gray(img) 
plt.imshow(gray, cmap = plt.get_cmap('gray')) 
plt.show() 
 
sess = tf.InteractiveSession() 
new_saver = tf.train.import_meta_graph('logs/model.ckpt-1000.meta') 
new_saver.restore(sess, 'logs/model.ckpt-1000') 
tf.get_default_graph().as_graph_def() 
x = sess.graph.get_tensor_by_name("input:0") 
y_conv = sess.graph.get_tensor_by_name("output:0") 
 
image_test = np.resize(gray,(1,48,48,1)) 
tResult = testResult() 
num_evaluations = 1000 
for i in range(0,num_evaluations): 
    result = sess.run(y_conv, feed_dict={x:image_test}) 
    label = sess.run(tf.argmax(result, 1)) 
    label = label[0] 
    label = int(label) 
    tResult.evaluate(label) 
 
tResult.display_result(num_evaluations) 