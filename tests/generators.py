from faker import Faker
import re
import random



fake = Faker('ru_Ru')

def generator_user_name():
    fio = re.split(r'\W+', fake.name())
    return fio


def generetor_adress():
    adress = re.split(r'\W+', fake.address())
    print(adress)
    return adress


def generator_email():
    email = fake.email()
    return email

