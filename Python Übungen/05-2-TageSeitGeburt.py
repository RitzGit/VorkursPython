# Aufgabe:  Zeit seit der Geburt berechnen mit args

import datetime 
import argparse

parser = argparse.ArgumentParser()


parser.add_argument('day', type=int)
parser.add_argument('month', type=int)
parser.add_argument('year', type=int)
parser.add_argument('form')

args = parser.parse_args()

def time_since_birth(bday, form):
    date = datetime.datetime.now()
    if form == "days":
        return date - bday

bday = time_since_birth(datetime.datetime(args.year, args.month, args.day), args.form)
print(bday)