import csv 
import phonenumbers
from faker import Faker 
fake = Faker()
phone_fake = Faker(locale="bn_BD")

def create_phone_book(rows=1000):
    

    with open('./testPhoneBook.csv','w',newline='' ) as csvfile :
        fieldnames= ['first_name','last_name','phone_number']

        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(rows):
            number = phone_fake.phone_number()
            objPhone = phonenumbers.parse(number, "BD")
            writer.writerow({'first_name': fake.first_name(),
                            'last_name': fake.last_name(),
                            'phone_number': phonenumbers.format_number(objPhone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)})


                          