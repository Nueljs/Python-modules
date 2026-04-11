import alchemy

alchemy.create_air()

try:
    alchemy.create_earth()
except AttributeError as e:
    print(e)
