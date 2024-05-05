import tkinter as tk
root=tk.Tk()
root.title("Weather app")
root.geometry("330x330")
l=tk.Label(root,text="city name")
e=tk.Entry(root)

def data():
    import requests
    city_name=e.get()
    API_key="6f80490dfe7d0a64e9f9a3be0f17fab3"
    ws=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={API_key}")
    if ws.json()['cod']=='404':
        n0.config(text=f"ERROR 404\nCity name not found")
    else:
        n1.config(text=f"City name:{city_name}")
        country=ws.json()['sys']['country']
        n2.config(text=f"city is in {country}")
        
        weather=ws.json()['weather'][0]['main'] 
        n3.config(text=f"the weather of {city_name} is : {weather}")
        
        temp=ws.json()['main']['temp'] 
        n4.config(text=f"the tempurature of city{city_name} is : {temp}(in kelvin)")  
        
        pressure=ws.json()['main']['pressure']
        n5.config(text=f"pressure is : {pressure} mb")
        
        humidity=ws.json()['main']['humidity']
        n6.config(text=f"humidity in {city_name} is : {humidity} %")
        
        wind=ws.json()['main']['speed']
        n7.config(text=f"high speed is : {wind} m/s")
        
b=tk.Button(root,text='submit',command=data)
l.grid(row=0,column=0)
e.grid(row=0,column=1)
b.grid(row=2,column=1)
n=tk.Label(root,text="name:")        
n.grid(row=3,column=1)
n0=tk.Label(root)        
n0.grid(row=3,column=1)
n1=tk.Label(root)        
n1.grid(row=4,column=1) 
n2=tk.Label(root)        
n2.grid(row=5,column=1)
n3=tk.Label(root)        
n3.grid(row=6,column=1)
n4=tk.Label(root)        
n4.grid(row=7,column=1)
n5=tk.Label(root)        
n5.grid(row=8,column=1)
n6=tk.Label(root)        
n6.grid(row=9,column=1)
n7=tk.Label(root)        
n7.grid(row=10,column=1)

root.mainloop()