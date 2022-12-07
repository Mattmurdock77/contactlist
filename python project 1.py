names = []
phone_numbers = []
num = int(input("Enter the number of contancts required: "))


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

for i in range(num):
    search_term = input("\nEnter search term name: ")

    print("Search result:")

    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        print("Name: {}, Phone Number: {}".format(search_term, phone_number))

    else:
        print("Name Not Found, Please enter the name correctly")

print("--------------------------End-------------------------------------------------")
