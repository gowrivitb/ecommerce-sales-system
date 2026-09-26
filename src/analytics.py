from src.orders import orders
from src.customer import customer
from src.inventory import inventory
from src.products import products

def TotalOrders():
    
    return(len(orders))

def TotalSales():
    t=0
    for o in orders:
        t+=float(o['t_amt'])
    return t

def BSProd():
    s={}
    for o in orders:
        if o['product_id'] in s:
            s[o['product_id']]+=int(o['qty'])
            
        else:
            s[o['product_id']]=int(o['qty'])
    
    b=0
    bid=''
    print('BEST SELLING ITEM IS :')
    for j,k in s.items():
        if k>b:
            b=k
            bid=j
    for p in products:
        if p['product_id']==bid:
            for m,n in p.items():
                
                print(m,'=',n)
    print('Total Sold=',b)

def PremCustomers():
    t=0
    for c in customer:
        if c['premium']=='Yes':
            t+=1
    return t

def LSProd():
    for i in inventory:
        if int(i['Quantity'])<10:
            print('LOW STOCK:',i)
