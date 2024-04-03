# simple class to represent a dataset and add methods for basic data calculations.

class DataSet:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        sorted_data = sorted(self.data)
        n = len(self.data)
        middle = n // 2
        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]


# To call a class method, you use the class name, followed by a dot, and then the method name like this:
ClassName.method_name()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self, loudness):
        print(f"{self.name} speaks {'loudly' if loudness else 'softly'}!")

# Creating an instance of the person class
p1 = Person(name="John", age=40)

# Using the voice method with parameters
p1.voice(loudness=True) 




class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Creating instances with and without specifying the radius
small_circle = Circle()          # Uses default radius of 1
large_circle = Circle(radius=5)  # Specifies a radius of 5

print("Area of small circle:", small_circle.area())  
print("Area of large circle:", large_circle.area())  
              
# Relevance to Data Science
# As you step into the world of data science, methods and parameters become your crafty companions. They allow you to tailor your tools for specific data tasks and make your helpers adaptable and versatile. Let's extend our dataset class to have a method that detects outliers with a customizable threshold.

class DataSet:
    def __init__(self, data):
        self.data = data

    def detect_outliers(self, threshold=2):
        mean_value = sum(self.data) / len(self.data)
        std_dev = (sum((x - mean_value) ** 2 for x in self.data) / len(self.data)) ** 0.5
        return [x for x in self.data if abs(x - mean_value) > threshold * std_dev]

# Usage
data_set = DataSet([15, 20, 25, 30, 100])
outliers = data_set.detect_outliers(threshold=1.5)

another_data_set = DataSet([50, 60, 70, 80, 90])

# Using the Same Method with Different Parameters
outliers_another = another_data_set.detect_outliers(threshold=2)
        
