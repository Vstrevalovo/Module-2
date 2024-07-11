def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    length = len(string)
    UpStr = string.upper()
    LwStr = string.lower()
    result = (length, UpStr, LwStr)
    return result
def is_contains(string, list):
    count_calls()
    for i in range(len(list)):
        list[i] = list[i].lower()
    if string.lower() in list:
        return True
    else:
        return False

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)