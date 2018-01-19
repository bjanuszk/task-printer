import task
from PIL import Image

task_1 = task.Task('MPI-1717','Create /filters endpoint and update postman collection','6')
task_2 = task.Task('MPI-1717','Create business logic to handle user request','8')
task_3 = task.Task('MPI-1717','Performance testing','8')

img_1 = task.create_task_rectangle(task_1)
img_2 = task.create_task_rectangle(task_2)
img_3 = task.create_task_rectangle(task_3)
images = [img_1,img_2,img_3]

task.mergeImages(images)

print('success')