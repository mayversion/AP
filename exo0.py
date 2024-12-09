rep1=int(input("how many people need a ride"))
print(rep1)
rep2=int(input("how many people can fit in one taxi"))
print(rep2)
nb_taxi=rep1//rep2
if rep1%rep2 != 0:
    nb_taxi+=1
print(f"Number of taxis needed:{nb_taxi}")

