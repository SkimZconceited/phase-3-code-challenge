class Review:
    
    all_reviews_list = []  
    
    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self.rating_value = rating
        restaurant.reviews.append(self)  
        customer.reviews.append(self)  
        Review.all_reviews_list.append(self)

    def get_customer(self):
        return self.customer_obj

    def get_restaurant(self):
        return self.restaurant_obj

    def get_rating(self):
        return self.rating_value

    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews_list