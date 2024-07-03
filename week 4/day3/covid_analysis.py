
import pandas as pd
import datetime as dt
import numpy as np
# import seaborn as sns
from matpotlib import pyplot as plt 
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[9], line 5
      3 import numpy as np
      4 # import seaborn as sns
----> 5 from matpotlib import pyplot as plt

ModuleNotFoundError: No module named 'matpotlib'
df=pd.read_csv('covid_19_india.csv' , parse_dates=['Date'] , dayfirst=True)

df
C:\Users\Dell\AppData\Local\Temp\ipykernel_6552\440397583.py:1: UserWarning: Parsing dates in %Y-%m-%d format when dayfirst=True was specified. Pass `dayfirst=False` or specify a format to silence this warning.
  df=pd.read_csv('covid_19_india.csv' , parse_dates=['Date'] , dayfirst=True)
Sno	Date	Time	State/UnionTerritory	ConfirmedIndianNational	ConfirmedForeignNational	Cured	Deaths	Confirmed
0	1	2020-01-30	6:00 PM	Kerala	1	0	0	0	1
1	2	2020-01-31	6:00 PM	Kerala	1	0	0	0	1
2	3	2020-02-01	6:00 PM	Kerala	2	0	0	0	2
3	4	2020-02-02	6:00 PM	Kerala	3	0	0	0	3
4	5	2020-02-03	6:00 PM	Kerala	3	0	0	0	3
...	...	...	...	...	...	...	...	...	...
18105	18106	2021-08-11	8:00 AM	Telangana	-	-	638410	3831	650353
18106	18107	2021-08-11	8:00 AM	Tripura	-	-	77811	773	80660
18107	18108	2021-08-11	8:00 AM	Uttarakhand	-	-	334650	7368	342462
18108	18109	2021-08-11	8:00 AM	Uttar Pradesh	-	-	1685492	22775	1708812
18109	18110	2021-08-11	8:00 AM	West Bengal	-	-	1506532	18252	1534999
18110 rows × 9 columns

#  python -m notebook

df=df[['Date','State/UnionTerritory','Cured','Confirmed','Deaths' ]]
# data['ConfirmedIndianNational']

df
Date	State/UnionTerritory	Cured	Confirmed	Deaths
0	2020-01-30	Kerala	0	1	0
1	2020-01-31	Kerala	0	1	0
2	2020-02-01	Kerala	0	2	0
3	2020-02-02	Kerala	0	3	0
4	2020-02-03	Kerala	0	3	0
...	...	...	...	...	...
18105	2021-08-11	Telangana	638410	650353	3831
18106	2021-08-11	Tripura	77811	80660	773
18107	2021-08-11	Uttarakhand	334650	342462	7368
18108	2021-08-11	Uttar Pradesh	1685492	1708812	22775
18109	2021-08-11	West Bengal	1506532	1534999	18252
18110 rows × 5 columns

df.head()
Date	State/UnionTerritory	Cured	Confirmed	Deaths
0	2020-01-30	Kerala	0	1	0
1	2020-01-31	Kerala	0	1	0
2	2020-02-01	Kerala	0	2	0
3	2020-02-02	Kerala	0	3	0
4	2020-02-03	Kerala	0	3	0
#df=df[['Date','State/UnionTerritory','Cured','Confirmed','Deaths'] ]

df['Date']
0       2020-01-30
1       2020-01-31
2       2020-02-01
3       2020-02-02
4       2020-02-03
           ...    
