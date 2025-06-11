import week1.output_tasks as wk1_output
import week1.input_tasks as wk1_input
import week2.math_tasks as wk2_math
import week3.loop_tasks as wk3_loops
import week4.module_tasks as wk4_module

def run_week_one():
    print("Which program in 'Week 1' do you wish to run?")
    response = input()
    if response == "simple_message":
        wk1_output.simple_message()
    elif response == "multiline_message":
        wk1_output.multiline_message()
    elif response == "name_input":
        wk1_input.name_input()

def run_week_two():
    print("Which program in 'Week 2' do you wish to run?")
    response = input()
    if response == "sum_two_numbers":
        wk2_math.sum_two_numbers()
    elif response == "area_circle":
        wk2_math.area_circle()

def run_week_three():
    print("Which program in 'Week 3' do you wish to run?")
    response = input()
    if response == "count_to_ten":
        wk3_loops.count_to_ten()
    elif response == "multiplication_table":
        wk3_loops.multiplication_table()

def run_week_four():
    print("Which program in 'Week 4' do you wish to run?")
    response = input()
    if response == "guess_number":
        wk4_module.play_guess_the_number()

def run():
    while True:
        print("What would you like to do?")
        print("[1] Run 'Week 1' programs")
        print("[2] Run 'Week 2' programs")
        print("[3] Run 'Week 3' programs")
        print("[4] Run 'Week 4' programs")
        print("[q] Quit")
        response = input()

        if response == "1":
            run_week_one()
        elif response == "2":
            run_week_two()
        elif response == "3":
            run_week_three()
        elif response == "4":
            run_week_four()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()
