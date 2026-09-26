from src.analytics import TotalOrders,TotalSales,BSProd,LSProd,PremCustomers

def SalesReport():
    print('***** SALES REPORT *****')
    print('Total Orders=',TotalOrders())
    print('Total Sales=',TotalSales())
    BSProd()
    print("************************")   