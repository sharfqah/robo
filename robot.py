class Robot:

    def __init__(self, name, color, battery_level):
        self.name = name
        self.color = color
        self.battery_level = battery_level

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"My color is {self.color} and my battery is at {self.battery_level}%.")

    def walk(self, steps):
        print(f"{self.name} is walking {steps} steps forward.")
        self.battery_level -= 5
        print(f"Battery is now at {self.battery_level}%.")

robo1 = Robot("Omega-4", "Silver", 100)
robo2 = Robot("Pixel", "Neon Blue", 80)

robo1.introduce()
print("-" * 30)
robo2.introduce()
print("-" * 30)
robo1.walk(10)