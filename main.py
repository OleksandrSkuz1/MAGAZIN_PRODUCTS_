if __name__ == '__main__':

   # створюємо словник 'products' з назвою товарів та їх ціною

    products = [
        {
         'fruit': 'Orange',
         'price': 10
        },

        {
        'fruit': 'Banana',
        'price': 20
        },

        {
        'fruit': 'Kiwi',
        'price': 25
    },

        {
        'fruit': 'Apple',
        'price': 15
        },

        {
        'fruit': 'Сherry',
        'price': 30 
        }
    ]

fruit_choice = float(input())
sum = 0
for i in range(fruit_choice):
    x = float(input())
    sum += x
    print(sum)



    #    shopping_cart = []
    #
    # total_price = input()
    #    balance = 0
    #      while balance >= 100:
    #          balance += 1
    #
    #          balance = 100
    #          print(shopping_cart)

