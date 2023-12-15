from reviews import Review

class Customer:
    all_customers_list = []  # Class variable to keep track of all customers

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_reviews = []  # List to store customer reviews
        Customer.all_customers_list.append(self)  # Add the customer to the list of all customers

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_restaurants(self):
        return list({review.restaurant for review in self.customer_reviews})

    def add_customer_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.customer_reviews.append(new_review)

    @classmethod
    def get_all_customers(cls):
        return cls.all_customers_list

    def get_num_reviews(self):
        return len(self.customer_reviews)

    @classmethod
    def find_customer_by_name(cls, name):
        for customer in cls.all_customers_list:
            if customer.get_full_name().lower() == name.lower():
                return customer
        return None

    @classmethod
    def find_all_customers_by_first_name(cls, name):
        return [customer for customer in cls.all_customers_list if customer.get_first_name().lower() == name.lower()]