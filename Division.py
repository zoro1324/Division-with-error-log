from datetime import datetime

try:
    divedent=(input("Enter the divident :"))
    divisor=(input("Enter the divisor :"))
    divedent=float(divedent)
    divisor=float(divisor)
    result=divedent/divisor
    print(result)
except Exception as error:
    now=datetime.now()
    with open("log.txt","a") as log:
        log.write(f"At {now} for the inputs DIVIDENT = {divedent} and DIVISOR = {divisor}, This error has occoured : {error} \n")
        print("Error log was Updated.")
else:
    print("No error")
finally:
    print("Program ran sucessfully")