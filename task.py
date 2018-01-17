from PIL import Image
from PIL import ImageDraw

class Task(object):
    def __init__(self, user_story, description, estimate):
        self.user_story = user_story
        self.description = description
        self.estimate = estimate

    def __str__(self):
        return 'User story: %s, description: %s, estimate: %s' % (self.user_story, self.description, self.estimate)

WHITE_RGB = (255, 255, 255)
UNIT_HEIGTH = 140
UNIT_WIDTH = 297

def create_task_rectangle():
    UNIT_HEIGTH = 140
    UNIT_WIDTH = 297

    img = Image.new('RGB', (UNIT_WIDTH, UNIT_HEIGTH), color=WHITE_RGB)
    draw = ImageDraw.Draw(img)
    draw.rectangle(((0, 0), (UNIT_WIDTH-1, UNIT_HEIGTH-1)), outline='red')
    draw.text(((0, 0)), 'test \n dd', fill='black')
    img.show()

create_task_rectangle()
