import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

zomato_orgnl=pd.read_csv("/home/kashi/Downloads/zomato.csv")
#zomato_orgnl.head()
#calling this method from file3.py
def predictmodel():
    #cleaning data
    zomato=zomato_orgnl.drop(['url','dish_liked','phone'],axis=1)
    zomato.duplicated().sum()
    zomato.drop_duplicates(inplace= True)
    zomato.isnull().sum()
    zomato.dropna(how='any',inplace= True)
    #changing col names

    zomato = zomato.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type','listed_in(city)':'city'})
    zomato['cost'] = zomato['cost'].astype(str)
    zomato['cost'] = zomato['cost'].apply(lambda x: x.replace(',','.'))
    zomato['cost'] = zomato['cost'].astype(float)
    #rating value cleaning
    zomato['rate'].unique()
    zomato = zomato.loc[zomato.rate !='NEW']
    zomato = zomato.loc[zomato.rate !='-'].reset_index(drop=True)
    remove_slash = lambda x: x.replace('/5', '') if type(x) == np.str else x
    zomato.rate = zomato.rate.apply(remove_slash).str.strip().astype('float')

    zomato.name = zomato.name.apply(lambda x:x.title())
    zomato.online_order.replace(('Yes','No'),(True, False),inplace=True)
    zomato.book_table.replace(('Yes','No'),(True, False),inplace=True)
    #zomato.cost.unique()
    def Encode(zomato):
        for column in zomato.columns[~zomato.columns.isin(['rate', 'cost', 'votes'])]:
            zomato[column] = zomato[column].factorize()[0]
        return zomato
    zomato_en = Encode(zomato.copy())
    corr = zomato_en.corr(method='kendall')
    #taking x,y
    x = zomato_en.iloc[:,[2,3,5,6,7,8,9,11]]
    y = zomato['name']
    #giving values to predict the restaurant by giving encoded values here in data

    #You can change ths data values to get different predictions
    #                       cuisines Price
    data = [[0, 1, 13, 15, 2, 90.0, 400.0, 0]]  # Obtained from user
    # Create the pandas DataFrame
    x_test = pd.DataFrame(data, columns=x.columns)
    #here we used support vector machine algo to predict the model,invloves .sav file used below
    #from sklearn import svm
    #clf to fit the model first time,one its fitted then just load using -> loaded_model below
    #clf = svm.svc(decision_function_shape='ovo')
    #clf.fit(x,y)
    import pickle
    #pickle.dump(clf, open('harshith.sav','wb')) # Change the path according to your convinience
    loaded_model = pickle.load(open('/home/kashi/PycharmProjects/intern/harshith.sav/harshith.sav','rb')) # Its support vector model Load the values from the path where you have saved it earlier
    pr=loaded_model.predict(x_test)
    addr=list(set(zomato[zomato['name']==pr[0]]['address']))#getting addr by getting the name of the restaurant
    return pr,addr