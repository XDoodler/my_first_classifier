import mydataset
from sklearn import tree
md=mydataset.load_my_fancy_dataset()
X=md.features
y=md.labels
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y)
print( "1=MALE")
print("0=FEMALE")
print (clf.predict([[178, 78]] ))

