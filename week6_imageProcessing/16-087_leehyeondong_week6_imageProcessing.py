from cs1media import *
import math
from typing import *

# Combine two images
rabbit = load_picture("./Photo/rabbit.jpg")
kouen = load_picture("./Photo/trees.jpg")
king = load_picture("./Photo/statue.jpg")
old_young = load_picture("./Photo/old_young.jpg")

  #Reduce the size

def scale_down(img: Picture, factor: int) -> Picture:
  w, h = img.size()
  w //= factor; h //= factor;

  result = create_picture(w, h)
  norm = factor ** 2

  for y in range(h):
    for x in range(w):
      r, g, b = 0, 0, 0
      x1 = x * factor
      y1 = y * factor
      for x0 in range(factor):
        for y0 in range(factor):
          r0, g0, b0 = img.get(x1+x0, y1+y0)
          r, g, b = r+r0, g+g0, b+b0

      r, g, b = r // norm, g // norm, b // norm
      result.set(x, y, (r, g, b))

  return result

def dist(c1, c2) -> float:
  r1, g1, b1 = c1; r2, g2, b2 = c2;
  return math.sqrt((r1-r2) ** 2 + (g1-g2) ** 2 + (b1-b2) ** 2)

def chroma_key(img: Picture, keyColor: tuple, threshold: int) -> None:
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      if dist(p, keyColor) < threshold:
        img.set(x, y, Color.yellow)

def paste(background, img, x1, y1) -> None:
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      background.set(x1+x, y1+y, img.get(x, y))

def chroma_paste(background, img, chroma, keyColor, threshold, x1, y1) -> None:
  w, h = img.size()
  chroma_key(img, chroma, threshold)
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      if p != keyColor:
        background.set(x1+x, y1+y, p)

def concat(imgList: list) -> Picture:
  w, h = 0, 0
  for img in imgList:
    w1, h1 = img.size()
    w += w1; h = max(h, h1)

  r = create_picture(w, h, Color.white)
  x0 = 0
  for img in imgList:
    w1, h1 = img.size()
    for y in range(h1):
      for x in range(w1):
        r.set(x0+x, y, img.get(x, y))
    x0 += w1

  return r

def interpolate(c1, c2, fac) -> tuple:
  r1, g1, b1 = c1
  r2, g2, b2 = c2

  return (round(r1 * fac + r2 * (1-fac)), round(g1 * fac + g2 * (1-fac)),\
  round(b1 * fac + b2 * (1-fac)))

# ###################

def question1():
  rabbit = load_picture("./Photo/rabbit.jpg")
  kouen = load_picture("./Photo/trees.jpg")

  small_rabbit = scale_down(rabbit, 12)
  chroma_paste(kouen, small_rabbit, (255, 255, 255), Color.yellow, 120, 240, 230)
  kouen.show()
def question2():
  old_young = load_picture("./Photo/old_young.jpg")
  w, h = old_young.size()
  old = create_picture(w // 2, h)
  young = create_picture(w // 2, h)

  for y in range(h):
    for x in range(w // 2):
      old.set(x, y, old_young.get(x, y))
      young.set(x, y, old_young.get(x + w // 2, y))

  num_slice = 8
  imgList = []
  gap = 1 / num_slice

  for i in range(num_slice):
    w, h = old.size()
    img = create_picture(w, h)
    for y in range(h):
      for x in range(w):
        old_data = old.get(x, y); young_data = young.get(x, y)
        img.set(x, y, interpolate(young_data, old_data, gap * i))

    imgList.append(img)

  concat(imgList).show()
def question3():
  mess = load_picture("./Photo/message.jpg")
  background = load_picture("./Photo/trees.jpg")
  message = scale_down(mess, 1)

  def change_rbg(img, isOdd: bool, p: tuple) -> tuple:
    r, g, b = img.get(p[0], p[1])
    if isOdd:
      r //= 2; r *= 2; r -= 1;
      g //= 2; g *= 2; g -= 1;
      b //= 2; b *= 2; b -= 1;
    else:
      r //= 2; r *= 2;
      g //= 2; g *= 2;
      b //= 2; b *= 2;

    return (r, g, b)

  def encrypt(img, background, pos_x, pos_y):
    w, h = img.size()
    w1, h1 = background.size()
    img_ = create_picture(w1, h1)

    for y in range(h1):
      for x in range(w1):
        img_.set(x, y, background.get(x, y))

    for y in range(h):
      for x in range(w):
        orig: tuple = background.get(pos_x + x, pos_y + y)
        if message.get(x, y) == Color.black:
          orig = change_rbg(background, True, (x, y))
          img_.set(pos_x + x, pos_y + y, orig)
        else:
          orig = change_rbg(background, False, (x, y))
          img_.set(pos_x + x, pos_y + y, orig)

    return img_

  def decrypt(background, x0, y0, size):
    w, h = background.size()
    img_ = create_picture(w, h, Color.white)
    for y in range(size[1]):
      for x in range(size[0]):
        if background.get(x+x0, y+y0)[0] % 2 == 1 and background.get(x+x0, y+y0)[1] % 2 == 1 and background.get(x+x0, y+y0)[2] % 2 == 1:
          img_.set(x+x0, y+y0, Color.black)

    return img_

  crypt = encrypt(message, background, 20, 30)
  crypt.show()
  decrypt(crypt, 20, 30, message.size()).show()
def question4():
  bono = load_picture("./Photo/bono.jpg")
  w, h = bono.size()

  #bono.show()
  color_set = [Color.red, Color.orange, Color.green, Color.blue, Color.purple, Color.black]
  img_list = []
  threshold = 240
  thres2 = 115
  color = None

  for y in range(h):
    for x in range(w):
      if dist(bono.get(x, y), Color.black) > threshold and dist(bono.get(x, y), Color.white) > threshold:
        color = bono.get(x, y)
        break


  for i in range(len(color_set)):
    img_ = load_picture("./Photo/bono.jpg")
    for y in range(h):
      for x in range(w):
        if dist(color, img_.get(x, y)) < thres2:
          img_.set(x, y, color_set[i])

    img_list.append(img_)

  concat(img_list).show()

question1()
question2()
question3()
question4()
