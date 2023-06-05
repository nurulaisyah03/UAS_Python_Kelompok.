#Machine Learning : Prediksi Penumpang yang Selamat di Kapal Titanic dengan Regresi
#Logistik dan K-Nearest Neighbors")

import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sb 

df=pd.read_csv('titanic_dataset.csv')
df

#menampilkan plot
import matplotlib.pyplot as plt

plt.scatter(df.Age, df.Survived, color='red', marker='o')
plt.show()

#metode ini mencetak informasi tentang DataFrame termasuk tipe data dan tipe kolom
#nilai-nilai non-null dan penggunaan memory
df.info()

#Isnull()
import matplotlib.pyplot as plt
print(df.isnull())

#Jumlah null pada kolom
print(df.isnull().sum())



#melihat data data kosong yang kosom pada kolom
sb.heatmap(df.isnull())
plt.show()

#Menghapus kolom kabin
df.drop('Cabin',axis=1,inplace=True)
print(df)


#Kolom age mengandung bebrapa nilai yang hilang 
#jadi tidak perlu menghapus satu kolom
df.dropna(inplace=True)
print(df)

sb.heatmap(df.isnull())
plt.show()

print(df.isnull().sum())

#Membuat model prediksi
import pandas as pd
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[['Age']],df.Survived,train_size=0.9)
print(x_test)
#menampilkan x_train
print(x_train)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)

model.predict((x_test))
model.score(x_test, y_test)
model.predict(([[43]]))

#KNN
from sklearn import neighbors
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[['Age']],df.Survived,train_size=0.9)
import math 
print (math.sqrt(891))

model_knn=neighbors.KNeighborsClassifier(n_neighbors=29)
model_knn.fit(x_train, y_train)

model_knn.score(x_test,y_test)
model_knn.predict(x_test)
model_knn.predict([[35]])
