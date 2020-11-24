import re
wachtwoord= input("Input your password")
x = True


while x:
    if (len(wachtwoord)<8 or len(wachtwoord)>24):
        print("Wachtwoord moet tussen de 8 en 24 karakters zijn")
        break
    elif not re.search("[a-z]",wachtwoord):
        print("Er moeten lowercase letters in het wachtwoord zitten")
        break
    elif not re.search("[0-9]",wachtwoord):
        print("Er moeten cijfers in het wachtwoord zitten")
        break
    elif not re.search("[A-Z]",wachtwoord):
        print("Er moeten Hoofdletters in het wachtwoord zitten")
        break
    elif not re.search("[!@#$%^&*]",wachtwoord):
        print("Er moeten speciale tekens in het wachtwoord zitten (!,@,#,$,%,^,&,*)")
        break
    elif re.search("\s",wachtwoord):
        break
    else:
        print("Wachtwoord goedgekeurd")
        x=False
        break



if x:
    print("Wachtwoord foutgekeurd.")


