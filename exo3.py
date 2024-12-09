total_amount=int(input("Total amount:"))
nb_items=int(input("Number of items"))
day_of_week=input("Day of the week:")
if day_of_week=="Monday" or day_of_week=="Tuesday" or day_of_week=="Wednesday" or day_of_week=="Thursday" or day_of_week=="Friday" :
    if nb_items>5:
        discount=0.15
    else:
        discount=0.10    
else:
    if nb_items>5:
        discount=0.25
    else:
        discount=0.20
Resultat=total_amount-(total_amount*discount)     
print(f"Total price after discount: {Resultat} dinaras")      