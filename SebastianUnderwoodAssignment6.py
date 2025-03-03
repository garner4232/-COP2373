#This program questions the user for phone number,
#social security number, and zip code. The program then
#checks to see if each variable is valid, returning valid or invalid
import re


#Checks the phone number to match a certain number of digits in three specific ways
def validatePhone(phone):
    pattern = re.compile(r"^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$")
    return "Valid" if pattern.match(phone) else "Invalid"


#Checks the social security number to see if it has a certain number of digits in only two ways
def validateSSN(ssn):
    pattern = re.compile(r"^\d{3}-\d{2}-\d{4}$|^\d{9}$")
    return "Valid" if pattern.match(ssn) else "Invalid"


#Checks the zip code to make sure it only has five digits
def validateZip(zipCode):
    pattern = re.compile(r"^\d{5}$")
    return "Valid" if pattern.match(zipCode) else "Invalid"


#Inquires specific data about the user, then validates it
def main():
#Gathers the data from user
    phone = input("Enter a phone number (example: 941-780-1963): ")
    ssn = input("Enter a Social Security Number (example: 421-65-8399 or 421658399): ")
    zipCode = input("Enter a ZIP Code (example: 34241): ")
#Uses the results from the previous functions to show the user if
#the data is valid or not.
    print("Validation Results:")
    print(f"Phone Number: {validatePhone(phone)}")
    print(f"SSN: {validateSSN(ssn)}")
    print(f"ZIP Code: {validateZip(zipCode)}")

main()
