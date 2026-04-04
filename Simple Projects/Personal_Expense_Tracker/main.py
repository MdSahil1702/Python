
from datetime import datetime
import json
import os

# import datetime
# class Expenses:
#     id=10001
#     def __init__(self,date,category,amount,description):
#         self.date=date
#         self.category=category
#         self.amount=amount
#         self.description=description
#         self.Expense=[]
        
#         readFromFile(self.Expense)
        
#     def add_Expenses(self):
#         Expenses.id=Expenses.id+1
#         expense={
#         "id":Expenses.id,
#         "date":self.date,
#         "category":self.category,
#         "amount":self.amount,
#         "description":self.description,
        
#         }
        
#         insertIntoFile(expense)
        
#         # self.Expense.append(expense)
#         print("Expense added!")
#         # print(self.Expense)
        
#     def view_Expenses(self):
        
#         # if(self.Expense.__sizeof__()==0):
#         if(os.path.exists("expenses_data.txt")):
#             readFromFile(self.Expense)
#             print(self.Expense)
#         else:
#             print("No expenses added till yet")
        
        
        
    
        
    
        
          
        
# def insertIntoFile(Expense):
#         f=open("expenses_data.txt",'a')
#         f.write(Expense)
#         f.close()
        
# def readFromFile(Expense):
#         if os.path.exists("expenses_data.txt"):
#             f=open("expenses_data.txt",'r')
#             Expense=f.read()
id=100

def validate_date(a):
    if(a==""):
        today=datetime.today().date()
        return today
    try:
        valid_date=datetime.strptime(a,"%Y-%m-%d").date()
        return valid_date
    except ValueError:
        print("Invalid date format! Please enter i YYYY-MM-DD format.")
def saveToFile(new_expense):
    global id
    id=id+1
    new_expense["id"]=id
    json_data=json.dumps(new_expense)
    
    f=open("expenses.json",'a')
    f.write(json_data+"\n")
    
    f.close()
    print(f"Expenses added successfully!(ID:{new_expense["id"]} )")
    
def add_expenses():
    new_expense={}
    
    
    a=input("Enter date (YYYY-MM-DD) or press Enter for today:")
    a=validate_date(a)
    new_expense["date"]=a.strftime("%Y-%m-%d")
    # print(new_expense["date"].strftime("%Y-%m-%d"))
    
    
    
    a=input("Select category (Food/Transport/Shopping/Bills/Other): ")
    a=a.title()
    if(a=="Food" or a=="Transport"or a=="Shopping"or a=="Bills"or a=="Other"):
     new_expense["category"]=a
    else:
     print("Invalid category")
    
    a=float(input("Enter amount (in $): "))
    
        
    if(not(a.is_integer())):
        print("Invalid Amount!")
    elif(a<0):
        print("Amount cannot be negative!")
    else:
        new_expense["amount"]=a

    a=input("Enter description(optional):")
    if(a==""):
        new_expense["description"]="No description"
    else:
        new_expense["desctiption"]=a

    saveToFile(new_expense)    

def get_expenses_fromfile(saved_expenses):
    f=open("expenses.json",'r')
    for i in f:
        saved_expenses.append(json.loads(i))
    f.close()
    
    
    
    
def view_Expenses():
    if(os.path.exists("expenses.json")):
        print("ID   Date    Category    Amount  Description")
        saved_expenses=[]
        get_expenses_fromfile(saved_expenses)
        
        for e in saved_expenses:
            print(f"{e['id']}   {e['date']}   {e['category']}   {e['amount']}   {e['description']}")
    else:
        print("No expenses added yet!")
        
    
        
            
def main():
    
    obj=None
    while True:
        print("===PERSONAL EXPENSE TRACKER BY SAHIL")

        print("1.Add Expense\n2.View All Expenses\n3.View Summary\n4.Filter by Category\n5.Delete Expense\n6.Set Monthly Budget\n7.Exit")    
        
        a=int(input())

    
        match a :
            case 1:
                add_expenses()
                
                # print("Date (YYYY-MM-DD):")
                # b=input()
                # print("Category:")
                # b1=input()
                # print("Amount:")
                # b2=input()
                # print("Description:")
                # b3=input()
                
                # obj = Expenses(b,b1,b2,b3)
                # obj.add_Expenses()
                
            
                
            case 2:
                
                view_Expenses()
                
                return
                    
            case 7:
                print("Exiting!")
                break
                
            
            
main()
            
            
    
        



    