18105   2021-08-11
18106   2021-08-11
18107   2021-08-11
18108   2021-08-11
18109   2021-08-11
Name: Date, Length: 18110, dtype: datetime64[ns]
df.columns=['date','state','cured','confirmed','deaths' ]
df.head()
date	state	cured	confirmed	deaths
0	2020-01-30	Kerala	0	1	0
1	2020-01-31	Kerala	0	1	0
2	2020-02-01	Kerala	0	2	0
3	2020-02-02	Kerala	0	3	0
4	2020-02-03	Kerala	0	3	0
df.tail()
date	state	cured	confirmed	deaths
18105	2021-08-11	Telangana	638410	650353	3831
18106	2021-08-11	Tripura	77811	80660	773
18107	2021-08-11	Uttarakhand	334650	342462	7368
18108	2021-08-11	Uttar Pradesh	1685492	1708812	22775
18109	2021-08-11	West Bengal	1506532	1534999	18252
today=df[df.date=='2020-07-17']
today
date	state	cured	confirmed	deaths
4179	2020-07-17	Andaman and Nicobar Islands	133	180	0
4180	2020-07-17	Andhra Pradesh	19393	38044	492
4181	2020-07-17	Arunachal Pradesh	153	543	3
4182	2020-07-17	Assam	12888	19754	48
4183	2020-07-17	Bihar	14018	21764	197
4184	2020-07-17	Chandigarh	476	651	11
4185	2020-07-17	Chhattisgarh	3451	4732	21
4186	2020-07-17	Dadra and Nagar Haveli and Daman and Diu	371	552	2
4187	2020-07-17	Delhi	97693	118645	3545
4188	2020-07-17	Goa	1817	3108	19
4189	2020-07-17	Gujarat	32103	45481	2089
4190	2020-07-17	Haryana	18185	24002	322
4191	2020-07-17	Himachal Pradesh	984	1377	11
4192	2020-07-17	Jammu and Kashmir	6446	12156	222
4193	2020-07-17	Jharkhand	2513	4624	42
4194	2020-07-17	Karnataka	19729	51422	1032
4195	2020-07-17	Kerala	4862	10275	37
4196	2020-07-17	Ladakh	970	1147	1
4197	2020-07-17	Madhya Pradesh	14127	20378	689
4198	2020-07-17	Maharashtra	158140	284281	11194
4199	2020-07-17	Manipur	1129	1764	0
4200	2020-07-17	Meghalaya	66	377	2
4201	2020-07-17	Mizoram	160	272	0
4202	2020-07-17	Nagaland	391	916	0
4203	2020-07-17	Odisha	10877	15392	79
4204	2020-07-17	Puducherry	947	1743	22
4205	2020-07-17	Punjab	6277	9094	230
4206	2020-07-17	Rajasthan	19970	27174	538
4207	2020-07-17	Sikkim	88	243	0
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4209	2020-07-17	Telengana	27295	41018	396
4210	2020-07-17	Tripura	1604	2283	3
4211	2020-07-17	Uttarakhand	2995	3982	50
4212	2020-07-17	Uttar Pradesh	26675	43441	1046
4213	2020-07-17	West Bengal	21415	36117	1023
4214	2020-07-17	Cases being reassigned to states	0	531	0
max_confirmed_cases=case=today.sort_values(by='confirmed',ascending=False)

