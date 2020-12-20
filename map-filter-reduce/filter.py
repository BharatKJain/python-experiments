number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# def func():
#     list_of_datapoints = [{
#         "fileName": "Check1",
#         "accExecutionStatus": False,
#         "prodExecutionStatus": False,
#         "devExecutionStatus": False,
#     }, {
#         "fileName": "Check2",
#         "accExecutionStatus": False,
#         "prodExecutionStatus": False,
#         "devExecutionStatus": False,
#     }]
#     fileName = "Check3"
#     if len(list(filter(lambda x: x["fileName"] != fileName, list_of_datapoints))) == len(list_of_datapoints):
#         print("This filename is not present in json")


# func()
