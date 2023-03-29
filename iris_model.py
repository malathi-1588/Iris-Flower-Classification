# DataFlair Iris Flower Classification
# Import Packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pymysql as pms

# Load the data
df = pd.read_csv(r"D:\College Files\Flask Codes\IRIS\Iris.csv")

conn = pms.connect(host = 'localhost', port = 3306, user = 'root', password = 'Malathi5*', db = 'iris')
cursor = conn.cursor()

query_str = 'SELECT SepalLength, SepalWidth, PetalLength, PetalWidth, Species FROM iris.iris_data'
cursor.execute(query_str)
conn.commit()
result = cursor.fetchall()
df = pd.DataFrame(result)


# Separate features and target  
data = df.values
X = data[:,0:4]
Y = data[:,4]

# Split the data to train and test dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Support vector machine algorithm
from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, y_train)

# Predict from the test dataset
predictions = svn.predict(X_test)

# Calculate the accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

X_new = np.array([[7, 3, 6, 2]])
#Prediction of the species from the input vector
prediction=svn.predict(X_new)
print("Prediction of Species: ", prediction[0])

# Save the model
import pickle
with open('SVM.pickle', 'wb') as f:
    pickle.dump(svn, f)

# Load the model
with open('SVM.pickle', 'rb') as f:
    model = pickle.load(f)
model.predict(X_new)