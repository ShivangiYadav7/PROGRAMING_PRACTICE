Enter_a_password=45678
password_is_wrong=0
while password_is_wrong != Enter_a_password:
    ask_agan= int(input("Enter the correct password"))
   

    if Enter_a_password==ask_agan:
       
       print(ask_agan,("correct password.phone is unlocked"))
       break
    else:   
       print(ask_agan,"incorrect password.please try again")
    