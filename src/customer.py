import csv
customer=[]
with open('data/customer.csv','r') as f:
    r=csv.DictReader(f)
    for o in r:
        customer.append(o)

def GenerateCustomerID():
    n=len(customer)+1
    if n<10:
        return 'C00'+str(n)
    elif n<100:
        return 'C0'+str(n)
    else:
        return 'C'+str(n)

def RegisterCustomer():
    c={}
    c['customer_id']=GenerateCustomerID()
    c['customer_name']=input('Enter your name:')
    c['email']=input('Enter your email id')
    c['phone']=input('Enter ur 10-digit phone number:')
    c['password']=input('Enter your password')
    i=input('Confirm your password:')
    if c['password']!=i:
        print('incorrect password')
        return
    c['premium']='No'
    customer.append(c)
    with open('data/customer.csv','a',newline='') as f:
        w=csv.DictWriter(f,fieldnames=c.keys())
        w.writerow(c)

def LoginCustomer():
    e=input('Enter your email id or phone numer:')
    p=input('Enter your password:')
    print('login input',repr(e))
    
    for c in customer:
        print('login email',repr(c['email']))
        print('login phone',repr(c['phone']))
        if c['email']==e or c['phone']==e:
            if c['password']==p:
                print('LOGGED IN')
                return c
            else:
                print('incorrect login id or password.')
                return None
        
    print('incorrect login id or password')

def ViewCustomer():
    for c in customer:
        for k,v in c.items():
            if k!='password':
                print(k,'=',v)

def SearchCustomer():
    cid=input('Enter customer id:')
    s=False
    for c in customer:
        if c['customer_id']==cid:
            s=True
            for j,k in c.items():
                if j!='password':
                    print(j,'=',k)
    if s==False:
        print('CUSTOMER NOT FOUND')

def PremiumCustomers():
    s=False
    for c in customer:
        if c['premium']=='Yes':
            s=True
            for j,k in c.items():
                if j!='password':
                    print(j,'=',k)
    if s==False:
        print('NO PREMIUM CUSTOMERS FOUND')



def UpgradePremium():
    lid=input('Enter your phone number or email id')
    
    for c in customer:
        if c['email']==lid or c['phone']==lid:
            if c['premium']=='No':
                print('Your Membership= Standard')
                print('Do you want Premium Membership?')
                print('Price:499/yr')
                print('1.Yes')
                print('2.No')
                i=int(input('Enter your choice(1 or 2):'))
                if i==1:
                    print('did you complete the payment?')
                    print('1.yes')
                    print('2.no')

                    j=int(input('Enter your choice(1 or 2)'))
                    if j==1:
                        c['premium']='Yes'
                        print('Congratulations you are premium member')
                        with open('data/customer.csv','w',newline='') as f:
                            w=csv.DictWriter(f,fieldnames=customer[0].keys())
                            w.writeheader()
                            w.writerows(customer)
                            return
                    elif j==2:
                        return
                    else:
                        print('INVALID OPTION')
                        return
                elif i==2:
                    return
                else:
                    print('INVALID OPTION')
                    return
            else:
                print('You are a Premium Subscriber')
                return
    
    print('User doesnt Match')
    return

def CancelPremium():
    lid=input('Enter yoru phone number or email id')
    for c in customer:
        if c['email']==lid or c['phone']==lid:
            if c['premium']=='Yes':
                print('Are you sure you want to cancel your memebership?')
                print('1.Yes')
                print('2.No')
                i=int(input('Enter your choice(1 or 2)'))
                if i==1:
                    print('Cancellation Succesful')
                    c['premium']='No'
                    with open('data/customer.csv','w',newline='') as f:
                        w=csv.DictWriter(f,fieldnames=customer[0].keys())
                        w.writeheader()
                        w.writerows(customer)
                elif i==2:
                    return
                else:
                    print('INVALID OPTION')
                    return
            else:
                return
    print('User doesnt Match')
    return

def UpdateCustomer():
    lid=input('Enter your phone number or email id:')
    for c in customer:
        if c['email']==lid or c['phone']==lid:
            print('What do you want to update?')
            print('1.Update Name')
            print('2.Update Email ID')
            print('3.Update Phone Number')
            print('4.Update Password')
            i=int(input('Enter yoru choice(1-4)'))
            if i==1:
                q=input('Enter your password:')
                if c['password']==q:
                    c['customer_name']=input('Enter your name:')
                    with open('dat.customer.csv','w',newline='') as f:
                        w=csv.DictWriter(f,fieldnames=customer[0].keys())
                        w.writeheader()
                        w.writerows(customer)
                else:
                    print('INCORRECT PASSWORD')
                    return
            elif i==2:
                q=input('Enter your password:')
                if c['password']==q:
                    c['email']=input('Enter your email id:')
                    with open('dat.customer.csv','w',newline='') as f:
                        w=csv.DictWriter(f,fieldnames=customer[0].keys())
                        w.writeheader()
                        w.writerows(customer)
                        return
                else:
                    print('INCORRECT PASSWORD')
                    return
            elif i==3:
                q=input('Enter your password:')
                if c['password']==q:
                    c['phone']=input('Enter your phone number:')
                    with open('dat.customer.csv','w',newline='') as f:
                        w=csv.DictWriter(f,fieldnames=customer[0].keys())
                        w.writeheader()
                        w.writerows(customer)
                        return
                else:
                    print('INCORRECT PASSWORD')
                    return
            elif i==4:
                q=input('Enter your password:')
                if c['password']==q:
                    y=input('Enter your new password:')
                    x=input('Confirm your password:')
                    if y==x:
                        c['password']=y
                        with open('dat.customer.csv','w',newline='') as f:
                            w=csv.DictWriter(f,fieldnames=customer[0].keys())
                            w.writeheader()
                            w.writerows(customer)
                            return
                    else:
                        print('Password doesnt match')
                        return
                else:
                    print('INCORRECT PASSWORD')
                    return
            else:
                print('INVALID OPTION')
                return
            


