class Kettle(object):

    powerSource = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switchOn(self):
        self.on = True


kenwood = Kettle("Kenwood", 100)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 50.50
print(kenwood.price)

hamilton = Kettle("Hamilton", 200)

print(f"Models: {kenwood.make} = {kenwood.price} | {hamilton.make} = {hamilton.price}")

print("Models: {0.make} = {0.price} | {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switchOn()
print(hamilton.on)

Kettle.switchOn(kenwood)
print(kenwood.on)

print("+" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switch to atomic power")
Kettle.powerSource = "atomic"
print(Kettle.powerSource)
print("Switch kenwood to gas")
kenwood.powerSource = "gas"
print(kenwood.powerSource)
print(hamilton.powerSource)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)



