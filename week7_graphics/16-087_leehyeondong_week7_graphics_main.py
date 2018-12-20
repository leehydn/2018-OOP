from cs1graphics import *
from cs1media import *
import time
import math


paper = Canvas(500, 312, bgColor="skyBlue", title="Super Mario")

num_frame = 4
mario_1 = load_picture("./sprite/mario_1.png")
mario_2 = load_picture("./sprite/mario_2.png")
mario_3 = load_picture("./sprite/mario_3.png")
mario_4 = load_picture("./sprite/mario_4.png")

spriteArr = [mario_1, mario_2, mario_3, mario_4]
pic_size = mario_1.size()
orig_pixel_size = 8

pixel_color = [[] for x in range(num_frame)]

pixels = []
width = pic_size[0] // orig_pixel_size
height = pic_size[1] // orig_pixel_size
num_pixel = width*height
pixel_size = 3
start_point = (30, 100)
background_color = (255,0,255)

for i in range(num_frame):
  for y in range(pic_size[1] // orig_pixel_size):
    for x in range(pic_size[0] // orig_pixel_size):
      refpt_x = int((x + 0.5) * orig_pixel_size)
      refpt_y = int((y + 0.5) * orig_pixel_size)
      pixel_color[i].append(spriteArr[i].get(refpt_x, refpt_y))


def isSame(a, b, r):
  return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) < r;

def printing(index, depth, start_point = start_point):
  layer = Layer()

  for i in range(num_pixel):
    delta_x = i % width
    delta_y = i // width

    newPixel = Square(pixel_size, centerPt=Point(start_point[0]+delta_x*pixel_size,
                                                 start_point[1]+delta_y*pixel_size))

    if isSame(pixel_color[index][i], background_color, 50): #if background
      continue

    else:
      newPixel.setBorderColor(pixel_color[index][i])
      newPixel.setFillColor(pixel_color[index][i])
      layer.add(newPixel)

    layer.setDepth(depth)
  return layer


layerArr = []

for i in range(num_frame):
  layerArr.append(printing(i, 100-10*i))

"""for i in range(len(layerArr)):
  paper.add(layerArr[i])
  time.sleep(0.2)
  #paper.remove(layerArr[i])
"""

"""paper.add(layerArr[0])
#time.sleep(0.1)


layerArr[1].move(30,0)
paper.add(layerArr[1])
paper.remove(layerArr[0])
#time.sleep(0.1)


layerArr[2].move(60,0)
paper.add(layerArr[2])
paper.remove(layerArr[1])
#time.sleep(0.1)


layerArr[3].move(90,0)
paper.add(layerArr[3])
paper.remove(layerArr[2])
#time.sleep(0.1)
#paper.remove(layerArr[3])
"""

"""paper.add(layerArr[2])
time.sleep(0.05)
paper.remove(layerArr[2])

paper.add(layerArr[3])
time.sleep(0.05)
paper.remove(layerArr[3])
"""

"""for size in range(1, 11):
  sprite_layer = Layer()
  pixel_size = size;
  layerArr.append(printing(sprite_layer))



paper.add(layerArr[0])
for i in range(1, 10):
  paper.remove(layerArr[i-1])
  paper.add(layerArr[i])
  time.sleep(0.2)
"""

def move(t, gap):
    paper.add(layerArr[0])

    layerArr[1].move(pixel_size*gap,0)
    paper.add(layerArr[1])
    paper.remove(layerArr[0])

    layerArr[2].move(pixel_size*gap*2,0)
    paper.add(layerArr[2])
    paper.remove(layerArr[1])

    layerArr[3].move(pixel_size*gap*3,0)
    paper.add(layerArr[3])
    paper.remove(layerArr[2])

    for i in range(t):
      layerArr[0].move(pixel_size*gap*4,0)
      paper.add(layerArr[0])
      paper.remove(layerArr[3])

      layerArr[1].move(pixel_size*gap*4,0)
      paper.add(layerArr[1])
      paper.remove(layerArr[0])

      layerArr[2].move(pixel_size*gap*4,0)
      paper.add(layerArr[2])
      paper.remove(layerArr[1])

      layerArr[3].move(pixel_size*gap*4,0)
      paper.add(layerArr[3])
      paper.remove(layerArr[2])

ground = Rectangle(500, 314, Point(250, 343))
box = Rectangle(40, 60, Point(350, 160))
top = Rectangle(50, 12, Point(350, 125))
text = Text("버섯친구", fontsize=10, centerPt=Point(300, 180))
text.setDepth(5)
text.setFontColor("white")

scene = Rectangle(500, 312, Point(250, 156))
scene.setBorderColor("black")
scene.setFillColor("black")
scene.setDepth(1)

scene0 = Rectangle(500, 312, Point(250, 156))
scene0.setBorderColor("red")
scene0.setFillColor("red")
scene0.setDepth(2)

text_dead = Text("YOU ARE DEAD", fontsize=30, centerPt=Point(250, 156))
text_dead.setDepth(0)
text_dead.setFontColor("white")

text1 = Text("호그와트", centerPt=Point(460, 115))
text1.setDepth(5)
text1.setFontColor("white")

house = Rectangle(100, 150, Point(460, 115))
house.setFillColor("black")

mush = Circle(radius=18, centerPt=Point(300, 180))
mush.setFillColor((92, 59, 0))

ground.setFillColor("chocolate3")
ground.setBorderColor("chocolate3")
box.setBorderColor("black")
box.setFillColor("green2")
top.setBorderColor("black")
top.setFillColor("green2")
paper.add(ground)
paper.add(box)
paper.add(top)
paper.add(text)
paper.add(mush)
paper.add(house)
paper.add(text1)

move(4,3)

def jump(gap):
  layerArr[0].move(pixel_size*gap*4,0)
  paper.add(layerArr[0])
  paper.remove(layerArr[3])

  layerArr[1].move(pixel_size*gap*4,-pic_size[1]*0.4)
  paper.add(layerArr[1])
  paper.remove(layerArr[0])

  layerArr[2].move(pixel_size*gap*4,-pic_size[1]*0.2)
  paper.add(layerArr[2])
  paper.remove(layerArr[1])

  layerArr[3].move(pixel_size*gap*4,pic_size[1]*0.2)
  paper.add(layerArr[3])
  paper.remove(layerArr[2])

  layerArr[0].move(pixel_size*gap*4,pic_size[1]*0.4)
  paper.add(layerArr[0])
  paper.remove(layerArr[3])


jump(5)
paper.add(scene0)
time.sleep(0.1)
paper.add(scene)
paper.add(text_dead)
