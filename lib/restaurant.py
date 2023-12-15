class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_value = name
        self.reviews_list = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name_value

    def get_reviews(self):
        return self.reviews_list

    def get_customers(self):
        return list({review.get_customer() for review in self.reviews_list})

    def average_rating(self):
        ratings_sum = sum(review.get_rating() for review in self.reviews_list)
        reviews_count = len(self.reviews_list)
        
        if reviews_count > 0:
            return ratings_sum / reviews_count
        else:
            return 0

    @classmethod
    def get_all_restaurants(cls):
        return cls.all_restaurants