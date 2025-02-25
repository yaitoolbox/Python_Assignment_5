
#Create a dictionary with 25 student names and marks

student_marks = { 'Vijai':65, 'Gopal':80, 'Pinky':90, 'Lakshmi':98,'Jyothi': 34,
                  'Srikanth': 90, 'Maram': 95, 'Kumari': 76, 'Ram Prasad': 90, 'Tambi':25,
                  'Prasanna': 100, 'Bhavesh': 92, "Vinodh":95,'Vejendla': 100, 'Tenali':45,
                  'Santu': 99, 'Sai Sampadha':100,'Sadhana':90,'Srinivas':92, 'Sahini': 50,
                  'John': 87,'Joe':55,'Jambo':77,'Jacky':89,'Darling':100
                  }

#Ask the user to input the student name

student_name = input("Enter the Student Name >> ")

#Displaying the marks of the student

if student_name in student_marks:
    print(f"{student_name}'s marks : {student_marks[student_name]}")
else:
    print(f"{student_name} name not found")