aurum_suspension = {
    "555": "Fox 38 Float Factory GripX2",
    "556": "RockShox Pike Ultimate",
    "557": "Marzocchi Bomber Z1",
    "333": "Maxima SC1 High Gloss Coating",
    "123": "full suspension service"
}

# print("Thank you for choosing Aurum Suspension! Your " + aurum_suspension.get("123") + " is scheduled and will be ready for pickup in 3-5 business days!")

billing_code = "222"

aurum_suspension[billing_code] = "Aurum pullover hoodie"

# aurum_suspension.pop("557")

for key, value in aurum_suspension.items():
    print(key + " => " + value)

#print(aurum_suspension)