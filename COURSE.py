import csv 
 
course_fields = ['Course ID', 'Course Name',' Student Name,Student ID,Roll,Score as a Dictionary(multiple student records can be stored as a sub dictionary(ex:{{},{}})'] 
course_database = 'COURSE.csv'  
def add_course(): 
    print("-------------------------")    
    print("Create New Course") 
    print("-------------------------")    
    global course_fields 
    global course_database 
       
    course_data = []     
    for field in course_fields: 
        value = input("Enter " + field + ": ")        
        course_data.append(value)     
    with open(course_database, "a", encoding="utf-8") as f: 
       writer=csv.writer(f)  
       writer.writerows([course_data]) 
 
    print("New Course saved successfully")     
    input("Press any key to continue")     
    return 
 
def display(): 
    global course_database     
    with open(course_database, "r", encoding="utf-8") as f: 
        reader = csv.reader(f)         
        for row in reader:            
          if len(row)>0:                
            print (row[2]) 
def histogram(): 
  from matplotlib import pyplot as plt      
  import numpy as np      
  x=np.array(['A','B','C','D','E','F','A','B','C','D','E','F','A','F','D','D'])
  plt.hist(x)    
print("COURSE MODULE FUNCTIONS") 
print("1.Create New Course") 
print("2.Performance of students in Course") 
print("3.Course statistics as Histogram") 
z=int(input("Enter your choice")) 
if z==1:  
  add_course() 
elif z==2:     
  display() 
elif z==3: 
  histogram()    
else: 
  print("Invalid choice") 
