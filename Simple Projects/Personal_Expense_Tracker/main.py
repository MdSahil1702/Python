print("===PERSONAL EXPENSE TRACKER BY SAHIL")

print("1.Add Expense\n2.View All Expenses\n3.View Summary\n4.Filter by Category\n5.Delete Expense\n6.Set Monthly Budget\n7.Exit")


class Expenses:
    def __init__(self,date,category,amount,description):
        self.date=date
        self.category=category
        self.amount=amount
        self.description=description
        
    def add_Expenses(self):
        E=[self.date,self.category,self.amount,self.description]
        
        zipped= zip(["date","category","amount","description"],E)
        
        Expense=dict(zipped)
        print("Expense added!")
        print(Expense)
        
    
        
    
a=int(input())


match a :
    case 1:
        print("Date (YYYY-MM-DD):")
        b=input()
        print("Category:")
        b1=input()
        print("Amount:")
        b2=input()
        print("Description:")
        b3=input()
        
        obj = Expenses(b,b1,b2,b3)
        obj.add_Expenses()
        
        
        
        
   
        



    
