import search
import data_base_update

global var
var=0

def student_attendance(data):
    global var

    if var==0:
        faculty_data=data_base_update.get_attendance(1,data)
        var = 1

    if var==1:
        faculty_data=data_base_update.get_attendance(2,data)
    


    
        
    

