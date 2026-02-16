#With list
# def log_action(action, logs=None):
#     if logs is None:
#         logs = []
#     logs.append(action)
#     return logs
#
# print(log_action("hfjdjj",[]))
# print(log_action("akfhdw",[]))
#With dict
def log_action_dict(action, logs=None):
    if logs is None:
        logs = {}
    logs[action] = 123
    return logs
print(log_action_dict("hfjdjj",{}))