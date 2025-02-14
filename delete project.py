class Employees:
    def __init__(self):
        print("employees are here:")

    def __del__(self):
        print ("destroctor called:")  

def create_obj():
    print ("makinkg object.....")
    obj= Employees() 
    print("function endes here")
    return obj

print("object made")
obj=create_obj()
print ("bye")