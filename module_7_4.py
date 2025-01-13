# https://github.com/SergeyFungus/HomeWork/blob/main/module_7_4.py

team1_name = input('Введите название первой команды: ')
team1 = input('Введите через пробел кол-во участников, кол-во решённых задач и итоговое время:\n')
team1 = team1.split()
team2_name = input('Введите название второй команды: ')
team2 = input('Введите через пробел кол-во участников, кол-во решённых задач и итоговое время:\n')
team2 = team2.split()

team1_num = int(team1[0])
team2_num = int(team2[0])
score_1 = int(team1[1])
score_2 = int(team2[1])
team1_time = float(team1[2])
team2_time = float(team2[2])
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 2)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'победа команды {team2_name}!'
else:
    challenge_result = 'ничья!'


print("В команде %s участников: %s !" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num) )
print("Команда {1} решила задач: {0} !".format(score_2,team2_name))
print("{} решили задачи за {} с !".format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")