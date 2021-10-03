import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'w+', new line='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(info_list)

   condition = True

while(condition):
    student_info = input("Enter student information in the following format (Name Age Contact Number E-mail_ID): ")
    print("Entered information:" + student_info)

    student_info_list = student_info.split(' ')
    print("Entered split up information is:" + str(student_info_list))

    write_into_csv (student_info_list)
    
    condition_cheak = input( "Enter to countinue with others (yes / no)")
    if condition_cheak == "yes":
         condition = True
    elif condition_cheak == "no":
         condition = False
         
