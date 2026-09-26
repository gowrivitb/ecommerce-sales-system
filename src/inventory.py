import csv
from src.validation import ProductExists,InventoryExists
from src.products import products
inventory=[        ]
with open('data/inventory.csv','r') as f:
    r=csv.DictReader(f)
    for o in r:
     inventory.append(o)
def AddInventory():
    
    ai=input('Enter product id:')
    if ProductExists(ai) is None:
        print('!!!Product Not Found!!!')
        return
    i=InventoryExists(inventory,ai)
    if i is None:
        i={}
        qty=int(input('Enter Product Quantity:'))
        i['product_id']=ai
        i['Quantity']=qty
        inventory.append(i)
        with open('data/inventory.csv','a',newline='') as f:
            w=csv.DictWriter(f,fieldnames=i.keys())
            w.writerow(i)
    else:        
        print('!!!Product already Exists!!!')
        print('Do you want to add quantity?')
        print('1.Yes')
        print('2. No')
        q=int(input('Enter your option(1 or 2)'))
        if q==1:
            i['Quantity']=int(i['Quantity'])+int(input('Amount of new stock:'))
            with open('data/inventory.csv', 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=inventory[0].keys())
                w.writeheader()
                w.writerows(inventory)
        elif q==2:
            return
        else:
            print('!!! Invalid Option !!!')
            return
        return
    

def ViewInventory():
    for i in inventory:
        p=ProductExists(i['product_id'])
        if p is not None:
            print('All Product Details')
            for m,n in p.items():
                print(m,'=',n)
            for j,k in i.items():
                if j!='product_id':
                    print(j,'=',k)
        
            
        


def SearchInventory():
    pid=input('Enter Product ID:')
    p=ProductExists(pid)
    if p is None:
        print('!!!PRODUCT NOT FOUND!!!')
        return
    
    print('Product Details')
    for m,n in p.items():
        print(m,'=',n)
    i=InventoryExists(inventory,pid)
    if i is None:
        print('Inventory not found')
    
    for j,k in i.items():
        if j!='product_id': 
            print(j,'=',k)
    
def UpdateInventory():

    pid=input('Enter Product ID:')
    p=ProductExists(pid)
    if p is None:
        print('Product not found')
        return
    i=InventoryExists(inventory,pid)
    if i is None:
        print('!!! Inventory Not Found!!!')
        return
    else:

        print('Do you want to update quantity?')
        print('1. Yes')
        print('2.No')
        q=int(input('Enter your choice(1 or 2):'))
        if q==1:
            i['Quantity']=int(input('Enter updated quantity:'))
            with open('data/inventory.csv', 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=inventory[0].keys())
                w.writeheader()
                w.writerows(inventory)
            print('!!! INVENTORY UPDATED SUCCESSFULLY !!!')
                
        elif q==2:
            return
        else:
            print('!!!!! INVALID OPTION !!!!!')
            return
    
    

def RemoveInventory():
    pid=input('Enter Product ID:')
    p=ProductExists(pid)
    if p is None:
        print('Product Not Found')
        return
    for m,n in p.items():
        print(m,'=',n)
    i=InventoryExists(inventory,pid)
    if i is None:
        print('!!!!! INVentory Not Found !!!!!')
        return
    else:
        for j,k in i.items():
            if j!='product_id':
                print(j,'=',k)
            
        print('Are you sure you want to delete this inventory?')
        print('1. Yes')
        print('2. No')
        u =int(input('Enter your option 1 or 2'))
        if u==1:
            l=inventory[0].keys()
            inventory.remove(i)
            with open('data/inventory.csv', 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=l)
                w.writeheader()
                w.writerows(inventory)
            print('!!! INVENTORY REMOVED SUCCESSFULLY!!!')
        elif u==2:
            return
        else:
            print('!!! INVALID OPTION!!!')
            
                
    
if __name__=='__main__':

    print('1. Add Inventory')
    print('2. View Inventory')
    print('3. Search Inventory')
    print('4. Update Inventory')
    print('5. Remove Inventory')

    c=int(input('Enter your choice: '))

    if c== 1:
        AddInventory()
    elif c==2:
        ViewInventory()
    elif c==3:
        SearchInventory()
    elif c==4:
        UpdateInventory()
    elif c==5:
        RemoveInventory()
    else:
        print('INVALID OPTION')