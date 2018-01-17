from PIL import Image
from PIL import ImageDraw
from task import Task

WHITE_RGB = (255, 255, 255)

HEIGHT = 842
WIDTH = 595

UNIT_HEIGTH = 140
UNIT_WIDTH = 297

img = Image.new('RGB', (WIDTH, HEIGHT), color=WHITE_RGB)
draw = ImageDraw.Draw(img)
draw.rectangle(((0,0),(UNIT_WIDTH,UNIT_HEIGTH)),outline='black')
draw.text(((0,0)),'test \n dd',fill='black')

task = Task('a','b',2)
print(task)

# img.show()
# img.save('test.jpg')
print('success')