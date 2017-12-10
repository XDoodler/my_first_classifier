import mydataset
import matplotlib.pyplot as plt
from sklearn import tree
md=mydataset.load_my_fancy_dataset()
X=md.features
y=md.labels
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y)
print( "1=MALE")
print("0=FEMALE")

plt.text(160,44, 'blue dots=Male; Red dots=Female',
         fontsize=10)
plt.xlabel('weight')
plt.ylabel('height')
plt.axis([145,190,40,90])
plt.show();

print (clf.predict([[160,45]] ))

