from faker import Faker

if __name__ == "__main__":
    fake = Faker()
    
    for i in range(1000):
        print(fake.local_latlng(country_code="ID", coords_only=True))
