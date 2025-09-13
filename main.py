import random
import time

print("Welcome to ReviseHelp")
choice = input("Press 1 for pomodoro timer, press 2 for random study tips, or press 3 for a revising timetable.")
if choice == '1':
    print("Pomodoro Timer")
    print("Start working for 25 minutes.")
    time.sleep(1500)
    print("Take a 5 minute break.")
    print(random.choice(tips))
    time.sleep(300)
    print("Now start working for 25 minutes again.")
    time.sleep(1500)
    print("Take another 5 minute break.")
    print(random.choice(tips))
    time.sleep(300)
    print("Now start working for another 25 minutes.")
    time.sleep(1500)
    print("Take another 5 minute break.")
    print(random.choice(tips))
    time.sleep(300)
    print("Now start working for one last 25 minutes.")
    time.sleep(1500)
    print("Now take a longer break of 15-30 minutes.")
elif choice == '2':
    print("Random Study Tips")
    tips = [
        "Take regular breaks to improve focus.",
        "Use active revision techniques.",
        "Teach the subject to someone else.",
        "Practice past exam papers under timed conditions.",
        "Stay hydrated."
    ]
    print("Here is a random study tip for you:")
    print(random.choice(tips))
elif choice == '3':
    print("Revising Timetable")
    daystiltest = int(input("How many days are left until the test? "))
    hrsperday = int(input("How many hours can you study each day? "))
    daysperweek = int(input("How many of those days can you study? "))
    daysperweek1 = daysperweek - (daysperweek * 0.2)
    daysperweek1 = round(daysperweek1)
    totalhrs = daysperweek1 * hrsperday
    totalhrs = totalhrs / daysperweek1
    totalhrs = round(totalhrs)
    print("You need to revise for", totalhrs, "hours per day, for", daysperweek1, "days a week.")
    print(random.choice(tips))
    print("Thank you for using revisehelp. (c) 2025, Hugo Robinson.")