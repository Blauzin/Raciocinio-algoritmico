import sys

name = input("What is your name? ")
formatted_name = ' '.join([part.capitalize() for part in name.split()]) #splits the name into each component, capitalizes it and then joins them together

cpf = input("What is your cpf? ") #checks cpf lenght before formatting it 
if len(cpf) != 11:
    print("Invalid CPF")
    sys.exit() #exits the program if the cpf is invalid 

formatted_cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]

phone = input("What is your phone number? ")
if len(phone) != 11: #checks the length of the phone number before formatting it
    print("Invalid phone number")
    sys.exit() #exits the program if the phone number is invalid
formatted_phone = "(" + phone[0:2] + ")" + phone[2:7] + "-" + phone[7:11]

ano = int(input("What is your year of birth?"))

print("Hello, your name is: " + str(formatted_name) + ", your CPF is " + str(formatted_cpf) + ", your cellphone number is " + str(formatted_phone) + " and you were born in " + str(ano))