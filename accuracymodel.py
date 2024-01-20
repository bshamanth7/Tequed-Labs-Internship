
#this prints accuracy of the prediction
import numpy as np
import pandas as pd
#import matplotlib
import seaborn as sns
from sklearn.model_selection import train_test_split

zomato_orgnl=pd.read_csv("/home/kashi/Downloads/zomato.csv")
zomato=zomato_orgnl.drop(['url','dish_liked','phone'],axis=1)
zomato.duplicated().sum()
zomato.drop_duplicates(inplace=True)
zomato.isnull().sum()
zomato.dropna(how='any',inplace=True)
#change col names
zomato = zomato.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type','listed_in(city)':'city'})
zomato['cost'] = zomato['cost'].astype(str)
zomato['cost'] = zomato['cost'].apply(lambda x: x.replace(',','.'))
zomato['cost'] = zomato['cost'].astype(float)
zomato['rate'].unique()
#data cleaning by removing new,nan etc
zomato = zomato.loc[zomato.rate !='NEW']
zomato = zomato.loc[zomato.rate !='-'].reset_index(drop=True)
remove_slash = lambda x: x.replace('/5', '') if type(x) == np.str else x
zomato.rate = zomato.rate.apply(remove_slash).str.strip().astype('float')
zomato.name = zomato.name.apply(lambda x:x.title())
zomato.online_order.replace(('Yes','No'),(True, False),inplace=True)
zomato.book_table.replace(('Yes','No'),(True, False),inplace=True)
#encoding the cl
def Encode(zomato):
    for column in zomato.columns[~zomato.columns.isin(['rate', 'cost', 'votes'])]:
        zomato[column] = zomato[column].factorize()[0]
    return zomato
zomato_en = Encode(zomato.copy())
corr = zomato_en.corr(method='kendall')
#plt.figure(figsize=(15,8))
#sns.heatmap(corr, annot=True)
x = zomato_en.iloc[:,[2,3,5,6,7,8,9,11]]
y = zomato_en['rate']
#Getting Test and Training Set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=353)
#using extratree regressor model
from sklearn.ensemble import  ExtraTreesRegressor
ETree=ExtraTreesRegressor(n_estimators = 100)
ETree.fit(x_train,y_train)
y_predict=ETree.predict(x_test)
from sklearn.metrics import r2_score
print("accuracy ",r2_score(y_test,y_predict)*100)