
first_stop = 0.3
second_go = 0.4
step_size = 0.1
current_increment = int(input('Enter current increment: \n'))

distance_travel = current_increment * step_size
print(distance_travel)
if distance_travel == 0.3:
    print('Stop the first stage!')
elif distance_travel == 0.4:
    print('Start the second stage!')
else:
    print('No action required at this point.')
# The program only reacted to the number 4, where is
# printed out Start the second stage. When 3 was input
# the value after multiplying was 0.30000000000000004
# else was activated most of the time