#ascending =True
max_confirmed_cases
date	state	cured	confirmed	deaths
4198	2020-07-17	Maharashtra	158140	284281	11194
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4187	2020-07-17	Delhi	97693	118645	3545
4194	2020-07-17	Karnataka	19729	51422	1032
4189	2020-07-17	Gujarat	32103	45481	2089
4212	2020-07-17	Uttar Pradesh	26675	43441	1046
4209	2020-07-17	Telengana	27295	41018	396
4180	2020-07-17	Andhra Pradesh	19393	38044	492
4213	2020-07-17	West Bengal	21415	36117	1023
4206	2020-07-17	Rajasthan	19970	27174	538
4190	2020-07-17	Haryana	18185	24002	322
4183	2020-07-17	Bihar	14018	21764	197
4197	2020-07-17	Madhya Pradesh	14127	20378	689
4182	2020-07-17	Assam	12888	19754	48
4203	2020-07-17	Odisha	10877	15392	79
4192	2020-07-17	Jammu and Kashmir	6446	12156	222
4195	2020-07-17	Kerala	4862	10275	37
4205	2020-07-17	Punjab	6277	9094	230
4185	2020-07-17	Chhattisgarh	3451	4732	21
4193	2020-07-17	Jharkhand	2513	4624	42
4211	2020-07-17	Uttarakhand	2995	3982	50
4188	2020-07-17	Goa	1817	3108	19
4210	2020-07-17	Tripura	1604	2283	3
4199	2020-07-17	Manipur	1129	1764	0
4204	2020-07-17	Puducherry	947	1743	22
4191	2020-07-17	Himachal Pradesh	984	1377	11
4196	2020-07-17	Ladakh	970	1147	1
4202	2020-07-17	Nagaland	391	916	0
4184	2020-07-17	Chandigarh	476	651	11
4186	2020-07-17	Dadra and Nagar Haveli and Daman and Diu	371	552	2
4181	2020-07-17	Arunachal Pradesh	153	543	3
4214	2020-07-17	Cases being reassigned to states	0	531	0
4200	2020-07-17	Meghalaya	66	377	2
4201	2020-07-17	Mizoram	160	272	0
4207	2020-07-17	Sikkim	88	243	0
4179	2020-07-17	Andaman and Nicobar Islands	133	180	0
top_states_confirmed=max_confirmed_cases[0:5]
top_states_confirmed
date	state	cured	confirmed	deaths
4198	2020-07-17	Maharashtra	158140	284281	11194
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4187	2020-07-17	Delhi	97693	118645	3545
4194	2020-07-17	Karnataka	19729	51422	1032
4189	2020-07-17	Gujarat	32103	45481	2089
import seaborn as sns
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='confirmed', data=top_states_confirmed , hue='state')
plt.show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[40], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.barplot(x='state',y='confirmed', data=top_states_confirmed , hue='state')
----> 3 plt.show()

NameError: name 'plt' is not defined

max_death_cases=today.sort_values(by='deaths', ascending=False)
max_death_cases
date	state	cured	confirmed	deaths
4198	2020-07-17	Maharashtra	158140	284281	11194
4187	2020-07-17	Delhi	97693	118645	3545
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4189	2020-07-17	Gujarat	32103	45481	2089
4212	2020-07-17	Uttar Pradesh	26675	43441	1046
4194	2020-07-17	Karnataka	19729	51422	1032
4213	2020-07-17	West Bengal	21415	36117	1023
4197	2020-07-17	Madhya Pradesh	14127	20378	689
4206	2020-07-17	Rajasthan	19970	27174	538
4180	2020-07-17	Andhra Pradesh	19393	38044	492
4209	2020-07-17	Telengana	27295	41018	396
4190	2020-07-17	Haryana	18185	24002	322
4205	2020-07-17	Punjab	6277	9094	230
4192	2020-07-17	Jammu and Kashmir	6446	12156	222
4183	2020-07-17	Bihar	14018	21764	197
4203	2020-07-17	Odisha	10877	15392	79
4211	2020-07-17	Uttarakhand	2995	3982	50
4182	2020-07-17	Assam	12888	19754	48
4193	2020-07-17	Jharkhand	2513	4624	42
4195	2020-07-17	Kerala	4862	10275	37
4204	2020-07-17	Puducherry	947	1743	22
4185	2020-07-17	Chhattisgarh	3451	4732	21
4188	2020-07-17	Goa	1817	3108	19
4191	2020-07-17	Himachal Pradesh	984	1377	11
4184	2020-07-17	Chandigarh	476	651	11
4181	2020-07-17	Arunachal Pradesh	153	543	3
4210	2020-07-17	Tripura	1604	2283	3
4200	2020-07-17	Meghalaya	66	377	2
4186	2020-07-17	Dadra and Nagar Haveli and Daman and Diu	371	552	2
4196	2020-07-17	Ladakh	970	1147	1
4179	2020-07-17	Andaman and Nicobar Islands	133	180	0
4207	2020-07-17	Sikkim	88	243	0
4202	2020-07-17	Nagaland	391	916	0
4201	2020-07-17	Mizoram	160	272	0
4199	2020-07-17	Manipur	1129	1764	0
4214	2020-07-17	Cases being reassigned to states	0	531	0
top_states_death=max_death_cases[0:5]

