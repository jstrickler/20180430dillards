#!/usr/bin/env python
from datetime import date, datetime, time, timedelta


aidan_bd = date(2002, 8, 21)

print(aidan_bd)

today = date.today()

print(today)

aidan_raw_age = today - aidan_bd

print(aidan_raw_age)

aidan_age = aidan_raw_age.days/365.25

print("aidan is {:.2f} years old".format(aidan_age))

