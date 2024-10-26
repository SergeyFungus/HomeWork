from logging.config import stopListening

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(stroka: str):
    count_calls()
    return (len(stroka), stroka.upper(), stroka.lower())

def is_contains(stroka, list_to_search):
    count_calls()
    stroka = stroka.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if stroka in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
