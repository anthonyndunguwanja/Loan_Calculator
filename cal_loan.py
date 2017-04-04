#calculate loan
def loan_amount(Amount_borrowed,rate,time):
    #int_rate = 0.12
    #Amount_borrowed = input("Enter amount to borrow:")
    #time = input("Enter payment period:")
    
    amount_to_pay = Amount_borrowed + (Amount_borrowed *(rate/100) * (time/12))
    
    return amount_to_pay

    
    
    
        
        
    
    
    
