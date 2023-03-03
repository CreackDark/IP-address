import os

import requests

import geocoder

import time

#os.system('	pip install pywebio')from pywebio.output import *

from pywebio.input import *

from pywebio import start_server,config

from pywebio.pin import *

from pywebio.session import *

def check(IP):

    res = requests.get(f'http://ip-api.com/json/{IP}').json()

    if res["status"] == 'fail':

        return 'Error IP ,Try Again IPv4'  

        

@config(theme="dark")

                             

def App():

 popup("Contact",put_link('TeleGram','https://t.me/Creack_Dark',new_window=True))

 toast('BY : Creack_Dark  🇮🇷')

 

 put_html("<center><h1>Web  info-ip 🧐</h1></center>").style('color:red').style('background:linear-gradient(#200015,#10001f')

 put_html('<hr>')

 put_html('''<center> 

       <img src ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvoWSr86KMAFiPNc4dv2uquts3e-yMH_Zaww&usqp=CAU" width=480px> 

           </center>''')

 put_html('<hr>')

 put_html("<h3>Welcome to the get ip informations website  me Creack_Dark  🔓</h3>").style("font-size:23px;wedth:bolder;color:green").style('background:linear-gradient(#200015,#10001f')

 put_html('<hr>')

 

 IP=input('IP :',

 placeholder='ENTER IP',

 validate=check)

 toast('✌🏻😉help us https://t.me/Creack_Dark ✌🏻😉')

 

 our_ip = geocoder.ip(IP).latlng

 map_lenr = our_ip[0]

 map_lenl = our_ip[1]    

  

 result = requests.get(f'http://ip-api.com/json/{IP}').json()

 count = result['country']

 coCo = result['countryCode']

 reg = result['region']

 reN = result['regionName']

 c = result['city']

 z = result['zip']

 la = result['lat']

 lo = result['lon']

 tim = result['timezone']

 isp = result['isp']

 org = result['org']

 ass = result['as'] 

 

 url= f'https://www.google.com/maps/@{map_lenr},{map_lenl},13z'

 img = requests.get(f'https://api.dlyar-dev.tk/scn-wb.json?url={url}').json()["screen"]  

 

 put_table([

 [

 'Location',

 'Country',

 'CountryCode',

 'Region',

 'RegionName',

 'City',

 'Zip',

 'Lat',

 'Lon',

 'TimeZone',

 'ISP','Org',

 'AS'

 ],

 [

 put_image(img).style('width:80px;'),

 put_text(count).style('background:linear-gradient(#200015,#10001f'),

 put_text(coCo).style('background:linear-gradient(#200015,#10001f'),

 put_text(reg).style('background:linear-gradient(#200015,#10001f'),

 put_text(reN).style('background:linear-gradient(#200015,#10001f'),

 put_text(c).style('background:linear-gradient(#200015,#10001f'),

 put_text(z).style('background:linear-gradient(#200015,#10001f'),

 put_text(la).style('background:linear-gradient(#200015,#10001f'),

 put_text(lo).style('background:linear-gradient(#200015,#10001f'),

 put_text(tim).style('background:linear-gradient(#200015,#10001f'),

 put_text(isp).style('background:linear-gradient(#200015,#10001f'),

 put_text(org).style('background:linear-gradient(#200015,#10001f'),

 put_text(ass).style('background:linear-gradient(#200015,#10001f')

 ]

 ])

 put_html('<br>')

 

 D = radio(

''' I hope you like it ''', 

 options=['YES ✅','NO ❌'],inline=True)

 requests.get("https://api.telegram.org/bot"+str('5813694054:AAH5isy_a3EovERLkFX6Z2XaX4CepwwU-4w')+"/sendMessage?chat_id="+str('5365751970')+"&text="+str(D))

   

 put_html('''

 <br>

   <hr>

      <center>

          <ruby>

              <rb>DEVELOPER</rb>

              <rt>[Creack_Dark]</rt>

          </ruby>

          </center>

        <hr>

      <br>

      ''').style('background:linear-gradient(#200015,#10001f')

        

start_server(App, port=8080, debug=True)
