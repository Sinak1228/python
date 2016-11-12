class Unit:
    count = 0

    def __init__(self, name):
        Unit.count = Unit.count + 1
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        print("호로롤로")

class Hanzo(Unit):
    def speak(self):
        print("한조 대기중")

class Genji(Unit):
    def speak(self):
        print("겐지가 함께한다")

h1 = Hanzo("한조1")
g2 = Hanzo("한조2")
g1 = Genji("겐지1")
g2 = Genji("겐지2")

h1.move()
h1.speak()
g2.move()
g2.speak()

print("현재인구수:%d" % (Unit.count))
