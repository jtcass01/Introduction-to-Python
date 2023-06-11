# module example
import order as v

v.make_pizza(12, 'ham', 'pineapple', 'extra cheese', 'meatballs', 'anchovies')
v.make_sandwich(6, 'chicken', 'bacon', 'extra ranch')

from order import make_pizza, make_sandwich

make_pizza(12, 'ham', 'pineapple', 'extra cheese', 'meatballs', 'anchovies')
make_sandwich(6, 'chicken', 'bacon', 'extra ranch')
