#!/usr/local/bin/python
# --*-- coding:utf-8 --*--

"""
data<->business logic<->presentation separation (strict relationships)
"""

class Data(object):

    """
    actual data store hold business data
    """

    products = {
        'milk': {'price': 1, 'quantity': 100},
        'egg': {'price': 2, 'quantity': 200},
        'cheese': {'price': 3, 'quantity': 300}
    }

    def __get__(self, obj, klass):
        print("fetching from data store")
        return {'products': self.products}


class BusinessLogic(object):

    """
    business logic that hold data store instance
    """

    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_info(self, product):
        return self.data['products'].get(product, None)


class UI(object):

    """
    UI that manipulate business logic
    """

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        for product in  self.business_logic.product_list():
            print( product )

    def get_product_info(self, product):
        product_info = self.business_logic.product_info(product)
        if product_info:
            print ('name: {name}, price: {price}, quantity: {quantity}'.format(name=product.title(),
                                                                               price=product_info.get('price',0),
                                                                               quantity=product_info.get('quantity',0)))
        else:
            print('That product "{0}" does not exist in the records'.format(product))


def main():
    ui = UI()
    ui.get_product_list()
    ui.get_product_info('cheese')
    ui.get_product_info('eggs')
    ui.get_product_info('milk')
    ui.get_product_info('arepas')

if __name__ == '__main__':
    main()
