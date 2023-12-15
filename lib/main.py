#!/usr/bin/env python3
from customers import Customer
from restaurant import Restaurant
from reviews import Review



def main():
    # Instantiate some customers, restaurants, and reviews
    customer1 = Customer("Cristiano", "Ronaldo")
    customer2 = Customer("Alejandro", "Garnacho")

    restaurant1 = Restaurant("Goat place")
    restaurant2 = Restaurant("Bicycle kick wings")

    review1 = Review(customer1, restaurant1, 2)
    review2 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(customer1.get_full_name())
    print(restaurant2.average_rating())
    print(customer2.get_num_reviews())

    print(vars(review1))
    print(vars(review2))

# This will run the program automatically
if __name__ == '__main__':
    main()