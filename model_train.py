from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import joblib

iris = load_iris()
X,y = iris.data, iris.target
#print(X.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)
#print(X_test.shape,X_train.shape,y_test,y_train)
rf = RandomForestClassifier()
rf.fit(X_train,y_train)
accuracy= rf.score(X_test,y_test)
print("accuracy is: ",accuracy)

#save the model
joblib.dump(rf,"./model.pkl")