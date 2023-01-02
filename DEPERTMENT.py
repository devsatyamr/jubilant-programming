import csv 
 
dep_fields = ['DEPARTMENT ID', 'DEPARTMENT NAME', 'LIST OF BATCHES'] 
dep_database = 'DEPARTMENT.csv' 
 
def add_department(): 
    print("-------------------------")     
    print("Add Department Information")     
    print("-------------------------") 
    global dep_fields 
    global dep_database 
 
 
    dep_data = []     
    for field in dep_fields:         
      value = input("Enter " + field + ": ") 
      dep_data.append(value) 
 
    with open(dep_database, "a", encoding="utf-8") as f: 
        writer = csv.writer(f) 
        writer.writerows([dep_data]) 
 
    print("Data saved successfully")     
    input("Press any key to continue")     
    return 
 
def display_batches():     
  global dep_database     
  with open(dep_database, "r", encoding="utf-8") as f: 
    reader = csv.reader(f)         
    for row in reader:             
      if len(row)>0:                 
        print (row[2]) 
 
print("DEPARTMENT MODULE FUNCTIONS") 
print("1.Create New Department") 
print("2.List of Batches") 
z=int(input("Enter your choice")) 
if z==1: 
  add_department() 
elif z==2: 
  display_batches() 
else: 
  print("Invalid choice") 
