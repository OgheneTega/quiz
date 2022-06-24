from question import Question
import time
import datetime
import threading
import os
import signal


def countdown_timer():
    global total_seconds
    global timer
    total_seconds = 10
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)

        time.sleep(1)
        total_seconds -= 1
        print(total_seconds, end="\r")
    print("*" * 40)
    print("Countdown has reached zero seconds")
    print(
        "You correctly answered "
        + str(score)
        + "/"
        + str(len(question_prompts))
        + " questions"
    )
    os.kill(os.getpid(), signal.SIGINT)
    exit()


qa = [
    "What is the capital of Ukraine? \n(a) Kiev\n(b) Keiv\n(c) Kive\n\n",
    "How many vowels are there in the word 'alphabet'? \n(a) 2\n(b) 3\n(c) 4\n\n",
    "Who is the captain of the Silent Mary?\n(a) Captain Salazar\n(b) Captain Barbossa\n(c) Captain Blackbeard\n\n",
]

question_prompts = [Question(qa[0], "a"), Question(qa[1], "a"), Question(qa[2], "a")]

countdown_thread = threading.Thread(target=countdown_timer)
countdown_thread.start()


def assessment(questions):
    global score
    score = 0
    attempts = 0
    count = len(question_prompts)

    for question in questions:
        answer = input(question.question)
        if total_seconds <= 0:
            print("You are out of time")
            break
        elif answer == question.answer:
            score += 1
        attempts += 1

        if attempts == count and total_seconds > 0:
            print(
                "You correctly answered "
                + str(score)
                + "/"
                + str(len(question_prompts))
                + " questions"
            )
            os.kill(os.getpid(), signal.SIGINT)
            exit()

    print(
        "You correctly answered "
        + str(score)
        + "/"
        + str(len(question_prompts))
        + " questions"
    )


assessment(question_prompts)


# stopwatch
# start_time = time.time()
# last_time = start_time
# lap_num = 1
# value = ""

# print("Press ENTER for each lap.\nType Q and press ENTER to stop.")
# while value.lower() != "q":
#     value = input()
#     lap_time = round(time.time() - last_time, 2)
#     total_time = round(time.time() - start_time, 2)
#     print("Lap number is:", lap_num)
#     print("Total time is:", total_time)
#     print("Lap time is:", lap_time)
#     print("*" * 20)

#     last_time = time.time()
#     lap_num += 1
# print("Exercise complete!!!")


# time.sleep(10)
