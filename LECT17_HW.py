from abc import ABC, abstractmethod


class Meal:
    def __init__(self):
        self.main_course = None
        self.drink = None
        self.dessert = None

    def __str__(self):
        return f"Main course: {self.main_course}, Drink: {self.drink}, Dessert: {self.dessert}"


class MealBuilder(ABC):
    @abstractmethod
    def main_course(self):
        pass

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def dessert(self):
        pass

    @abstractmethod
    def get_meal(self):
        pass


# ==================================================================#
class ItalianMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def main_course(self):
        self.meal.burger = "Pizza"

    def drink(self):
        self.meal.drink = "Red Wine"

    def dessert(self):
        self.meal.dessert = "Tiramisu"

    def get_meal(self):
        return self.meal


# ==================================================================#
class AmericanMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def main_course(self):
        self.meal.burger = "Cheeseburger"

    def drink(self):
        self.meal.drink = "Cola"

    def dessert(self):
        pass  # No dessert

    def get_meal(self):
        return self.meal


# ==================================================================#
class Waiter:
    def __init__(self):
        self.meal_builder = None

    def set_builder(self, builder):
        self.meal_builder = builder

    def construct_meal(self):
        self.meal_builder.main_course()
        self.meal_builder.drink()
        self.meal_builder.dessert()

    def get_meal(self):
        return self.meal_builder.get_meal()


# ==================================================================#
if __name__ == "__main__":
    waiter = Waiter()

    italian_builder = ItalianMealBuilder()
    waiter.set_builder(italian_builder)

    waiter.construct_meal()
    meal = waiter.get_meal()
    print("Italian Meal:", meal)

    # ============================#
    american_builder = AmericanMealBuilder()
    waiter.set_builder(american_builder)

    waiter.construct_meal()
    meal = waiter.get_meal()
    print("American Meal:", meal)