top_states_death
date	state	cured	confirmed	deaths
4198	2020-07-17	Maharashtra	158140	284281	11194
4187	2020-07-17	Delhi	97693	118645	3545
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4189	2020-07-17	Gujarat	32103	45481	2089
4212	2020-07-17	Uttar Pradesh	26675	43441	1046
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='deaths', data=top_states_death , hue='state')
plt.show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[84], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.barplot(x='state',y='deaths', data=top_states_death , hue='state')
----> 3 plt.show()

NameError: name 'plt' is not defined

max_cured_cases=today.sort_values(by='cured', ascending=False)
max_cured_cases
date	state	cured	confirmed	deaths
4198	2020-07-17	Maharashtra	158140	284281	11194
4208	2020-07-17	Tamil Nadu	107416	156369	2236
4187	2020-07-17	Delhi	97693	118645	3545
4189	2020-07-17	Gujarat	32103	45481	2089
4209	2020-07-17	Telengana	27295	41018	396
4212	2020-07-17	Uttar Pradesh	26675	43441	1046
4213	2020-07-17	West Bengal	21415	36117	1023
4206	2020-07-17	Rajasthan	19970	27174	538
4194	2020-07-17	Karnataka	19729	51422	1032
4180	2020-07-17	Andhra Pradesh	19393	38044	492
4190	2020-07-17	Haryana	18185	24002	322
4197	2020-07-17	Madhya Pradesh	14127	20378	689
4183	2020-07-17	Bihar	14018	21764	197
4182	2020-07-17	Assam	12888	19754	48
4203	2020-07-17	Odisha	10877	15392	79
4192	2020-07-17	Jammu and Kashmir	6446	12156	222
4205	2020-07-17	Punjab	6277	9094	230
4195	2020-07-17	Kerala	4862	10275	37
4185	2020-07-17	Chhattisgarh	3451	4732	21
4211	2020-07-17	Uttarakhand	2995	3982	50
4193	2020-07-17	Jharkhand	2513	4624	42
4188	2020-07-17	Goa	1817	3108	19
4210	2020-07-17	Tripura	1604	2283	3
4199	2020-07-17	Manipur	1129	1764	0
4191	2020-07-17	Himachal Pradesh	984	1377	11
4196	2020-07-17	Ladakh	970	1147	1
4204	2020-07-17	Puducherry	947	1743	22
4184	2020-07-17	Chandigarh	476	651	11
4202	2020-07-17	Nagaland	391	916	0
4186	2020-07-17	Dadra and Nagar Haveli and Daman and Diu	371	552	2
4201	2020-07-17	Mizoram	160	272	0
4181	2020-07-17	Arunachal Pradesh	153	543	3
4179	2020-07-17	Andaman and Nicobar Islands	133	180	0
4207	2020-07-17	Sikkim	88	243	0
4200	2020-07-17	Meghalaya	66	377	2
4214	2020-07-17	Cases being reassigned to states	0	531	0
max_states_cured=max_cured_cases[0:5]
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='cured', data=top_states_death , hue='state')
plt.show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[92], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.barplot(x='state',y='cured', data=top_states_death , hue='state')
----> 3 plt.show()

NameError: name 'plt' is not defined

maha=df[df.state=='Maharashtra']
maha
date	state	cured	confirmed	deaths
76	2020-03-09	Maharashtra	0	2	0
91	2020-03-10	Maharashtra	0	5	0
97	2020-03-11	Maharashtra	0	2	0
120	2020-03-12	Maharashtra	0	11	0
133	2020-03-13	Maharashtra	0	14	0
...	...	...	...	...	...
17950	2021-08-07	Maharashtra	6130137	6341759	133717
17986	2021-08-08	Maharashtra	6139493	6347820	133845
18022	2021-08-09	Maharashtra	6144388	6353328	133996
18058	2021-08-10	Maharashtra	6151956	6357833	134064
18094	2021-08-11	Maharashtra	6159676	6363442	134201
520 rows × 5 columns

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed', data=maha , hue='state')
plt.show()
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[98], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.lineplot(x='date',y='confirmed', data=maha , hue='state')
----> 3 plt.show()

