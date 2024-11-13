# Uni1
uni_1 = {
    "id": "1",
    "name": "Cal-Tech",
    "location": "California",
    "quality": "10/10",
    "rate": "3%",
}

# Uni2
uni_2 = {
    "id": "2",
    "name": "Harvard University",
    "location": "Massachusetts",
    "quality": "10/10",
    "rate": "3%",
}

# Uni3
uni_3 = {
    "id": "3",
    "name": "Princeton University",
    "location": "New Jersey",
    "quality": "10/10",
    "rate": "4%",
}

# Uni4
uni_4 = {
    "id": "4",
    "name": "Stanford",
    "location": "California",
    "quality": "10/10",
    "rate": "4%",
}

# Uni5
uni_5 = {
    "id": "5",
    "name": "Brown University",
    "location": "Rhode Island",
    "quality": "10/10",
    "rate": "5%",
}

# Uni6
uni_6 = {
    "id": "6",
    "name": "MIT",
    "location": "Massachusetts",
    "quality": "10/10",
    "rate": "5%",
}

# Uni7
uni_7 = {
    "id": "7",
    "name": "University of Chicago",
    "location": "Chicago",
    "quality": "10/10",
    "rate": "5%",
}

# Uni8
uni_8 = {
    "id": "8",
    "name": "Yale University",
    "location": "Connecticut",
    "quality": "10/10",
    "rate": "5%",
}

# Uni9
uni_9 = {
    "id": "9",
    "name": "Dartmouth University",
    "location": "New Hampshire",
    "quality": "10/10",
    "rate": "6%",
}

Univ = [uni_1, uni_2, uni_3, uni_4, uni_5, uni_6, uni_7, uni_8, uni_9]

for uni in Univ:
    print(f"ID: {uni.get('id')}, Name: {uni.get('name')}, Location: {uni.get('location')}, Quality: {uni.get('quality')}, Acceptance Rate: {uni.get('rate')}")