# Models go here:
from peewee import *

db = SqliteDatabase('betsy.db')


class User(Model):
    name = CharField()

    class Meta:
        database = db


class User_Address(Model):
    user = ForeignKeyField(User, backref='address')
    street = CharField()
    postal_code = CharField()
    city = CharField()

    class Meta:
        database = db


class User_Billing(Model):
    user = ForeignKeyField(User, backref='billing')
    card_type = CharField()
    card_number = IntegerField()

    class Meta:
        database = db


class Product(Model):
    owner = ForeignKeyField(User, backref='products')
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()

    class Meta:
        database = db


class Tag(Model):
    name = CharField()

    class Meta:
        database = db


class ProductTag(Model):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

    class Meta:
        database = db


class Transaction(Model):
    buyer = ForeignKeyField(User, backref='transactions')
    bought_product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()
    total_price = FloatField()
    bought_at = DateTimeField()

    class Meta:
        database = db


def init():
    connection = db.connect()

    if connection:
        print('Connected to database.')

    with db:
        db.create_tables([
            User,
            User_Address,
            User_Billing,
            Product,
            Tag,
            ProductTag,
            Transaction
        ])

        print('Created tables.')


def test_data():
    # User #1 - Betsy
    betsy = User.create(
        name='Betsy'
    )

    betsy_address = User_Address.create(
        user=betsy, 
        street='Leidschestraat 28', 
        postal_code='1234 AA', 
        city='Amsterdam'
    )

    betsy_billing = User_Billing.create(
        user=betsy, 
        card_type='ING Bank', 
        card_number=1234567890
    )

    wooden_chair = Product.create(
        owner=betsy, 
        name='Wooden Chair', 
        description='Wooden Chair, handmade by Betsy',
        price=89.99,
        quantity=8
    )

    wooden_bench = Product.create(
        owner=betsy,
        name='Wooden Bench',
        description='Wooden Bench, handmade by Betsy',
        price=129.99,
        quantity=4
    )

    wooden_statue = Product.create(
        owner=betsy,
        name='Wooden Statue',
        description='Wooden Statue, handmade by Betsy',
        price=17.99,
        quantity=3
    )

    # User 2 - Paul
    paul = User.create(
        name='Paul'
    )

    paul_address = User_Address.create(
        user=paul,
        street='Ringostraat 34',
        postal_code='4141 AZ',
        city='Delft'
    )

    paul_billing = User_Billing.create(
        user=paul,
        card_type='ABN Amro',
        card_number=9876543210
    )

    electric_guitar = Product.create(
        owner=paul,
        name='Electric Guitar',
        description='Nice Electric Guitar',
        price=349,
        quantity=9
    )

    acoustic_guitar = Product.create(
        owner=paul,
        name='Acoustic Guitar',
        description='Nice Acoustic Guitar',
        price=229,
        quantity=10
    )

    bass_guitar = Product.create(
        owner=paul,
        name='Bass Guitar',
        description='Nice Bass Guitar',
        price=399,
        quantity=15
    )

    # User 3 - Peter
    peter = User.create(
        name='Peter'
    )

    peter_address = User_Address.create(
        user=peter,
        street='Utrechtsestraat 17',
        postal_code='3201 ZA',
        city='Utrecht'
    )    

    peter_billing = User_Billing.create(
        user=peter,
        card_type='Knab',
        card_number=1245678930
    )

    electric_heater = Product.create(
        owner=peter,
        name='Electric Heater',
        description='Small Electric Heater',
        price=15.99,
        quantity=5
    )

    electric_razor = Product.create(
        owner=peter,
        name='Electric Razors',
        description='The one and only great Electric Razor',
        price=39.50,
        quantity=25
    )

    keyboard = Product.create(
        owner=peter,
        name='Keyboard',
        description='A nice Keyboard',
        price=799,
        quantity=3
    )

    #Tags
    electric = Tag.create(
        name='electric'
    )

    great = Tag.create(
        name='great'
    )

    keyboard = Tag.create(
        name='keyboard'
    )

    acoustic = Tag.create(
        name='acoustic'
    )

    wooden= Tag.create(
        name='wooden'
    )

    handmade = Tag.create(
        name='handmade'
    )

    guitar = Tag.create(
        name='guitar'
    )

    furniture = Tag.create(
        name='furniture'
    )

    art = Tag.create(
        name='art'
    )

    nice = Tag.create(
        name='nice'
    )

    # ProductTags
    # Betsy
    ProductTag.create(
        product=wooden_chair,
        tag=wooden
    )

    ProductTag.create(
        product=wooden_bench,
        tag=wooden
    )

    ProductTag.create(
        product=wooden_statue,
        tag=wooden
    )

    ProductTag.create(
        product=wooden_chair,
        tag=furniture
     )

    ProductTag.create(
        product=wooden_bench,
        tag=furniture
    )

    ProductTag.create(
        product=wooden_statue,
        tag=art
    )    

    ProductTag.create(
        product=wooden_chair,
        tag=handmade
    )    

    ProductTag.create(
        product=wooden_bench,
        tag=handmade
    )    

    ProductTag.create(
        product=wooden_statue,
        tag=handmade
    )    

    ProductTag.create(
        product=wooden_chair,
        tag=furniture
    )    

    ProductTag.create(
        product=wooden_bench,
        tag=furniture
    )  

    # Paul
    ProductTag.create(
        product=electric_guitar,
        tag=guitar
    )

    ProductTag.create(
        product=acoustic_guitar,
        tag=guitar
    )

    ProductTag.create(
        product= bass_guitar,
        tag=guitar
    )

    ProductTag.create(
        product=electric_guitar,
        tag=electric
    )

    ProductTag.create(
        product=electric_guitar,
        tag=nice
    )

    ProductTag.create(
        product=acoustic_guitar,
        tag=nice
    )

    ProductTag.create(
        product= bass_guitar,
        tag=nice
    )



    # Peter
    ProductTag.create(
        product=electric_heater,
        tag=electric
    )

    ProductTag.create(
        product=electric_razor,
        tag=electric
    )

    ProductTag.create(
        product=keyboard,
        tag=nice
    )

    ProductTag.create(
        product=electric_razor,
        tag=great
    )

    ProductTag.create(
        product=keyboard,
        tag=keyboard
    )

    print('Database with test data.')