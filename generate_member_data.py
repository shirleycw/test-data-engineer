import random
from faker import Faker
import pandas as pd

# Please note that you'll need to install the faker library in your Databricks environment for this script to work.
# !pip install faker

# Set seed for reproducibility
random.seed(123)

# Initialize Faker library
fake = Faker()

# Set the number of sample records to generate
num_records = 1000

# Generate sample member data
member_data = []
for _ in range(num_records):
    member_id = fake.uuid4()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    country = fake.country()
    registration_date = fake.date_between(start_date='-2y', end_date='today')
    
    member_data.append([member_id, first_name, last_name, email, phone_number, address, city, country, registration_date])

# Create pandas DataFrame from the generated data
df_members = pd.DataFrame(member_data, columns=['member_id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country', 'registration_date'])

# Display sample data
df_members.head()
