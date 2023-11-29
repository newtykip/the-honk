from datetime import datetime
from time import sleep
from random import choice
from string import ascii_letters

SLEEP_DURATION = 0.001

def get_time():
    return datetime.now()

def format_time(t: datetime):
    return '{}:{:0>2}:{}'.format(t.hour, t.minute, t.second + t.microsecond / 1000000)

def output(start_t: datetime, end_t: datetime):
    start = format_time(start_t)
    end = format_time(end_t)
    elapsed = end_t - start_t

    print(f"""Start Time: {start}
End Time: {end}
Time Taken: {elapsed}""")

def O_constant(n: int):
    start_t = get_time()
    
    # print(n)

    end_t = get_time()
    output(start_t, end_t)

def O_linear(n: int):
    start_t = get_time()

    for i in range(n):
        sleep(SLEEP_DURATION)
        # print(i)

    end_t = get_time()
    output(start_t, end_t)

def O_quadratic(n: int):
    start_t = get_time()

    for i in range(n):
        sleep(SLEEP_DURATION)
        # print(i)

        for j in range(n):
            sleep(SLEEP_DURATION)
            # print(j)

    end_t = get_time()
    output(start_t, end_t)

def O_cubic(n: int):
    start_t = get_time()

    for i in range(n):
        sleep(SLEEP_DURATION)
        # print(i)

        for j in range(n):
            sleep(SLEEP_DURATION)
            # print(j)
        
        for k in range(n):
            sleep(SLEEP_DURATION)
            # print(k)

    end_t = get_time()
    output(start_t, end_t)

def O_exponential(n: int):
    loop_count = 0
    p_words = ["".join(choice(ascii_letters) for _ in range(n)) for _ in range(n)]
    start_t = get_time()

    for i in range(n):
        for j in range(len(p_words[i])):
            sleep(SLEEP_DURATION)
            ascii_value = 97
            
            for _ in range(len(p_words[i])):
                print(f"""Checking {p_words[i]} position: {j}
Checking for {chr(ascii_value)}""")

                if p_words[i][j] == chr(ascii_value):
                    print(f"{chr(ascii_value)} was found at position {j}")

                ascii_value += 1
                loop_count += 1
            loop_count += 1
        loop_count += 1

    end_t = get_time()
    output(start_t, end_t)

def O_factorial(n: int, out: bool = True):
    if out:
        start_t = get_time()

    for _ in range(n):
        # print(n)
        O_factorial(n - 1, False)

    if out:
        end_t = get_time()
        output(start_t, end_t)

O_factorial(5)