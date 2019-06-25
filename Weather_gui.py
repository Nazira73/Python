import tkinter as tk
import requests


HEIGHT = 700
WIDTH = 800

def test_function(entry):
    print('This is the entry:', entry)

def format_response(weather):
    try:
         name = (weather['name'])
         desc = (weather['weather'][0]['description'])
         temp = ((weather['main']['temp']) - 273)

         final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, round(temp,2))

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '7cd7e5c22bb53545deefddf96e80ef08'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : weather_key, 'q' : city, 'units' : 'Celsius'}
    response = requests.get(url, params = params)
    weather = response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print((weather['main']['temp'])-273)
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

back_image = tk.PhotoImage(file = "landscape.png")
back_label = tk.Label(root,image= back_image)
back_label.place(relheight = 1,relwidth = 1)

frame = tk.Frame(root, bg = '#001433' , bd = 5)
frame.place(relx = 0.5 , rely = 0.1 , relwidth = 0.75 , relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place(relheight = 1,relwidth = 0.65)

button = tk.Button(frame,text = 'Get weather', command = lambda: get_weather(entry.get()))
button.place(relx = 0.7,rely = 0,relheight = 1,relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#eeffcc', bd = 10)
lower_frame.place(relx = 0.5 , rely = 0.25 , relwidth = 0.75 , relheight = 0.5, anchor = 'n')

label = tk.Label(lower_frame, font = ("Arial",14),bg = '#b3d9ff',bd = 10,justify = "left",anchor = 'nw')
label.place(relwidth = 1, relheight = 1)

tk.mainloop()