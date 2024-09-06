# Fake data - @T7C


module `Faker` cung cấp các thông tin giả, ngẫu nhiên


## cài đặt 
```bash
pip install faker
```

sử dụng mã sau:
```bash

from faker import Faker

fake = Faker('en_US')

print("Name:", fake.name())
print("Gender:", fake.random_element(elements=('Male', 'Female')))
print("Date of Birth:", fake.date_of_birth())
print("Phone Number:", fake.phone_number())

print("\nAddress:")
print("Street Address:", fake.street_address())
print("City:", fake.city())
print("State:", fake.state())
print("Zipcode:", fake.zipcode())

print("\nCompany Information:")
print("Company Name:", fake.company())
print("Job Title:", fake.job())

print("\nFinancial Information:")
print("Credit Card Number:", fake.credit_card_number())
print("Credit Card Expiry:", fake.credit_card_expire())
print("CVV Code:", fake.credit_card_security_code())

print("\nInternet Information:")
print("Email:", fake.email())
print("Domain Name:", fake.domain_name())
print("IPv4 Address:", fake.ipv4_public())
print("Username:", fake.user_name())
print("Password:", fake.password())

print("\nDate and Time Information:")
print("Current DateTime:", fake.date_time())
print("Date:", fake.date())
print("Time:", fake.time())

print("\nOther Data Types:")
print("Favorite Color:", fake.color_name())
print("License Plate:", fake.license_plate())
print("SSN:", fake.ssn())
print("Insurance Company:", fake.company())
print("Catchphrase:", fake.catch_phrase())
print("Sample Text:", fake.text())

print("\nRandom Information:")
print("Gender:", fake.random_element(elements=('Male', 'Female')))
print("Favorite Language:", fake.language_name())
print("Country:", fake.country())
print("Postal Code:", fake.postcode())

```

## minh họa
![example](images/image.png)