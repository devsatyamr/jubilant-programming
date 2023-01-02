import csv 
 
batch_fields = ['BATCH ID', 'BATCH NAME', 'DEPARTMENT NAME', 
'LIST OF COURSES', 'LIST OF STUDENTS'] 
batch_database = 'BATCH.csv' 
 
def add_batch(): 
    print("-------------------------")     
    print("Add Batch Information")     
    print("-------------------------")     
    global batch_fields 
    global batch_database 
 
 
    batch_data = []     
    for field in batch_fields: 
      value = input("Enter " + field + ": ") 
      batch_data.append(value) 
 
    with open(batch_database, "a", encoding="utf-8") as f: 
      writer = csv.writer(f)         
      writer.writerows([batch_data]) 
 
    print("Data saved successfully")     
    input("Press any key to continue") 
    return 
 
def display_students():     
  global batch_database     
  with open(batch_database, "r", encoding="utf-8") as f: 
    reader = csv.reader(f)         
    for row in reader:             
      if len(row)>0:                 
        print (row[4]) 
def display_course():     
  global batch_database     
  with open(batch_database, "r", encoding="utf-8") as f: 
    reader = csv.reader(f)         
    for row in reader:             
      if len(row)>0:                 
        print (row[3]) 
 
def pie(): 
    from matplotlib import pyplot as plt     
    import numpy as np      
    student = ['ASMIT', 'AKASH', 'AMBHRIN', 'TANISHA']      
    percent= [89,99,32,78]     
    fig = plt.figure(figsize =(10, 7))     
    plt.pie(percent, labels = student)     
    plt.show() 
 
print("BATCH MODULE FUNCTIONS") 
print("1.Create New Batch") 
print("2.List of students in batch") 
print("3.List of courses in batch") 
print("4.Batch Statistics in pie plot") 
z=int(input("Enter your choice")) 
if z==1: 
  add_batch() 
elif z==2: 
  display_students() 
elif z==3: 
  display_course() 
elif z==4:     
  pie()  
else: 
  print("Invalid choice") 
