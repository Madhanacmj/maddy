# -*- coding: utf-8 -*-
"""Madhan saikumar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d_-TtC51NO7X6wCINskJkY4cOKplfr6H
"""

#qus 4
import pandas as pd
df=pd.DataFrame({
"students name":['a','b','c','d','e','f','g','h','i','j'],
"DOB":[2000,2000,2000,2000,2001,2000,2001,2000,2001,2000],
"weight":[45,57,50,46,56,70,59,65,80,48],
"height":[1.76,1.80,1.98,2.10,2.11,2.00,1.68,1.59,1.78,1.70],
"age":[22,21,22,21,22,22,21,21,22,21],})
df["BMI"]=round(df['weight']/df['height'])
print(df)



#qus 5
bill=int(input("enter units used:"))
if bill == 0 and bill < 100:
    print("units consumed=",bill,"unit amount=Rs 0.50/unit",round(0.50*bill))
elif bill >= 100 and bill <= 200:
    print("units consumed=",bill,"unit amount=Rs 0.75/unit",round(0.75*bill))
elif bill >= 200 and bill <= 300:
    print("units consumed=",bill,"unit amount=Rs 1.20/unit",round(1.20*bill))
else :
    print("units consumed=",bill,"unit amount=Rs 1.50/unit",round(1.50*bill))

# qus 1
print("""I am signing up for Replit's 100 days of Python challenge! I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day. I'll be using Replit, an amazing online IDE so I can do this from my phone wherever I happend to be.
No excuses for not coding from the middle of a field!""")

#qus 2
print("A person bought a mobile for the cost of 12,300 with additionally he pays 18% of GST.")
price=12300
GST=price*(18/100)
NetPrice=price+GST
print("GST",GST)
print("NetPrice:",NetPrice)

#qus 1
malware={'adwar':'tracks user activity',
        'Botnet':'infected and commanded by the attacker',
        'keylogger':'A keylogger can monitor a great deal of user activity, including email, browsing activity, program ',
        'spyware':'A little like adware'}
print(malware)
print(len(malware))
print(type(malware))
malware['trojon']='trojon is a malware it attack unexpeted time'
print(malware)
malware.update({'adwar': 'virus'})
print(malware)
malware.pop('spyware')
print(malware)
malware.clear()
print(malware)