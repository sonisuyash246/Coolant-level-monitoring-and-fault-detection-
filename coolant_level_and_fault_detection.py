# -*- coding: utf-8 -*-
"""coolant level and fault detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ghudrJEQQjXsVceCSNMHXLA1mWAXz5eF
"""

#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.svm as svc
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import mlxtend as ml
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from mlxtend.evaluate import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix

# In[82]:


data=pd.read_csv(r'/content/TrMLR.csv')
real_x=data.iloc[:,[0,1]].values
real_y=data.iloc[:,3].values
training_x,testing_x,training_y,testing_y=train_test_split(real_x,real_y,test_size=0.25,random_state=0)
s_c=StandardScaler()
training_x=s_c.fit_transform(training_x)
testing_x=s_c.fit_transform(testing_x)
cls_svc=SVC(kernel='linear',random_state=0)
cls_svc.fit(training_x,training_y)
y_pred=cls_svc.predict(testing_x)
testing_y=testing_y.tolist()
y_pred = y_pred.tolist()

gh=r2_score(testing_y,y_pred)

print('Accuracy is =' + str(gh))

# In[83]:




cm = confusion_matrix(y_target=testing_y, 
                      y_predicted=y_pred, 
                      binary=True, 
                      positive_label=1)
cm

fig, ax = plot_confusion_matrix(conf_mat=cm)
plt.show()
cm




from matplotlib.colors import ListedColormap

X_set, y_set = training_x,training_y
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))


plt.contourf(X1, X2,cls_svc.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(("red", "green")))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(("red", "black"))(i), label = j)

plt.title('SVM Training Set')
plt.xlabel('Coolentlevel-IsDroplet-Temperature')
plt.ylabel('Leakage Status')
plt.legend()
plt.show()

# In[84]:


from mpl_toolkits.mplot3d import Axes3D

# graph the data
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(testing_x[:, 0], testing_x[:, 1], testing_y,color='g',label='Actual Status')
ax.scatter(testing_x[:, 0], testing_x[:, 1], y_pred,color='r',label='predicted status')
ax.set_xlabel('Coolentlevel')
ax.set_ylabel('Temperature')
ax.set_zlabel('Leakage Status')


# In[ ]: