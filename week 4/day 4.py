
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
data=pd.read_csv('income.csv')
data.head()

# no -->pay 
# yes --> not pay
default	student	balance	income
0	No	No	729.526495	44361.625074
1	No	Yes	817.180407	12106.134700
2	No	No	1073.549164	31767.138947
3	No	No	529.250605	35704.493935
4	No	No	785.655883	38463.495879
data.shape
(10000, 4)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.boxplot(y=data['balance'])
plt.subplot(1,2,2)
sns.boxplot(y=data['income'])
plt.show()

data.describe()
balance	income
count	10000.000000	10000.000000
mean	835.374886	33516.981876
std	483.714985	13336.639563
min	0.000000	771.967729
25%	481.731105	21340.462903
50%	823.636973	34552.644802
75%	1166.308386	43807.729272
max	2654.322576	73554.233495
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(data['student'])
plt.subplot(1,2,2)
sns.countplot(data['default'])
plt.show()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[143], line 3
      1 plt.figure(figsize=(15,5))
      2 plt.subplot(1,2,1)
----> 3 sns.countplot(data['student'])
      4 plt.subplot(1,2,2)
      5 sns.countplot(data['default'])

File D:\Anaconda\Lib\site-packages\seaborn\categorical.py:2943, in countplot(data, x, y, hue, order, hue_order, orient, color, palette, saturation, width, dodge, ax, **kwargs)
   2940 elif x is not None and y is not None:
   2941     raise ValueError("Cannot pass values for both `x` and `y`")
-> 2943 plotter = _CountPlotter(
   2944     x, y, hue, data, order, hue_order,
   2945     estimator, errorbar, n_boot, units, seed,
   2946     orient, color, palette, saturation,
   2947     width, errcolor, errwidth, capsize, dodge
   2948 )
   2950 plotter.value_label = "count"
   2952 if ax is None:

File D:\Anaconda\Lib\site-packages\seaborn\categorical.py:1530, in _BarPlotter.__init__(self, x, y, hue, data, order, hue_order, estimator, errorbar, n_boot, units, seed, orient, color, palette, saturation, width, errcolor, errwidth, capsize, dodge)
   1525 def __init__(self, x, y, hue, data, order, hue_order,
   1526              estimator, errorbar, n_boot, units, seed,
   1527              orient, color, palette, saturation, width,
   1528              errcolor, errwidth, capsize, dodge):
   1529     """Initialize the plotter."""
-> 1530     self.establish_variables(x, y, hue, data, orient,
   1531                              order, hue_order, units)
   1532     self.establish_colors(color, palette, saturation)
   1533     self.estimate_statistic(estimator, errorbar, n_boot, seed)

File D:\Anaconda\Lib\site-packages\seaborn\categorical.py:516, in _CategoricalPlotter.establish_variables(self, x, y, hue, data, orient, order, hue_order, units)
    513     plot_data = data
    515 # Convert to a list of arrays, the common representation
--> 516 plot_data = [np.asarray(d, float) for d in plot_data]
    518 # The group names will just be numeric indices
    519 group_names = list(range(len(plot_data)))

File D:\Anaconda\Lib\site-packages\seaborn\categorical.py:516, in <listcomp>(.0)
    513     plot_data = data
    515 # Convert to a list of arrays, the common representation
--> 516 plot_data = [np.asarray(d, float) for d in plot_data]
    518 # The group names will just be numeric indices
    519 group_names = list(range(len(plot_data)))

File D:\Anaconda\Lib\site-packages\pandas\core\series.py:953, in Series.__array__(self, dtype)
    906 """
    907 Return the values as a NumPy array.
    908 
   (...)
    950       dtype='datetime64[ns]')
    951 """
    952 values = self._values
--> 953 arr = np.asarray(values, dtype=dtype)
    954 if using_copy_on_write() and astype_is_view(values.dtype, arr.dtype):
    955     arr = arr.view()

ValueError: could not convert string to float: 'No'

