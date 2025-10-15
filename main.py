from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "˖˚₊~ ComFe ~₊˚˖"
owner_name = "Shantia Luna"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Donut", "Macaroons", "Cake"]
beverages = ["Matcha", "Water"]

# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Donut": 79.99,
    "Macaroons": 150.00,
    "Cake": 100.00,
    "Matcha": 85.00,
    "Water": 20.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Donut']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Macaroons']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Cake']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Matcha']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Water']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")
