from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

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
MARGIN = 5
MAX_LINE_LENGTH = 40

FONT_25 = ImageFont.truetype('Roboto-Black.ttf', 25)
FONT_20 = ImageFont.truetype('Roboto-Black.ttf', 20)
FONT_18 = ImageFont.truetype('Roboto-Black.ttf', 18)

def create_task_rectangle(task):
    UNIT_HEIGTH = 140
    UNIT_WIDTH = 297

    img = Image.new('RGB', (UNIT_WIDTH, UNIT_HEIGTH), color=WHITE_RGB)
    draw = ImageDraw.Draw(img)
    draw.rectangle(((0, 0), (UNIT_WIDTH - 1, UNIT_HEIGTH - 1)), outline='red')
    draw.text(((MARGIN, 0)), task.user_story, fill='black', font=FONT_25)
    __draw_description(draw, task.description)
    draw.text(((MARGIN, 110)), 'Left [h]: ' + task.estimate, fill='black', font=FONT_20)
    return img

def mergeImages(images):
    result = Image.new("RGB", (594, 840), color=WHITE_RGB)
    #TODO create images matrix
    result.paste(images[0],(0,0,UNIT_WIDTH,UNIT_HEIGTH))
    result.show()

def __draw_description(draw, text):
    wrapped_description = textwrap.wrap(text, MAX_LINE_LENGTH)
    for x in range(0, wrapped_description.__len__()):
        draw.text((MARGIN, (40 + (x * 15))), wrapped_description[x], fill='black', font=FONT_18)

# print(FONT_18.getsize('XX'))
