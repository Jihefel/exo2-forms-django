from django_seed import Seed    
from .models import Member
import random
from faker import Faker

def run():
    seeder = Seed.seeder()
    faker = Faker('fr_BE')
    genders = ['homme','femme']
    seeder.add_entity(Member, 60, {
        'name' : lambda x: faker.name(),
        'age' : lambda x: random.randint(18,30),
        'gender' : lambda x: genders[random.randint(0,1)],
        'email' : lambda x: faker.email(),
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)
