#Openiong the data file

import csv

data = []

with open("dataset2.csv","r") as f:
  csv_reader = csv.reader(f)
  for i in csv_reader:
    data.append(i)

data_1 = data[1:]

#Getting the headers
headers = data[0]

#Creating a list relative mass
relative_mass = []

for i in data_1:
  relative_mass.append(float(i[3]))

#Creating a list relative radius
relative_radius = []

for i in data_1:
  relative_radius.append(float(i[4]))

#Changling solar masses into kilograms

mass = []

for i in relative_mass:
  i = i*1.989e+30
  mass.append(i)

#Changing solar radii into metres

radius = []

for i in relative_radius:
  x = i*6.957e+8
  radius.append(x)

#Creating a function to calculate g
G = float(6.67e-11)

def calculate(mass,radius):
  g = G*float(mass)/float(radius)*float(radius)
  return(g)

#Calculating g of all stars
gravity = []
gravity.append('gravity')

for i in range(len(data_1)):
  g = calculate(mass[i],radius[i])
  gravity.append(g)

#Creating a new data file with gravity
header = data[0]
header2 = gravity[0]
header.append(header2)

star_data1 = data[1:]
star_data2 = gravity[1:]

for index,data_row in enumerate(star_data1):
  star_data1[index].append(star_data2[index])

with open('data.csv','a+') as f:
  csv_writer = csv.writer(f)
  csv_writer.writerow(header)
  csv_writer.writerows(star_data1)
