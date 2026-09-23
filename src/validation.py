from products import products
def ProductExists(product_id):
    for p in products:
        if p['product_id']==product_id:
            return p
    return None
    
    