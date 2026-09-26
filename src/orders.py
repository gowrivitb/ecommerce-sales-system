import csv
from src.customer import customer
from src.products import products
from src.inventory import inventory
from src.validation import ProductExists,InventoryExists
orders=[]
with open('data/orders.csv','r') as f:
    r=csv.DictReader(f)
    for o in r:
        orders.append(o)
def GenerateOrderID():
    l=len(orders)+1
    if l<10:
        return 'O00'+str(l)
    elif l<100:
        return 'O0'+str(l)
    else:
        return 'O'+str(l)
def PlaceOrder(c):
    v=input('Enter product name:')
    s=False
    for i in products:
        if i['product_name']==v:
            for j,k in i.items():
                print(j,'=',k)
            s=True
            print('Which Product do ou prefer?')
            pid=input('Please enter the product id:')
            p=ProductExists(pid)
            if p is not None:
                k=InventoryExists(inventory,pid)
                if k is not None:
                    print(k['Quantity'],'are available')
                    print('Do you want to buy this product?')
                    print('1.Yes')
                    print('2.No')
                    n=int(input('Enter your choice(1 or 2):'))
                    if n==1:
                        o={}
                        o['order_id']=GenerateOrderID()
                        o['customer_id']=c['customer_id']
                        o['product_id']=pid
                        a=int(input('Enter number of products added to cart:'))
                        if a>int(k['Quantity']):
                            print('Not Enough Stock')
                            break
                        else:
                            o['qty']=a
                            t=a*int(p['price'])
                            if c['premium']=='Yes':
                                 t=t-t*(10/100)
                                 o['t_amt']=t
                            o['t_amt']=t
                            orders.append(o)
                            with open('data/orders.csv','a',newline='') as f:
                                w=csv.DictWriter(f,fieldnames=o.keys())
                                w.writerow(o)
                            k['Quantity']=int(k['Quantity'])-a
                            with open('data/inventory.csv','w',newline='') as f:
                                w=csv.DictWriter(f,fieldnames=inventory[0].keys())
                                w.writeheader()
                                w.writerows(inventory)
                            print('ORDER PLACED SUCCESSFULLY')
                            print('TOTAL AMOUNT=',o['t_amt'])

                    elif n==2:
                        return
                    else:
                        print('INVALID OPTION')
                        return
                if k is None:
                    print('INVENTORY NOT FOUND')
                    return
            if p is None:
                print('PRODUCT NOT FOUND')
                return
            
    if s==False:
        print('PRODUCT NOT FOUND')
        return

def MyOrders(c):
    s=False
    for o in orders:
        if o['customer_id']==c['customer_id']:
            s=True
            for j,k in o.items():
                print(j,'=',k)
                
    if s==False:
        print('NO ORDERS FOUND')
        return

def ViewOrders():
    s=False
    for o in orders:
        s=True
        for j,k in o.items():
            print(j,'=',k)
    if s==False:
        print('NO ORDERS FOUND')

def SearchOrder():
    s=False
    oid=input('Enter Order Id:')
    for o in orders:
        if o['order_id']==oid:
            s=True
            for j,k in o.items():
                print(j,'=',k)
    if s==False:
        print('ORDER NOT FOUND')

def CancelOrder(c):
    s=False
    oid=input('Enter Order ID:')
    for o in orders:
        if o['order_id']==oid:
            if o['customer_id']==c['customer_id']:
                s=True
                n=orders[0].keys()
                pid=o['product_id']
                q=int(o['qty'])
                orders.remove(o)
                with open('data/orders.csv','w',newline='') as f:
                    w=csv.DictWriter(f,fieldnames=n)
                    w.writeheader()
                    w.writerows(orders)
                for i in inventory:
                    if i['product_id']==pid:
                        i['Quantity']=int(i['Quantity'])+q
                        with open('data/inventory.csv','w',newline='')as f:
                            w=csv.DictWriter(f,fieldnames=inventory[0].keys())
                            w.writeheader()
                            w.writerows(inventory)
                        print('ORDER CANCELLED SUCCESSFULLY')
                        break
    if s==False:
        print('ORDER NOT FOUND')

def CancelOrderEmp():
    s=False
    oid=input('Enter Order ID:')
    for o in orders:
        if o['order_id']==oid:
            s=True
            n=orders[0].keys()
            pid=o['product_id']
            q=int(o['qty'])
            orders.remove(o)
            with open('data/orders.csv','w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=n)
                w.writeheader()
                w.writerows(orders)
            for i in inventory:
                if i['product_id']==pid:
                    i['Quantity']=int(i['Quantity'])+q
                    with open('data/inventory.csv','w',newline='')as f:
                        w=csv.DictWriter(f,fieldnames=inventory[0].keys())
                        w.writeheader()
                        w.writerows(inventory)
                    print('ORDER CANCELLED SUCCESSFULLY')
                    break
    if s==False:
        print('ORDER NOT FOUND')
