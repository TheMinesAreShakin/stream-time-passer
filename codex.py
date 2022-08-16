# modules are singleton by definition aparrently
import time

wait_type = ""
timer_length_minutes = 0
timer_length_seconds = 0
timer_seconds_left = 0


def __user_wait_type():
    global wait_type
    while True:
        wait_type = input("Enter the wait type (S)tarting or (B)rb: ").upper()
        if wait_type in ("S", "B"):
            return
        else:
            print("Please enter 'S' or 'B' for the type.")
            continue


def __user_timer_length():
    global timer_length_minutes, timer_length_seconds, timer_seconds_left
    while True:
        try:
            timer_length_minutes = int(input("Enter the timer length in minutes: "))
            if timer_length_minutes <= 0:
                print("Enter a time greater than 0 please.")
                continue
            else:
                break
        except ValueError:
            print("Invalid Input")
    timer_length_seconds = timer_length_minutes * 60
    timer_seconds_left = timer_length_seconds


def user_setup():
    __user_wait_type()
    __user_timer_length()


def get_time_int():
    return int(time.time())


def get_time_seconds_left():
    return timer_seconds_left


def get_time_minsec_str(include_minus=True):
    out = ""
    if timer_seconds_left >= 0:
        minutes = timer_seconds_left // 60
        seconds = timer_seconds_left % 60
        out += "{}:{:0>2}".format(minutes, seconds)
    else:
        if include_minus:
            out += "-"
        minutes = abs(timer_seconds_left) // 60
        seconds = abs(timer_seconds_left) % 60
        out += "{}:{:0>2}".format(minutes, seconds)
    return out


def get_time_min_str(include_minus=True):
    out = ""
    if timer_seconds_left >= 0:
        minutes = timer_seconds_left // 60
        out += str(minutes)
    else:
        if include_minus:
            out += "-"
        minutes = abs(timer_seconds_left) // 60
        out += str(minutes)
    return out


def get_wait_type():
    return wait_type


def update():
    global timer_seconds_left
    timer_seconds_left -= 1