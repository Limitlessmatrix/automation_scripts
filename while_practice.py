#This will be a practice of while loops trying to use them in real world problems.
#
def average(number_1, number_2, total):
    return ((int(number_1) + int(number_2)) / total) 
average(2, 4543, 2)

#better way to get averages
#take into consideration lists of numbers, and dictionaries
#Any other common data types you might be messing with

loop_1 = 1
while (loop_1 <= 23):
    print(loop_1)
    loop_1= loop_1 + 1

# while loop in a function
#def run_commands():

#    your_input = 29
#    your_input = your_input + 1
#    print(your_input)

#while(your_input <=70):
#    run_commands()

#google crash course examples
#

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)