# Product 1
product_1 = {
    "product": "Canned Food",
    "product name": "Argentina Meatloaf",
    "price": "P49.00",
    "quantity": "100pcs",
    "quality": "7/10",
    "supplier": "Argentina"
}

# Product 2
product_2 = {
    "product": "Shampoo",
    "product name": "Sunsilk Strong & Long Shampoo",
    "price": "P499.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Sunsilk"
}

# Product 3
product_3 = {
    "product": "Conditioner",
    "product name": "Cream Silk Triple Keratin Serum Conditioner",
    "price": "P299.00",
    "quantity": "100pcs",
    "quality": "9/10",
    "supplier": "Cream Silk"
}

# Product 4
product_4 = {
    "product": "Face Cleanser",
    "product name": "Pond's Men Energy Charge",
    "price": "P149.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Pond's"
}

# Product 5
product_5 = {
    "product": "Soap",
    "product name": "Kojie San Men Lightening Face and Body Soap",
    "price": "P79.00",
    "quantity": "100pcs",
    "quality": "9/10",
    "supplier": "Kojie San"
}

# Product 6
product_6 = {
    "product": "Instant Coffee",
    "product name": "Nescafe Classic",
    "price": "P49.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Nescafe"
}

# Product 7
product_7 = {
    "product": "Lotion",
    "product name": "Silka Papaya Premium Whitening Lotion",
    "price": "P98.00",
    "quantity": "100pcs",
    "quality": "7/10",
    "supplier": "Silka"
}

# Product 8
product_8 = {
    "product": "Condiments",
    "product name": "Del Monte Classic Ketchup",
    "price": "P55.00",
    "quantity": "100pcs",
    "quality": "10/10",
    "supplier": "Del Monte"
}

# Product 9
product_9 = {
    "product": "Beverage",
    "product name": "Zesto Big 250",
    "price": "P12.00",
    "quantity": "100pcs",
    "quality": "9/10",
    "supplier": "Zesto"
}

# Product 10
product_10 = {
    "product": "Frozen Food",
    "product name": "Pure Foods Tender Juicy Hotdog",
    "price": "P99.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Pure Foods"
}

products = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10]

for product in products:
    print(f"Product: {product.get('product')}, Product Name: {product.get('product name')}, Price: {product.get('price')}, Quantity: {product.get('quantity')}, Quality: {product.get('quality')}, Supplier: {product.get('supplier')}")