import requests #pip install requests
from colorama import Fore,init
import os
import time
from config import *
#clear the terminal
#windows => 'cls' ,Linux and mac => 'clear'
clear_var = 'cls' if os.name=='nt' else 'clear'
clear = lambda : os.system(clear_var)
clear()
init(autoreset=True)
green = Fore.LIGHTGREEN_EX
bold = '\33[1m'
red = '\33[31m'
time.sleep(1)
print(bold + 'Open Weather App...')
time.sleep(1)
print('                    Developed by' + bold + red + ' SHAN...')
time.sleep(1)

print()
print('1.by city' + green + ' name... ') 
time.sleep(1)
print('2.by' + green + ' latitude and longitude... ') #This Method is not yet ready
time.sleep(1)
choice = int(input('enter your choice '))
time.sleep(.5)
clear()

def choose_color(temp):
  if temp < 25 :
    return '\33[34m'
  elif temp >=25 and temp <=36 :
    return '\33[33m'
  else :
    return '\33[31m'

def weather_check(url) :

   
   
        clear() 
        url = url
    #this is my api key if you want api key login into openweather website and get the apikeys
        try :
            response = requests.get(url,timeout=5)
        except :
            print('server down try again later....')
            return
        if response.ok :
            print('*------------------------------------------------*')
            print('|                     {0} {1}                        '.format(green+ bold +response.json()['name'].upper(),response.json()['sys']['country'].upper()))
            lon = response.json()['coord']['lon']
            lat = response.json()['coord']['lat']
            print('| '+ bold +'city coordinates..........                     |')
            print('| ' + f'longitude : {lon}   ',end = '    ')
            print( f'lattitude : {lat}  ')
            print('|                                                |')
            print('| '+'weather : {}                     '.format(green + '\33[1m'+response.json()['weather'][0]['description']))
            print('|                                                |')
            print('| '+ bold +'temperature condtions......                    |')
            value = response.json()['main']
            cnt = 0
            color = choose_color(value['temp'])
            for i,j in value.items() :
                if cnt%2 == 0:
                    print('| '+ color + str(i) + ' : ' + str(j),end = '    ')
                    cnt += 1
                else :
                    print( color + str(i) + ' : ' + str(j))
                    print('|                                                |')
                    cnt += 1
            
            print('| ' + bold +'wind conditions....                            |')
            print('| ' + 'wind speed : {} '.format(response.json()['wind']['speed']),end= '    ')
            print( 'wind degree : {}        |'.format(response.json()['wind']['deg']))
            print('|                                                |')
            print('*------------------------------------------------*')
            print()
            
            
                 
        else :
            print(red + 'city not found....')
            print()

if choice == 1 :
  while(True) :
    city = input('enter your city ')
    if city == '0' :
     clear()
     break
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric'
    weather_check(url)
  
elif choice == 2 :
    while(True) :
     lon,lat = map(float,(input('enter your longitude and lattitude ').strip().split()))
     url = f'http://api.openweathermap.org/data/2.5/weather?lon={lon}&lat={lat}&appid={apikey}&units=metric'
     weather_check(url)
else :
    raise KeyError('Invalid Input.....')


print('This is Developed by'+ red + bold + ' SHAN.......')
print()
