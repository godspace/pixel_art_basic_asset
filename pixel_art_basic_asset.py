import turtle

pixel_size = 20
pixel_scale = 2
real_size = pixel_size*pixel_scale

map_w = 16
map_h = 16

screen = turtle.Screen()
screen.setup(map_w*real_size, map_h*real_size)
screen.tracer(0)

pixel_list = []

for j in range(-map_h//2,map_h//2+1):
    for i in range(-map_w//2, map_w//2+1):
        pixel = turtle.Turtle()
        pixel.speed(0)
        pixel.penup()
        pixel.shape("square")
        pixel.shapesize(pixel_scale)
        pixel.color("black","white")
        pixel.setpos(i*real_size, j*real_size)
        pixel.i = i
        pixel.j = j
        pixel_list.append(pixel)

def get_pixel(event):
    mx, my = event.x, event.y
    mx = round((mx - map_w/2*real_size)/real_size)
    my = round((-my + map_h/2*real_size)/real_size)
    print('{}, {}'.format(mx, my))
    for pixel in pixel_list:
        x = round(pixel.xcor()/real_size)
        y = round(pixel.ycor()/real_size)
        if x == mx and y == my:
            return pixel

def fill(event):
    pixel = get_pixel(event)
    pixel.color("blue","red")
    screen.update()

def clear(event):
    pixel = get_pixel(event)
    pixel.color("black","white")
    screen.update()

canvas = turtle.getcanvas()
canvas.bind('<B1-Motion>', fill)
canvas.bind('<B3-Motion>', clear)

screen.update()
screen.mainloop()