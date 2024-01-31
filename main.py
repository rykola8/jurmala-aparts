
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

#print(apartments[0][8])

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        number = input('Whats the sequence number?: ')
        print(apartments[int(number)])
    elif choice == '2':
        def myfunc(apartment):
            return int(apartment[8])
        apartments.sort(key = myfunc, reverse = True)
        print(apartments[0:9])
        pass
    elif choice == '3':
        def myfunc(apartment):
            return int(apartment[8])
        apartments.sort(key = myfunc)
        print(apartments[0:9])
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        newprice = []
        nameprice = int(input('name a price: '))

        def myfunc(apartment):
            return int(apartment[8])
        apartments.sort(key = myfunc, reverse = True)
        
        for x in apartments:
            if nameprice > int(x[8]):
                newprice.append(x)
        print(newprice[0:19])
        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass

    elif choice == '6':
        # 
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")