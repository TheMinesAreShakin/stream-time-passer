'''
    Tool to pass the time on stream.
    Copyright (C) 2022  theMinesAreShakin

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''


# modules are singleton by definition aparrently
import time

wait_type = ""
timer_length_minutes = 0
timer_length_seconds = 0
timer_seconds_left = 0
did_tina_chat = False
tina_last_dialog = ""
did_andy_rage = False


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


def set_did_tina_chat_true(dialog):
    global did_tina_chat
    global tina_last_dialog
    did_tina_chat = True
    tina_last_dialog = dialog


def get_did_tina_chat():
    global did_tina_chat
    global tina_last_dialog
    if did_tina_chat:
        did_tina_chat = False
        return True, tina_last_dialog
    else:
        return False, ""


def set_did_andy_rage_true():
    global did_andy_rage
    did_andy_rage = True


def get_did_andy_rage():
    global did_andy_rage
    if did_andy_rage:
        did_andy_rage = False
        return True
    else:
        return False


def update():
    global timer_seconds_left
    timer_seconds_left -= 1