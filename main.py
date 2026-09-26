print('-----------------------------------')
print('E-Commerce Sales Management System')
print('-----------------------------------')
from src.customer import *
from src.employee import *
from src.products import *
from src.inventory import *
from src.orders import *
from src.analytics import *
from src.reports import *


while True:
    print('1.Employee Login')
    print('2.Customer Login')
    print('3.Register Customer')
    print('4.Exit')
    i=int(input('Enter your choice(1-4):'))
    if i==1:
        e=LoginEmp()
        if e is not None:
            while True:
                print('1.Manage Products')
                print('2.Manage Inventory')
                print('3.Manage Customers ')
                print('4.Manage orders')
                print('5.Analytics')
                print('6.Reports')
                print('7.Logout')
                n=int(input('Enter your choice(1-7):'))
                if n==1:
                    while True:
                        print('1.Add Products')
                        print('2.View Products')
                        print('3.Search Products')
                        print('4.Update Products')
                        print('5.Remove Products')
                        print('6.Exit')
                        m=int(input('Enter your choice(1-6):'))
                        if m==1:
                            AddProduct()
                        elif m==2:
                            ViewProducts()
                        elif m==3:
                            SearchProducts()
                        elif m==4:
                            UpdateProduct()
                        elif m==5:
                            RemoveProduct()
                        elif m==6:
                            break
                        else:
                            print('INVALID OPTION')
                            
                elif n==2:
                    while True:
                        print('1.Add Inventory')
                        print('2.View Inventory')
                        print('3.Search Inventory')
                        print('4.Update Inventory')
                        print('5.Remove Inventory')
                        print('6.Exit')
                        m=int(input('Enter your choice(1-6):'))
                        if m==1:
                            AddInventory()
                        elif m==2:
                            ViewInventory()
                        elif m==3:
                            SearchInventory()
                        elif m==4:
                            UpdateInventory()
                        elif m==5:
                            RemoveInventory()
                        elif m==6:
                            break
                        else:
                            print('INVALID OPTION')
                            
                elif n==3:
                    while True:
                        print('1.View Customers')
                        print('2. Search Customer')
                        print('3.Premium Customers')
                        print('4.Exit')
                        m=int(input('Enter your choice(1-4):'))
                        if m==1:
                            ViewCustomer()
                        elif m==2:
                            SearchCustomer()
                        elif m==3:
                            PremiumCustomers()
                        elif m==4:
                            break
                        else:
                            print('INVALID OPTION')
                            break
                elif n==4:
                    while True:
                        print('1. View All Orders')
                        print('2.Search Orders')
                        print('3.Cancel an Order')
                        print('4.Exit')
                        m= int(input('Enter your choice(1-4):'))
                        if m==1:
                            ViewOrders()
                        elif m==2:
                            SearchOrder()
                        elif m==3:
                            CancelOrderEmp()
                        elif m==4:
                            break
                        else:
                            print('INVALID OPTION')
                elif n==5:
                    while True:
                        print('1.Total Orders')
                        print('2.Total Sales')
                        print('3.Best-Selling Product')
                        print('4.Premium Customers')
                        print('5.Low Stock Products')
                        print('6.Back')
                        m= int(input('Enter your choice(1-6):'))
                        if m==1:
                            print(TotalOrders())
                        elif m==2:
                            print(TotalSales())
                        elif m==3:
                            BSProd()
                        elif m==4:
                            print(PremCustomers())
                        elif m==5:
                            LSProd()
                        elif m==6:
                            break
                        else:
                            print('INVALID OPTION')

                elif n==6:
                    SalesReport()
                elif n==7:
                    break
                else:
                    print('INVALID OPTION')



    elif i==2:
        c=LoginCustomer()
        if c is not None:
            while True:
                print('1.View Products')
                print('2.Search Products')
                print('3.Place Order')
                print('4.My Orders')
                print('5.Cancel My Order')
                print('6.Get Premium')
                print('7.Cancel Premium')
                print('8.Update My Account')
                print('9.Logout')
                x=int(input('Enter your choice(1-8):'))
                if x==1:
                    ViewProducts()
                elif x==2:
                    SearchProducts()
                elif x==3:
                    PlaceOrder(c)
                elif x==4:
                    MyOrders(c)
                elif x==5:
                    CancelOrder(c)
                elif x==6:
                    UpgradePremium()
                elif x==7:
                    CancelPremium()
                elif x==8:
                    UpdateCustomer()
                elif x==9:
                    break
                


                
    elif i==3:
        RegisterCustomer()
        
    elif i==4:
        break
    else:
        print('Invalid Option')


