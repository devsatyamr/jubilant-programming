import csv 
def entermarks(): 
  a=input("Enter Course Name of Examination")   
  b=input("Enter all the Student's Roll number in list form" )   
  c=input("Enter respective marks of the students out of 100 in list form")   
  print("Data saved") 
  x=[a,b,c]   
  with open("EXAMINATION.csv" ,"a") as e:       
    writer=csv.writer(e) 
    writer.writerow(x) 
   
     
def performance():   
  with open("EXAMINATION.csv" ,"r") as e:       
    r=csv.reader(e)       
    for row in r:         
      print(row) 
   
   
     
def plot(): 
  import matplotlib.pyplot as plt   
  import numpy as np   
  x1 = np.array([70,62,45,35])   
  x2 = np.array([70,62,45,35])   
  y1 = np.array([85,95,75,93])   
  y2 = np.array([97,86,90,84])   
  plt.scatter(x1, y1, color='green')   
  plt.scatter(x2, y2, color='red')   
  plt.show() 
 
print("EXAMINATION MODULE FUNCTIONS") 
print("1.Enter Marks of Students") 
print("2.View Performance of Students") 
print("3.Exam Statistics in scatter plot") 
z=int(input("Enter your choice")) 
if z==1: 
  entermarks() 
elif z==2: 
  performance() 
elif z==3:   
  plot() 
else:   
  print("Invalid choice") 
