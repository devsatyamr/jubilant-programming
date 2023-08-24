//yooooooo

import csv 
student_fields = ['Student ID', 'Name', 'Class Roll Number', 'Batch Name', 
'Batch ID'] 
student_database = 'STUDENT.csv' 
 
def add_student():
  print("-------------------------")
  print("Add Student Information") 
  print("-------------------------")
  global student_fields 
  global student_database 
  student_data = [] 
  for field in student_fields: 
    value = input("Enter " + field + ": ") 
    student_data.append(value) 
    with open(student_database, "a", encoding="utf-8") as f: 
      writer = csv.writer(f) 
      writer.writerows([student_data]) 
      print("Data saved successfully") 
      input("Press any key to continue") 
      return 
def update_student(): 
 global student_fields 
 global student_database 
 print("--- Update Student ---")
 roll = input("Enter roll no. to update: ") 
 index_student = None 
 updated_data = [] 
 with open(student_database, "r", encoding="utf-8") as f: 
  reader = csv.reader(f) 
 counter = 0 
 for row in reader: 
  if len(row) > 0: 
    if roll == row[2]: 
      index_student = counter 
 print("Student Found: at index ",index_student) 
 student_data = [] 
 for field in student_fields: 
  value = input("Enter " + field + ": ") 
  student_data.append(value) 
  updated_data.append(student_data) 
 else: 
  updated_data.append(row) 
 counter += 1 
 
 if index_student is not None: 
  with open(student_database, "w", encoding="utf-8") as f: 
    writer = csv.writer(f) 
  writer.writerows(updated_data) 
 else: 
   print("Roll No. not found in our database") 
 input("Press any key to continue") 
def delete_student(): 
 global student_fields 
 global student_database 
 print("--- Remove Student ---")
 roll = input("Enter roll no. to remove: ") 
 student_found = False 
 updated_data = [] 
 with open(student_database, "r", encoding="utf-8") as f: 
  reader = csv.reader(f) 
 counter = 0 
 for row in reader: 
  if len(row) > 0: 
    if roll != row[2]: 
      updated_data.append(row) 
      counter += 1 
    else: 
      student_found = True 
 if student_found is True: 
  with open(student_database, "w", encoding="utf-8") as f: 
    writer = csv.writer(f) 
    writer.writerows(updated_data) 
    print("Roll no. ", roll, "deleted successfully") 
 else: 
   print("Roll No. not found in our database") 
 input("Press any key to continue") 
def report(): 
 a= input("Student Name:") 
 b=input ("enter subject name:") 
 c=int(input("enter marks")) 
 if c>90: 
   x='A' 
 elif c>80: 
   x='B' 
 elif c>70: 
  x='C' 
 elif c>60: 
  x='D' 
 elif c>50: 
  x='E' 
 elif c<40: 
   x='FAIL(F)' 
 z = open("REPORTCARD.txt","w") 
 l=[a, b ,x] 
 z.writelines(l) 
print("STUDENT MODULE FUNCTIONS") 
print("1.Create A Student") 
print("2.Update Student Details") 
print("3.Remove a student's details from database") 
print("4.Generate Student Report card") 
z=int(input("Enter your choice")) 
if z==1: 
 add_student() 
elif z==2: 
 update_student() 
elif z==3: 
 delete_student() 
elif z==4: 
 report() 
else: 
 print("Invalid choice")