NameError: name 'plt' is not defined

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths', data=maha  )
plt.show()
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[100], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.lineplot(x='date',y='deaths', data=maha  )
----> 3 plt.show()

NameError: name 'plt' is not defined

delhi=df[df.state=='Delhi']
delhi
date	state	cured	confirmed	deaths
34	2020-03-02	Delhi	0	1	0
38	2020-03-03	Delhi	0	1	0
42	2020-03-04	Delhi	0	1	0
45	2020-03-05	Delhi	0	2	0
51	2020-03-06	Delhi	0	3	0
...	...	...	...	...	...
17938	2021-08-07	Delhi	1411042	1436623	25065
17974	2021-08-08	Delhi	1411064	1436695	25066
18010	2021-08-09	Delhi	1411159	1436761	25066
18046	2021-08-10	Delhi	1411235	1436800	25067
18082	2021-08-11	Delhi	1411280	1436852	25068
528 rows × 5 columns

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed', data=delhi , hue='state')
plt.show()
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[61], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.lineplot(x='date',y='confirmed', data=delhi , hue='state')
----> 3 plt.show()

NameError: name 'plt' is not defined

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths', data=delhi  )
plt.show()
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
D:\Anaconda\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[63], line 3
      1 sns.set(rc={'figure.figsize':(15,10)})
      2 sns.lineplot(x='date',y='deaths', data=delhi  )
----> 3 plt.show()

NameError: name 'plt' is not defined

from sklearn.model_selection import train_test_split
pip install sklearn
Collecting sklearn
  Downloading sklearn-0.0.post12.tar.gz (2.6 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'error'
Note: you may need to restart the kernel to use updated packages.
  error: subprocess-exited-with-error
  
  python setup.py egg_info did not run successfully.
  exit code: 1
  
  [15 lines of output]
  The 'sklearn' PyPI package is deprecated, use 'scikit-learn'
  rather than 'sklearn' for pip commands.
  
  Here is how to fix this error in the main use cases:
  - use 'pip install scikit-learn' rather than 'pip install sklearn'
  - replace 'sklearn' by 'scikit-learn' in your pip requirements files
    (requirements.txt, setup.py, setup.cfg, Pipfile, etc ...)
  - if the 'sklearn' package is used by one of your dependencies,
    it would be great if you take some time to track which package uses
    'sklearn' instead of 'scikit-learn' and report it to their issue tracker
  - as a last resort, set the environment variable
    SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True to avoid this error
  
  More information is available at
  https://github.com/scikit-learn/sklearn-pypi-package
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
from sklearn.model_selection import train_test_split
# maharastra ==> top  (data analysisP) 

# predict ===> 
x=maha['date']    # independent veriable
y=maha['confirmed']   #dependent 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
x_train
7525    2020-10-20
1175    2020-04-21
18058   2021-08-10
1921    2020-05-14
1592    2020-05-04
           ...    
2255    2020-05-24
4690    2020-07-31
8645    2020-11-21
17014   2021-07-12
10102   2021-01-01
Name: date, Length: 364, dtype: datetime64[ns]
y_train
7525     1601365
1175        4669
18058    6357833
1921       25922
1592       12974
          ...   
2255       47190
4690      411798
8645     1768695
17014    6157799
10102    1932112
Name: confirmed, Length: 364, dtype: int64
lr.fit(np.array(x_train).reshape(-1,1),np.array(x_train).reshape(-1,1))
LinearRegression()
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
LinearRegression(copy_X=True,fit_intercept=True, n_jobs=None)
lr.predict(np.array([[2020-7-19]]))
 
