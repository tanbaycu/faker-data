from faker import Faker

# Khởi tạo đối tượng Faker với ngôn ngữ tiếng Anh
fake = Faker('en_US')

# Thông tin cá nhân
print("Name:", fake.name())
print("Gender:", fake.random_element(elements=('Male', 'Female')))
print("Date of Birth:", fake.date_of_birth())
print("Phone Number:", fake.phone_number())

# Địa chỉ
print("\nAddress:")
print("Street Address:", fake.street_address())
print("City:", fake.city())
print("State:", fake.state())
print("Zipcode:", fake.zipcode())

# Thông tin công ty
print("\nCompany Information:")
print("Company Name:", fake.company())
print("Job Title:", fake.job())

# Thông tin tài chính
print("\nFinancial Information:")
print("Credit Card Number:", fake.credit_card_number())
print("Credit Card Expiry:", fake.credit_card_expire())
print("CVV Code:", fake.credit_card_security_code())

# Thông tin internet
print("\nInternet Information:")
print("Email:", fake.email())
print("Domain Name:", fake.domain_name())
print("IPv4 Address:", fake.ipv4_public())
print("Username:", fake.user_name())
print("Password:", fake.password())

# Thông tin ngày giờ
print("\nDate and Time Information:")
print("Current DateTime:", fake.date_time())
print("Date:", fake.date())
print("Time:", fake.time())

# Các loại dữ liệu khác
print("\nOther Data Types:")
print("Favorite Color:", fake.color_name())
print("License Plate:", fake.license_plate())
print("SSN:", fake.ssn())
print("Insurance Company:", fake.company())
print("Catchphrase:", fake.catch_phrase())
print("Sample Text:", fake.text())

# Các thông tin ngẫu nhiên khác
print("\nRandom Information:")
print("Gender:", fake.random_element(elements=('Male', 'Female')))
print("Favorite Language:", fake.language_name())
print("Country:", fake.country())
print("Postal Code:", fake.postcode())