data['student'].value_counts()
student
No     7056
Yes    2944
Name: count, dtype: int64
data['default'].value_counts()
default
No     9667
Yes     333
Name: count, dtype: int64
data['student'].value_counts(normalize=True)
student
No     0.7056
Yes    0.2944
Name: proportion, dtype: float64
# percentange
data['default'].value_counts(normalize=True)
default
No     0.9667
Yes    0.0333
Name: proportion, dtype: float64
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.boxplot(x=data['default'], y=data['balance'] , data=data)
plt.subplot(1,2,2)
sns.boxplot(x=data['default'],y=data['income'], data=data)
plt.show()

pd.crosstab(data['student'], data['default'],normalize='index').round(2)
default	No	Yes
student		
No	0.97	0.03
Yes	0.96	0.04
#pd.crosstab(data['balance'], data['income'],normalize='index').round(2)
sns.heatmap(data[['balance','income']].corr() , annot=True)
<Axes: >

data.isnull().sum()
default    0
student    0
balance    0
income     0
dtype: int64
q1,q3=data['balance'].quantile([.25,.75])
q1
481.731105054518
q3
1166.3083864758376
IQR=(q3-q1)
lower=q1-1.5*(IQR)
upper=q3+1.5*(IQR)
lower
-545.1348170774612
upper
2193.174308607817
df=data[data['balance']>lower]
df
default	student	balance	income
0	No	No	729.526495	44361.625074
1	No	Yes	817.180407	12106.134700
2	No	No	1073.549164	31767.138947
3	No	No	529.250605	35704.493935
4	No	No	785.655883	38463.495879
...	...	...	...	...
9995	No	No	711.555020	52992.378914
9996	No	No	757.962918	19660.721768
9997	No	No	845.411989	58636.156984
9998	No	No	1569.009053	36669.112365
9999	No	Yes	200.922183	16862.952321
10000 rows × 4 columns

df['default'].count()
10000
df['default'].value_counts(normalize=True)
default
No     0.9667
Yes    0.0333
Name: proportion, dtype: float64
df['default'].value_counts()
default
No     9667
Yes     333
Name: count, dtype: int64
data['balance']=np.where(data['balance']>upper,upper, data['balance'])      # 
sns.boxplot(y=data['balance'])
plt.show()

# categories ==>[0,1] false , true
data=pd.get_dummies(data,drop_first=True)
data.head()
balance	income	default_Yes	student_Yes
0	729.526495	44361.625074	False	False
1	817.180407	12106.134700	False	True
2	1073.549164	31767.138947	False	False
3	529.250605	35704.493935	False	False
4	785.655883	38463.495879	False	False
data.columns=['balance','income','default','student']
data.head()
balance	income	default	student
0	729.526495	44361.625074	False	False
1	817.180407	12106.134700	False	True
2	1073.549164	31767.138947	False	False
3	529.250605	35704.493935	False	False
4	785.655883	38463.495879	False	False
from sklearn.model_selection import train_test_split
x=data.drop('default',axis=1)  #independent

#x=data[['balance','income','student']]
y=data['default']    #dependent
x.head()
balance	income	student
0	729.526495	44361.625074	False
1	817.180407	12106.134700	True
2	1073.549164	31767.138947	False
3	529.250605	35704.493935	False
4	785.655883	38463.495879	False
y.head()
0    False
1    False
2    False
3    False
4    False
Name: default, dtype: bool
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=21,stratify=y)
# stratify ==> balanced data when there is imbalanced data 
x_train.shape
(7000, 3)
x_test.shape
(3000, 3)
print(y_train.value_counts(normalize=True).round(2))
default
False    0.97
True     0.03
Name: proportion, dtype: float64
y_test.value_counts(normalize=True).round(2)
default
False    0.97
True     0.03
Name: proportion, dtype: float64
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
LogisticRegression()
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
y_pred=lr.predict(x_test)
y_pred[0:5]
array([False, False, False, False, False])
y_test.head()
1071    False
9106    False
501     False
6475    False
5943    False
Name: default, dtype: bool
#from sklearn.metrics import mean_squere_error  => linear Regression


# logistic Regression ==> confusion matrix
from sklearn.metrics import confusion_matrix 
confusion_matrix(y_test,y_pred)
 
