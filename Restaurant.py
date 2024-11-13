# Resto 1
resto_1 = {
    "id": "1",
    "name": "Antonio's",
    "owner": "Tony Boy",
    "cuisine type": "Fine Dining",
    "reservation": "Yes",
}

# Resto 2
resto_2 = {
    "id": "2",
    "name": "Jollibee",
    "owner": "JFC",
    "cuisine type": "Fast Food",
    "reservation": "Yes",
}

# Resto 3
resto_3 = {
    "id": "3",
    "name": "Olive Garden",
    "owner": "Darden Restaurants, Inc.",
    "cuisine type": "Casual Dining",
    "reservation": "No",
}

# Resto 4
resto_4 = {
    "id": "4",
    "name": "Laza Food Plaza",
    "owner": "N/A",
    "cuisine type": "Cafeteria",
    "reservation": "No",
}

# Resto 5
resto_5 = {
    "id": "5",
    "name": "The Alley",
    "owner": "Vikings",
    "cuisine type": "Buffet",
    "reservation": "Yes",
}

# Resto 6
resto_6 = {
    "id": "6",
    "name": "Five Guys",
    "owner": "Five Guys Holdings, Inc.",
    "cuisine type": "Fast Casual",
    "reservation": "Yes",
}

# Resto 7
resto_7 = {
    "id": "7",
    "name": "Mexikombi",
    "owner": "N/A",
    "cuisine type": "Food Trucks",
    "reservation": "no",
}

# Resto 8
resto_8 = {
    "id": "8",
    "name": "It's Just Wings",
    "owner": "Brinker International, Inc.",
    "cuisine type": "Ghost Restaurants",
    "reservation": "No",
}

restaurant = [resto_1, resto_2, resto_3, resto_4, resto_5, resto_6, resto_7, resto_8]

for resto in restaurant:
    print(f"ID:  {resto.get('id')}, Name: {resto.get('name')}, Owner: {resto.get('owner')}, Cuisine Type: {resto.get('cuisine type')}, Reserved?: {resto.get('reservation')}")