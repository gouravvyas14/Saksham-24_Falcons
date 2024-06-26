import pandas as pd 
import seaborn as sns
import sklearn 

#  Standerlization 
from sklearn.preprocesing import StandardScaler

# normalization
from sklearn.preprocesing import MinMaxScaler

# will work only numerical value 

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()


df2=df[['survived','pclass' ,'age','parch']]

df2.head()

# forfilling value in excel original file
df3=df2.fillna(df2.mean())

df3.head()


x=df3[["pclass","age" ,"parch"]]  # independent
y=df2[['survived']].fillna(df2.mean())  # dependend
# y=df3.iloc[:,0:0]

#x
y

x.shape

y.shape

from sklearn.model_selection import train_test_split

# training ==> 70 %
# testing data ==>30 %

x_train ,x_test, y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=51)


x_train

x_train.shape

x_test
x_test.shape

y_train
y_train.shape

y_test
y_test.shape


# creating a object

sc=StandardScaler()

sc.fit(x_train)

# fit is use to the value fill in model 

sc.mean_
# we have three feature find out mean value

sc.scale_
# for checking array scale value 

x_train.describe()
# describe is use to whole dattaset 

x1_scalled=sc.transform(x_train)
x2_scalled=sc.transform(x_test)

x1_scalled

x2_scalled.head()


x_train_sclval=pd.DataFrame(x1_scalled)
x_train_sclval.head()
# for seeing in 2dimensional table form 

x_train_sclval.describe().round(5)


x_test_sclval=pd.DataFrame(x2_scalled)
x_test_sclval.head()

x_test_sclval.describe()


# ================normalizaion =====================#

from sklearn.preprocessing import MinMaxScaler

mnc=MinMaxScaler()

mnc.fit(x_train)

x_train_min=mnc.transform(x_train)
x_test_min=mnc.transform(x_test)

x_train_min

x_test_min

data1=pd.DataFrame(x_train_min)
data2=pd.DataFrame(x_test_min)

data1.describe()

data2.describe().round(5)
