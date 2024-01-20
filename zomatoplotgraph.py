#This file plots the graph just by importing it and providing data to the function
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import operator

df=pd.read_csv("/home/shamanth/Downloads/zomato.csv")
#function for plotting no. of restaurants vs area // bar graph
def online_or_not():
    plt.title('Online Order vs Offline Order')
    sb.countplot(df['online_order'])
    plt.show()

def rest_area_plot(data,title):
    counts=data
    plt.figure(title)
    sb.barplot(counts.index,counts.values,alpha=0.8,color='blue')
    plt.title(title,fontsize=20,color='gray')
    plt.xlabel('Location')
    plt.ylabel('No. of Restaurants')
    plt.xticks(rotation=45,fontsize=8)
    plt.show()


def ratedistribution(data,title):
    plt.figure(title)
    sb.distplot(data)
    plt.title('Rate Distribution', fontsize=20,color='gray')
    plt.xlabel('Rate')
    plt.xticks(fontweight='light',fontsize=8)
    plt.show()
#converting rating into numeric value
def convert_float():
    float_rate = []
    # df['rate'] = df['rate'].apply(lambda x: float(x[:-2].strip()))
    for i in df['rate']:
        if str(i) != 'NEW' and str(i) != 'nan' and str(i) != 'Nan' and str(i) != '-':
            float_rate.append(float(str(i)[0:3]))
    return float_rate


def covert_dict():
    dishes = df['dish_liked'].dropna()
    dish_liked_dict={}
    for dish in dishes:
        dish_list = [x.strip() for x in dish.split(',')]
        for dish_item in dish_list:
            if dish_item in dish_liked_dict.keys():
                dish_liked_dict[dish_item] +=1
            else:
                dish_liked_dict[dish_item] = 1
    return dish_liked_dict
def plot_top_dishes(dish_liked_dict):
    sorted_dish = sorted(dish_liked_dict.items(),key=operator.itemgetter(1), reverse=True)
    x = [x[0] for x in sorted_dish[:20]]
    y = [y[1] for y in sorted_dish[:20]]
    plt.figure(figsize=(20, 10))
    sb.barplot(x, y, alpha=0.8, color='skyblue')
    plt.title('Top 20 most liked dishes', fontsize=25)
    plt.ylabel('Number of Restaurants', fontsize=20)
    plt.xlabel('Locations', fontsize=20)
    plt.xticks(rotation=45,fontsize=8)
    plt.show()
def all_restaurant_graph():
    sb.countplot(df['rest_type'])
    sb.countplot(df['rest_type']).set_xticklabels(sb.countplot(df['rest_type']).get_xticklabels(), rotation=90,ha="right")
    plt.title('Restuarant Type')
    plt.show()
def famous_rest():
    plt.figure(figsize=(17, 10))
    chains = df['name'].value_counts()[:20]
    sb.barplot(x=chains, y=chains.index, palette='deep')
    plt.title("Most famous restaurants chains in Bangaluru")
    plt.xlabel("Number of outlets")
    plt.show()
