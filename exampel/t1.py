from turtle import *

color('blue', 'yellow')
begin_fill()

while True:
    forward(100)
    left(100)

    if abs(pos()) < 1:
        break

end_fill()
done()
