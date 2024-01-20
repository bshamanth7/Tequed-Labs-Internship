#! /usr/bin/python3

#This is the main file,imports other two files
# datasets taken from https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants
#importing modules
import tkinter
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import zomatoplotgraph# importing file
import warnings
import svmodel #importing svmodel file

warnings.filterwarnings('ignore')
#creating root window

root=tkinter.Tk()
root.geometry('1000x650')#setting window label and reading csv file
heading=Label(root,text=" R E S T A U R A N T  G U I D E ",font=('Times New Roman',45),bg='white',)
heading.pack(side='top')
place=Label(root,text="B  a  n  g  a  l  o  r  e",font=('Times New Roman',15),bg='white',fg='red')
place.pack(side='top')
df=pd.read_csv("/home/shamanth/Downloads/zomato.csv")#path of dataset as per convinience
t,ad=svmodel.predictmodel()#clling from svmodel file
#creating new windo for restaurant prediction using tkinter
def predictwindow(event):
    new=tkinter.Tk()
    new.geometry('400x250')
    new.title("Restaurant")
    lb=Label(new,text='Restaurant Name :',font=('Arial',21),bg='white')
    lb.pack(side='top')
    lb1=Label(new,text=str(t[0]),font=('Times New Roman',27),bg='white',fg='red')
    lb1.pack(side='top')
    for i in range(3):#presenting first 2 different addrs of restaurant as per ur convience
        lb2 = Label(new, text=str(i+1)+" Address -> "+str(ad[i]), font=('Times New Roman', 12), bg='white')
        lb2.pack(side='top')
    new.mainloop()

#defining mouse event handler to call graph plot functions
#all function is present in plot module(zomatoplotgraph.py file) i,e calling from plot module
def rest_vs_Location(event):
    zomatoplotgraph.rest_area_plot(df['location'].value_counts()[:15, ], 'Location vs No. of Restaurants in Bangalore')
def poploc_vs_rest(event):
    zomatoplotgraph.rest_area_plot(df.groupby('location')['votes'].sum().sort_values(ascending=False)[:15, ],'Popular Locations vs Restaurants')
def rating_graph(event):
    l=zomatoplotgraph.convert_float()
    zomatoplotgraph.ratedistribution(l,'Rate Distribution')
def top_dishes(event):
    l=zomatoplotgraph.covert_dict()
    zomatoplotgraph.plot_top_dishes(l)
def order_mode(event):
    zomatoplotgraph.online_or_not()
def all_restaurants(event):
    zomatoplotgraph.all_restaurant_graph()
def famous_restau(event):
    zomatoplotgraph.famous_rest()

#adds button feature
button1=Button(root,text='Popular Rest in Area',width=20)
button1.bind("<Button-1>",rest_vs_Location)
button1.pack(side="top")
#poplr rest vs area graph
button2=Button(root,text='Popular Restaurants',width=20)
button2.bind("<Button-1>",poploc_vs_rest)
button2.pack(side="top")
#rating graph button
button3=Button(root,text='Rating Graph',width=20)
button3.bind("<Button-1>",rating_graph)
button3.pack(side="top")
#plotting dishes graph
button4=Button(root,text='Dishes',width=20,)
button4.bind("<Button-1>",top_dishes)
button4.pack(side="top")

button5=Button(root,text='Reataurant Types',width=20)
button5.bind("<Button-1>",all_restaurants)
button5.pack(side="top")

button6=Button(root,text='Order Mode',width=20,)
button6.bind("<Button-1>",order_mode)
button6.pack(side="top")
#famous restaurants
button7=Button(root,text='Famous Reataurants',width=20,)
button7.bind("<Button-1>",famous_restau)
button7.pack(side="top")
#prediction fn cl button
button8=Button(root,text='predict Best Restaurant',width=20,)
button8.bind("<Button-1>",predictwindow)
button8.pack(side="top")

root.mainloop()
