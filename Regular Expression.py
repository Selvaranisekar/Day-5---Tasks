
'''Email  address
Mobile no of Bangladesh
Telephone numbers of USA
16 character of Alpha numeric password composed of alphabets
of upper case ,lower case , Special characters, numbers'''
import re
data=re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
Mobile_Bangladesh=+97898767898
def Valid_email(email):
    if re.fullmatch(data,email):
        return "Success: email address valid"
    else:
        return "Failed: email address not valid"
email="selvaranisekar.94@gmail.com"
print(Valid_email(email))

def Validate_Mobile_Number_of_Bangladesh(Mobile_Bangladesh):
    pattern=re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    result=re.search(pattern, Mobile_Bangladesh)
    if result:
        return "Success: Mobile number is Bangladesh"
    else:
        return "Failed: Mobile number is not Bangladesh"

Mobile_Bangladesh="+0 9934212311"

print(Validate_Mobile_Number_of_Bangladesh(Mobile_Bangladesh))



