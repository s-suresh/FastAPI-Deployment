from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import joblib
#load the dataset
iris = load_iris()
X,y = iris.data, iris.target
#print(X.shape)
#it shows all 150 rows
#test-train split with approx ~=20% data is set for test and rest for train
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)
#print(X_test.shape,X_train.shape,y_test,y_train)
# random forest classifier
rf = RandomForestClassifier()
# fit the train data on to the model
rf.fit(X_train,y_train)
# we get accuracy=96.667% on the test data
accuracy= rf.score(X_test,y_test)
print("accuracy is: ",accuracy)

#save the model
joblib.dump(rf,"./model.pkl")