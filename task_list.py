tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# def uncompleted_tasks(list, completed):
#     uncompleted = []
#     for task in list:
#         if task["completed"] == False:
#             uncompleted.append(task)
#     return uncompleted

# print(uncompleted_tasks(tasks, False))

# def completed_tasks(list, completed):
#     completed = []
#     for task in list:
#         if task["completed"] == True:
#             completed.append(task)
#     return completed

# print(completed_tasks(tasks, True))

# def task_descriptions(list):
#     task_description = []
#     for task in list:
#             task_description.append(task["description"])
#     return task_description

# print(task_descriptions(tasks))

# def task_time(list):
#     task_time = []
#     for task in list:
#         if task["time_taken"] > 0:
#             task_time.append(task)
#     return task_time

# print(task_time(tasks))

# def given_description(list, description):
#     given_description = []
#     for task in list:
#         if task["description"] == "Wash Dishes":
#             given_description.append(task)
#     return given_description

# print(given_description(tasks, "Wash Dishes"))

# tasks[3]["completed"] = True
# print(tasks)

# tasks.append({
#   "description": "Do Laundry",
#   "completed": True,
#   "time_taken": 15
# })
# print(tasks)

