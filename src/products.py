import csv
products=[]

with open('data/products.csv', 'r') as f:
    r= csv.DictReader(f)
    for o in r:
        products.append(o)
        

def AddProduct():
    for i in products:
        print('details of products')
        for j,k in i.items():
            print(j,'=',k)
    
    P={}
    pid=input('ENTER PRODUCT ID:')
    ptyp=input('ENTER PRODUCT TYPE:')
    pname=input('ENTER PRODUCT NAME:')
    pbrand=input('ENTER PRODUCT BRAND:')
    pprice=int(input('ENTER PRODUCT PRICE:'))
    P['product_id']=pid
    P['product_type']=ptyp
    P['product_name']=pname
    P['brand']=pbrand
    P['price']=pprice
    products.append(P)
    with open('data/products.csv', 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=P.keys())
        w.writerow(P)

    print('!!!!!PRODUCT ADDED SUCCESSFULLY!!!!!')

def ViewProducts():
    for i in products:
        print('details of products')
        for j,k in i.items():
            print(j,'=',k)

            

def SearchProducts():
    
    v=input('Enter product_id to view:')
    s=False
    for i in products:
        if i['product_id']==v:
            for j,k in i.items():
                print(j,'=',k)
            s=True
    if s==False:
        print('PRODUCT NOT FOUND')


def UpdateProduct():
    p=input('Enter Product ID:')
    s=False
    for i in products:
        if i['product_id']==p:
            s=True
            for j,k in i.items():
                print(j,'=',k)
            print('What do you want to change?')
            print('1. Product Type')
            print('2. Product Name')
            print('3. Brand Name')
            print('4.Price')
            n=int(input('Enter your option:'))
            if n==1:
                i['product_type']=input('Enter new Product Type:')
                with open('data/products.csv', 'w', newline='') as f:
                    w = csv.DictWriter(f, fieldnames=products[0].keys())
                    w.writeheader()
                    w.writerows(products)
            elif n==2:
                i['product_name']=input('Enter New product name:')
                with open('data/products.csv', 'w', newline='') as f:
                    w =csv.DictWriter(f, fieldnames=products[0].keys())
                    w.writeheader()
                    w.writerows(products)
            elif n==3:
                i['brand']=input('Enter Brand Name:')
                with open('data/products.csv', 'w', newline='') as f:
                    w = csv.DictWriter(f, fieldnames=products[0].keys())
                    w.writeheader()
                    w.writerows(products)
            elif n==4:
                i['price']=int(input('Enter New Price:'))
                with open('data/products.csv', 'w', newline='') as f:
                    w = csv.DictWriter(f, fieldnames=products[0].keys())
                    w.writeheader()
                    w.writerows(products)
            else:
                print('!!!!! INVALID OPTION !!!!!')
            for j,k in i.items():
                print(j,'=',k)
    if s==False:
        print('PRODUCT NOT FOUND')
    
        



def RemoveProduct():
    p=input('Enter Product ID:')
    s=False
    for i in products:
        if i['product_id']==p:
            s=True
            for j,k in i.items():
                print(j,'=',k)
                
            print('Are you sure you ant to delete this product?')
            print('1. Yes')
            print('2. No')
            u =int(input('Enter your option 1 or 2'))
            if u==1:
                l=products[0].keys()

                products.remove(i)
                with open('data/products.csv', 'w', newline='') as f:
                    w = csv.DictWriter(f, fieldnames=l)
                    w.writeheader()
                    w.writerows(products)
            elif u==2:
                continue
            else:
                print('!!!!! INVALID OPTION !!!!!')
    if s==False:
        print('!!!!! PRODUCT NOT FOUND !!!!!')
            

if __name__=='__main__':
    print('1.Add Product')
    print('2.View Products')
    print('3.Search Product')
    print('4.Update Product')
    print('5.Remove Product')

    c=int(input('Enter your choice: '))

    if c== 1:
        AddProduct()
    elif c==2:
        ViewProducts()
    elif c==3:
        SearchProducts()
    elif c==4:
        UpdateProduct()
    elif c==5:
        RemoveProduct()
    else:
        print('INVALID OPTION')