from controllerFly import controller
controllerA = controller()

choice = 0

while(choice != 7):
    print("1-Import an airport")
    print("2-Delete an airport")
    print("3-Add a flight operator to an airport")
    print("4-Delete a flight operator from an airport")
    print("5-List airport by operators")
    print("6-List number of planes by operator – (by airport / all)")
    print("7-Exit")
    print("Choose an option:")

    choice = int(input())

    if(choice == 1):
        iata = input("Enter the iata code for the airport: ")
        if(controllerA.AddAirport(iata)):
            print("Airport added")
        else:
            print("Something went wrong")

    if(choice == 2):
        iata = input("Enter the iata code for the airport: ")
        if(controllerA.DeleteAirport(iata)):
            print("Airport deleted")
        else:
            print("Something went wrong")

    if(choice == 3):
        iata = input("Enter the iata code for the airport: ")
        operator = input("Enter the operator for the airport: ")
        numPlanes = int(input("Enter the number of planes: "))
        if(controllerA.AddOperator(iata, operator, numPlanes)):
            print("Operator added")
        else:
            print("Something went wrong")

    if(choice == 4):
        iata = input("Enter the iata code for the airport: ")
        operator = input("Enter the operator for the airport: ")
        if(controllerA.DeleteOperator(iata, operator)):
            print("Operator deleted")
        else:
            print("Something went wrong")

    if(choice == 5):
        operator = input("Enter the operator for the airport: ")
        print(controllerA.ListOperators(operator))

    if(choice == 6):
        operator = input("Enter the operator for the airport: ")
        condition = input("All the airports(all) or one in specific(iata of the airport)? ")
        print("Number of planes:")
        print(controllerA.ListAirport(operator, condition))

