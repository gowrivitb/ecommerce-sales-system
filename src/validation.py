from products import products
def ProductExists(product_id):
    for p in products:
        if p['product_id']==product_id:
            return p
    return None
    

def InventoryExists(inventory,product_id):
    for i in inventory:
        if i['product_id']==product_id:
            return i 
    return None
