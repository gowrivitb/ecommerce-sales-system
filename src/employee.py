import csv
employee=[]
with open('data/employee.csv','r') as f:
    r=csv.DictReader(f)
    for o in r:
        employee.append(o)

def LoginEmp():
    eid=input('Enter employee id:')
    p=input('Enter your password:')
    for e in employee:
        if e['emp_id']==eid:
            if e['password']==p:
                print('Logged In')
                return e
            else:
                print('INCORRECT PASSWORD')
                return None
    print('Employee Not Found')
    return None

