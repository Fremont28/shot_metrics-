#import dataset 
import json 
f=open("0021700002_full_pbp.json","r") 
data=json.load(f) #data is now a dictionary

#Kevin Durant shot attempts
for i in range(len(data['g']['pd'][3]['pla'])):
    if data['g']['pd'][3]['pla'][i]['pid']==201142:
        if data['g']['pd'][3]['pla'][i]['etype']==1:
          print(data['g']['pd'][3]['pla'][i]["locX"],data["g"]["pd"][3]["pla"][i]["locY"])
        elif data['g']['pd'][3]['pla'][i]['etype']==2:
          print(data['g']['pd'][3]['pla'][i]["locX"],data["g"]["pd"][3]["pla"][i]["locY"])

#James Harden shot attempts
for i in range(len(data['g']['pd'][3]['pla'])):
    if data['g']['pd'][3]['pla'][i]['pid']==201935:
        if data['g']['pd'][3]['pla'][i]['etype']==1:
          print(data['g']['pd'][3]['pla'][i]["locX"],data["g"]["pd"][3]["pla"][i]["locY"])
        elif data['g']['pd'][3]['pla'][i]['etype']==2:
          print(data['g']['pd'][3]['pla'][i]["locX"],data["g"]["pd"][3]["pla"][i]["locY"])

#player shots 
import pandas as pd 
shots=pd.read_csv("hou vs golden.csv")

#Kevin Durant shots 
import matplotlib.pylab as plt
plt.scatter(durant_x,durant_y)
plt.title('Kevin Durant Shot Attempts')
plt.xlabel('x')
plt.ylabel('y')
plt.show() 
plt.savefig('durant.png')

#James Harden Shots
import matplotlib.pylab as plt
plt.scatter(harden_x,harden_y)
plt.title('James Harden Shot Attempts')
plt.xlabel('x')
plt.ylabel('y')
plt.show() 
plt.savefig('harden.png')









        