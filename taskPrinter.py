import task

task_1 = task.Task('MPI-1717', 'Create /filters endpoint and update postman collection', '6')
task_2 = task.Task('MPI-1717', 'Create business logic to handle user request', '8')
task_3 = task.Task('MPI-1717', 'Performance testing', '8')
task_4 = task.Task('MPI-1717', 'Performance testing', '8')
task_5 = task.Task('MPI-1717', 'UI testing', '4')
task_6 = task.Task('MPI-1717', 'Technical debt', '2')
task_7 = task.Task('MPI-1717', 'Backend improvements', '8')
task_8 = task.Task('MPI-1717', 'Coffee', '1')

img_1 = task.create_task_rectangle(task_1)
img_2 = task.create_task_rectangle(task_2)
img_3 = task.create_task_rectangle(task_3)
img_4 = task.create_task_rectangle(task_4)
img_5 = task.create_task_rectangle(task_5)
img_6 = task.create_task_rectangle(task_6)
img_7 = task.create_task_rectangle(task_7)
img_8 = task.create_task_rectangle(task_8)
images = [img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8]

image_with_8_tasks = task.mergeImages(images)
# image_with_8_tasks.save('test.png')
image_with_8_tasks.show()

print('success')
