import os
import pyttsx3
from geopy.geocoders import Nominatim
import requests, json
from tkinter import *
ts=pyttsx3.init()
ts.setProperty('rate',150)  #to reduce spped of voice {default=200}

root=Tk()
root.title("agriculture system")
root.geometry("1400x700")

crop=""
def locate():
    city=e1.get()
    geolocator=Nominatim(user_agent="MyApp")
    location=geolocator.geocode(city)
    print("latitude = ",location.latitude)
    print("longitude = ",location.longitude)
    

    apikey="173a8ff52cfdd22a7427bbab2fc7c606"
    baseurl="https://api.openweathermap.org/data/2.5/weather?lat="
    completeURL=baseurl+str(location.latitude)+"&lon="+str(location.longitude)+"&appid="+apikey
    response = requests.get(completeURL)
    data=response.json()
    temp=data["main"]["temp"]
    temp=str(temp)+"K"
    l4.config(text=temp)
    print("current temperature = ",data["main"]["temp"])     #in kelvin
    hum=data["main"]["humidity"]
    l5.config(text=hum)
    print("humidity = ",data["main"]["humidity"])  #humidity

    b2=Button(f,text="recommandations",command=recommand)
    b2.place(x=650,y=350)


def recommand():
    temp=l4.cget("text")
    hum=l5.cget("text")
    count=0
    for i in temp:
        count+=1
    temp=float(temp[:count-1])
    ftemp=(temp-273.5)*(9/5)+32
    temp=int(ftemp)
    hum=int(hum)
    speak(temp,hum)
    
def speak(temp,hum):
    display()
    a="as the temperature is "+str(temp)+" degree fahrenheit and humidity is "+str(hum)+" percent you can grow wheat, rice, corn, sugercane"
    ts.say(a)
    ts.runAndWait()
    

def display():
    l6=Label(f,text="crop")
    l6.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l6.place(x=400,y=400)

    l7=Label(f,text="required temperature")
    l7.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l7.place(x=550,y=400)

    l8=Label(f,text="required humidity")
    l8.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l8.place(x=800,y=400)

    l6=Label(f,text="wheat")
    l6.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l6.place(x=400,y=450)

    l7=Label(f,text="70-75F")
    l7.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l7.place(x=550,y=450)

    l8=Label(f,text="50-60%")
    l8.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l8.place(x=800,y=450)

    b3=Button(f,text="learn more",command=speak1)
    b3.place(x=1000,y=450)

    l6=Label(f,text="rice")
    l6.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l6.place(x=400,y=500)

    l7=Label(f,text="70-100F")
    l7.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l7.place(x=550,y=500)

    l8=Label(f,text="60-80%")
    l8.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l8.place(x=800,y=500)

    b4=Button(f,text="learn more",command=speak2)
    b4.place(x=1000,y=500)

    l6=Label(f,text="corn")
    l6.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l6.place(x=400,y=550)

    l7=Label(f,text="75-86F")
    l7.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l7.place(x=550,y=550)

    l8=Label(f,text="55-65%")
    l8.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l8.place(x=800,y=550)

    b5=Button(f,text="learn more",command=speak3)
    b5.place(x=1000,y=550)

    l6=Label(f,text="sugarcane")
    l6.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l6.place(x=400,y=600)

    l7=Label(f,text="65-100F")
    l7.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l7.place(x=550,y=600)

    l8=Label(f,text="40-80%")
    l8.config(font=("sans-serif",13,"normal"),bg="#585FFA")
    l8.place(x=800,y=600)
    
    b6=Button(f,text="learn more",command=speak4)
    b6.place(x=1000,y=600)

def speak1():
    text="wheat needs a lot of sunshine especially when the grains are beginning to fill out ."
    ts.say(text)
    ts.runAndWait()

def speak2():
    text="rice needs hot and humid climatic conditions. high humidity and good supply of water and prolonged sunshine is required."
    ts.say(text)
    ts.runAndWait()

def speak3():
    text="corn needs hot temperature, high humidity and intermittent moderate rains for good growth."
    ts.say(text)
    ts.runAndWait()
def speak4():
    text="sugarcane requires very hot climate with humid atmosphere and with average rainfall of 1200 mm to 2500 mm for good growth."
    ts.say(text)
    ts.runAndWait()

f=Frame(root)
f.configure(bg="#585FFA",width=1400,height=700)
f.place(x=0,y=0)

l=Label(f,text="AI in Agriculture ")
l.configure(bg="#585FFA",font=("sans-serif",20,"bold"))
l.place(x=700,y=10)

l1=Label(f,text="enter city name :")
l1.configure(font=("sans-serif",16,"normal"),bg="#585FFA")
l1.place(x=500,y=100)


l2=Label(f,text="Temperature :")
l2.configure(font=("sans-serif",16,"normal"),bg="#585FFA")
l2.place(x=500,y=250)

l3=Label(f,text="Humidity :")
l3.configure(font=("sans-serif",16,"normal"),bg="#585FFA")
l3.place(x=500,y=300)

l4=Label(f,text="")
l4.configure(font=("sans-serif",16,"normal"),bg="#585FFA")
l4.place(x=700,y=250)

l5=Label(f,text="")
l5.configure(font=("sans-serif",16,"normal"),bg="#585FFA")
l5.place(x=700,y=300)

e1=Entry(f)
e1.configure(font=("sans-serif",16,"normal"))
e1.place(x=700,y=100)

b1=Button(f,text="submit",command=locate)
b1.configure(font=("sans-serif",16,"normal"),width=0)
b1.place(x=700,y=150)




root.mainloop()






