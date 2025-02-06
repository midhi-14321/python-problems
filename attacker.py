attack1=int(input("enter atc1 value:"))
attack2=int(input("enter atc2 value:"))
health1=int(input("enter energy1:"))
health2=int(input("enter energy2:"))
if attack1>attack2:
    print("warrior1 wins")
elif attack1<attack2:
    print("warrior2 wins")
elif attack1==attack2:
    if health1>health2:
        print("warrior1 wins based on health")
    elif health1<health2:
        print("warrior2 wins based on health")
    else:
        print("tie")