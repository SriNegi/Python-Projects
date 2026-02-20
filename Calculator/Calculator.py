#Project 1



while True:
    print("Mini Calculator using Python")
    print("1. ADDITION ")
    print("2. SUBTRACTION ")
    print("3. MULTIPLICATION ")
    print("4. DIVISION")
    print("5. REMAINDER")
    print("6. EXIT")
    choice=int(input("Enter a choice(1-6): "))
    if choice==6:
        break
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))

    match choice:
        case 1: 
            print("Addition : ", num1+num2)
        case 2: 
            print("Subtraction : ", num1-num2)
        case 3: 
            print("Multiplication : ", num1*num2)
        case 4: 
            print("division : ", num1/num2)
        case 5: 
            print("Remainder : ", num1%num2)
    



   


   
    
    
    
    
    
    
  


