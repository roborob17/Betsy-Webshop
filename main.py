__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from datetime import datetime
import models

def search(term=str):
    term = term.lower()
    query = models.Product.select().where(models.Product.name.contains(term) | models.Product.description.contains(term))

    if query:
        print('Search results:')
        for product in query:
            print(product.name)
    else:
        print('No products found that matched your search.')


def list_user_products(user_id=int):
    query = models.Product.select().where(models.Product.owner == user_id)

    if query:
        user = models.User.get_by_id(user_id)

        print(user.name + "'s products:")

        for product in query:
            print(product.name)
    else:
        print('The user has no products or no valid id was given.')


def list_products_per_tag(tag_id=int):
    query = models.Product.select().join(models.ProductTag).join(models.Tag).where(models.Tag.id == tag_id)

    if query:
        tag = models.Tag.get_by_id(tag_id)

        print('All products associated with ' + tag.name + ':')

        for product in query:
            print(product.name)
    else:
        print('The tag has no associated products or no valid id was given.')


def add_product_to_catalog(user_id=int, product=models.Product):
    user = models.User.get_by_id(user_id)

    product.owner = user

    product.save()

    print(product.name + ' with the id of ' + str(product.id) + ' owned by ' + user.name + ' was stored in the database.')


def update_stock(product_id=int, new_quantity=int):
    product = models.Product.get_by_id(product_id)

    old_stock = product.quantity

    product.quantity = new_quantity
    product.save()

    print(product.name + ' used to have ' + str(old_stock) + ' in stock. New stock is: ' + str(product.quantity) + '.')


def purchase_product(product_id=int, buyer_id=int, quantity=int):
    product = models.Product.get_by_id(product_id)
    buyer = models.User.get_by_id(buyer_id)

    if buyer.id == product.owner:
        print('You cannot buy products from yourself ' + buyer.name + '.')
        return

    if quantity >= product.quantity:
        print('Not enough ' + product.name + ' in stock.')
        return

    total_price = round(product.price * quantity, 2)

    transaction = models.Transaction.create(
        buyer = buyer.id,
        bought_product = product.id,
        quantity = quantity,
        total_price = total_price,
        bought_at = datetime.now()
    )

    print('At ' + str(transaction.bought_at) + ', ' + buyer.name + ' bought ' + str(transaction.quantity) + ' of ' + product.name + ' at a total price of: €' + str(transaction.total_price) + '.')

    new_quantity = product.quantity - quantity

    update_stock(product.id, new_quantity)


def remove_product(product_id):
    product = models.Product.get_by_id(product_id)

    print('Deleting ' + product.name + ' from the database.')
    product.delete_instance()


def main():
    # Initial database
    models.init()
    print('')

    # Test Data
    models.test_data()
    print('')

    # Search
    search('guitar')
    print('')

    # List Paul's Products
    list_user_products(2)
    print('')

    # List all products tagged with 'electric'
    list_products_per_tag(1)
    print('')

    # Paul starts selling new product mouthharp!
    product = models.Product(name='Mouthharp', description='Great handmade mouthharp', price=7.50, quantity=20)
    add_product_to_catalog(2, product)
    print('')

    # List Pauls' Products again
    list_user_products(2)
    print('')

    # Update the stock quantity of a product
    update_stock(3, 5)
    print('')

    # Handle a purchase between a buyer and a seller for a given product
    purchase_product(1, 2, 2)
    print('')

    # And remove a product
    remove_product(6)
    print('')

    # Search for something authentic
    search('handmade')
    print('')


if __name__ == '__main__':
    main()