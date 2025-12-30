# expense trracker
expenseList =[] #List of expenses the form pf dictionary
print ("Welcome to the Expense Tracter : ")
while True:
    print("===Menu==")
    print("1. Add Expenses")
    print("2.view All Expenses")
    print("3. View Total Cost")
    print("4.Exit")
    choice= int(input("Please enter your Choice :"))
    
    if(choice==1):
       date=input("Enter the date of the Cost:")
       category=input("Enter the Category ?(Food,Travel,Makeup,Book,Car,Dress):")
       description=input("Detail Description:")
       amount=float(input("Enter the amout :"))
       
       expense={
           "Date":date,
           "Category":category,
           "Description":description,
           "Amount":amount
       }
       expenseList.append(expense)
       print("\n Done bro.Expense is added succesfully")
    # view all expenses
    elif(choice ==2):
        if(len(expenseList)==0):
            print("No Expenses Added.Go spend first.  ")
        else:
            print("==This is all your expenses==")
            count= 1
            for eachcost in expenseList:
                print(f"cost Number {count} -> {eachcost["Date"]}, {eachcost["Category"]}, {eachcost["Description"]}, {eachcost["Amount"]} ")
                count= count+1
    # view total spending
    elif(choice == 3):
        total= 0
        for eachcost in expenseList:
            total = total + eachcost["Amount"]

        print("\n TOTAL Cost = ", total) 
    # Exit
        
    elif(choice == 4):
        print("Thank you for updating our system.")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")         