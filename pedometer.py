class Pedometer:
    def __init__(self, date: str):
        self.date = date
        self.steps = 0

    def incrementSteps(self):
        self.steps += 1

    def __str__(self):
        return f"Am {self.date} bin ich {self.steps} Schritte Gelaufen."

# Testprogramm
if __name__ == "__main__":
    # Test 1
    pedometer1 = Pedometer("11.11.2011")
    for _ in range(1111):
        pedometer1.incrementSteps()
    print(pedometer1)

    # Test 2
    pedometer2 = Pedometer("1.9.2017")
    for _ in range(10000):
        pedometer2.incrementSteps()
    print(pedometer2)
