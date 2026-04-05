
from datetime import datetime
import json
import os

id=0

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
    data=[]
    
    
    if(os.path.exists('expenses.json')):
        
        f=open("expenses.json","r")
        try:
            data=json.load(f)
        except:
            data =[]
    
        finally:
            f.close()
    data.extend(new_expense)
    
    f=open("expenses.json","w")
    json.dump(data,f,indent=4) 
    
    
    print(f"Expenses added successfully!(ID:{new_expense[0]['id']} )")
    
def add_expenses():
    new_expense=[]
    current_expenses={}
    
    
    a=input("Enter date (YYYY-MM-DD) or press Enter for today:")
    a=validate_date(a)
    current_expenses["date"]=a.strftime("%Y-%m-%d")
  
    
    
    a=input("Select category (Food/Transport/Shopping/Bills/Other): ")
    a=a.title()
    if(a=="Food" or a=="Transport"or a=="Shopping"or a=="Bills"or a=="Other"):
     current_expenses["category"]=a
    else:
     print("Invalid category")
    
    a=float(input("Enter amount (in $): "))
    
        
    if(not(a.is_integer())):
        print("Invalid Amount!")
    elif(a<0):
        print("Amount cannot be negative!")
    else:
        current_expenses["amount"]=a

    a=input("Enter description(optional):")
    if(a==""):
        current_expenses["description"]="No description"
    else:
        current_expenses["description"]=a

    global id
    id=id+1
    current_expenses["id"]=id
    
    new_expense=[current_expenses]
    
    saveToFile(new_expense)    

def get_expenses_fromfile(saved_expenses):
    f=open("expenses.json",'r')
    
    data=json.load(f)
    saved_expenses.extend(data)
       
    f.close()
    
    
    
    
def view_Expenses():
    if(os.path.exists("expenses.json")):
        print("ID      Date    Category    Amount  Description")
        saved_expenses=[]
        get_expenses_fromfile(saved_expenses)
        
        for e in saved_expenses:
            print(f"{e['id']}   {e['date']}   {e['category']}   {e['amount']}   {e['description']}")
            
        total= sum(e['amount'] for e in saved_expenses)
        print(" ===================================")
        print(f"Total expenses : $ {total}")
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
                
      
            case 2:
                
                view_Expenses()
                
                return
                    
            case 7:
                print("Exiting!")
                break
                
            
            
main()
            
            
    
        



    
