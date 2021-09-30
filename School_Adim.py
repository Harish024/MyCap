
condition = True

while(condition):
    student_info = input("Enter the student Register Roll Number , Name , Age , Email , Mobile :")
    
    spliting_list = student_info.split(' ')
    print("spited new info : " + str(spliting_list))
    
    print(student_info
    
    condition_cheak = input( "Enter to countinue with others (yes / no)")
    if condition_cheak == "yes":
         condition = True
    elif condition_cheak == "no":
         condition = False
         
