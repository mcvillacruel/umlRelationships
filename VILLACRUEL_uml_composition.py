# Composition
class Heart:
    pass

class Human:
    def __init__(self):
        self.heart = Heart()

# (Test)
person = Human()
print(hasattr(person, 'heart'))
