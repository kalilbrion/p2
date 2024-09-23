from datetime import datetime
import random
import time

# Список с нечётными минутами
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 
        33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# Дополнительные сообщения
odd_messages = [
    "This minute feels quite odd!",
    "An odd minute has come!",
    "Seems like an odd time to check!",
    "It's an odd minute now!",
    "Odd minutes are mysterious!",
    "Another odd minute is here!"
]

even_messages = [
    "Not an odd minute, maybe next time.",
    "It's an even minute, nothing strange here.",
    "Waiting for an odd minute... try again later.",
    "Looks like a normal minute!",
    "Even minutes are pretty boring, aren't they?",
    "Everything seems even and stable."
]

# Сообщения в зависимости от времени суток
morning_messages = [
    "Good morning! Odd minutes feel different in the morning.",
    "Early risers catch odd minutes!",
    "Morning odd minutes are refreshing."
]

afternoon_messages = [
    "Afternoon odd minutes are a perfect time for a break.",
    "Odd minutes help break up the day in the afternoon."
]

evening_messages = [
    "Odd minutes in the evening bring peace.",
    "Evening odd minutes help wind down the day."
]

night_messages = [
    "Odd minutes at night feel extra mysterious!",
    "Nighttime odd minutes are rare, but special."
]

# Новые элементы программы
special_minute_messages = {
    0: "Midnight magic! You're here at the start of a new day!",
    30: "Half-past the hour, and the world feels balanced.",
    15: "Quarter past! An interesting time to reflect.",
    45: "Quarter to the next hour, the day is moving fast!"
}

# Дополнительные действия при попадании в особые минуты
def check_special_minute(minute):
    if minute in special_minute_messages:
        print(special_minute_messages[minute])
    elif minute % 10 == 0:
        print(f"Another full ten-minute mark has passed: {minute:02d} minutes.")
    else:
        print("Nothing special about this minute...")

# Функция для проверки времени суток
def get_time_of_day():
    current_hour = datetime.today().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "afternoon"
    elif 17 <= current_hour < 21:
        return "evening"
    else:
        return "night"

# Функция для получения сообщения в зависимости от времени суток
def get_time_of_day_message():
    time_of_day = get_time_of_day()
    
    if time_of_day == "morning":
        return random.choice(morning_messages)
    elif time_of_day == "afternoon":
        return random.choice(afternoon_messages)
    elif time_of_day == "evening":
        return random.choice(evening_messages)
    else:
        return random.choice(night_messages)

# Дополнительная функция для генерации случайных советов
advice_list = [
    "Take a deep breath, sometimes odd minutes require patience.",
    "An odd minute is a good time to stand up and stretch!",
    "Use this time to think of one thing you're grateful for.",
    "Odd minutes remind us that time is always moving, make the most of it!",
    "This odd minute could be a chance to plan something exciting."
]

def get_random_advice():
    return random.choice(advice_list)

# Новая логика для специального события
def special_event_check():
    current_hour = datetime.today().hour
    if current_hour == 0:
        print("Special event! It's midnight, the start of a brand new day!")
    elif current_hour == 12:
        print("It's noon, the midpoint of the day!")
    elif current_hour == 6:
        print("The day has begun! Time to catch some odd minutes!")
    elif current_hour == 18:
        print("The evening has begun! Let's check for odd minutes during sunset!")

# Функция для проверки минуты
def check_minute_status():
    right_this_minute = datetime.today().minute
    current_hour = datetime.today().hour
    special_event_check()  # Проверка на специальные события
    
    if right_this_minute in odds:
        time_of_day_message = get_time_of_day_message()
        odd_message = random.choice(odd_messages)
        print(f"[{current_hour:02d}:{right_this_minute:02d}] {odd_message}")
        print(f"Additional note: {time_of_day_message}")
        print(f"Random advice: {get_random_advice()}")
    else:
        even_message = random.choice(even_messages)
        print(f"[{current_hour:02d}:{right_this_minute:02d}] {even_message}")
    check_special_minute(right_this_minute)

# Функция для выбора случайного времени ожидания на основе времени суток
def get_wait_time():
    time_of_day = get_time_of_day()
    if time_of_day == "morning":
        return random.randint(10, 30)  # Утром меньше ждать
    elif time_of_day == "afternoon":
        return random.randint(20, 40)
    elif time_of_day == "evening":
        return random.randint(30, 50)
    else:
        return random.randint(40, 60)  # Ночью ждать дольше

# Дополнительная функция для статистики
def calculate_statistics(odd_count, even_count):
    total_checks = odd_count + even_count
    odd_percentage = (odd_count / total_checks) * 100
    even_percentage = (even_count / total_checks) * 100
    
    print("\n--- Statistics Report ---")
    print(f"Total checks: {total_checks}")
    print(f"Odd minutes: {odd_count} ({odd_percentage:.2f}%)")
    print(f"Even minutes: {even_count} ({even_percentage:.2f}%)")
    print("-------------------------")

# Основной цикл программы
def run_time_checker():
    odd_minute_counter = 0  # Счётчик нечётных минут
    even_minute_counter = 0  # Счётчик чётных минут
    consecutive_odd_count = 0  # Подсчёт количества последовательных нечётных минут
    consecutive_even_count = 0  # Подсчёт количества последовательных чётных минут

    for i in range(25):  # Программа повторяется 25 раз
        right_this_minute = datetime.today().minute
        check_minute_status()
        
        if right_this_minute in odds:
            odd_minute_counter += 1
            consecutive_odd_count += 1
            consecutive_even_count = 0  # Сброс чётных минут
        else:
            even_minute_counter += 1
            consecutive_even_count += 1
            consecutive_odd_count = 0  # Сброс нечётных минут

        # Вывод предупреждений, если последовательность нечётных или чётных минут слишком длинная
        if consecutive_odd_count >= 3:
            print("Warning: You've encountered 3 or more consecutive odd minutes!")
        if consecutive_even_count >= 3:
            print("Warning: You've encountered 3 or more consecutive even minutes!")
        
        wait_time = get_wait_time()
        print(f"Waiting for {wait_time} seconds before checking again...\n")
        time.sleep(wait_time)

    # Финальный отчёт
    calculate_statistics(odd_minute_counter, even_minute_counter)

# Приветственное сообщение с учётом времени суток
def welcome_message():
    time_of_day = get_time_of_day()
    if time_of_day == "morning":
        print("Good morning! Let's start checking for odd minutes!")
    elif time_of_day == "afternoon":
        print("Good afternoon! Ready to explore some odd minutes?")
    elif time_of_day == "evening":
        print("Good evening! Let's see if any odd minutes come our way.")
    else:
        print("Good night! Late-night odd minutes are always exciting!")

# Начало программы
welcome_message()
run_time_checker()
print("The time-checking process is complete. Hope you enjoyed the odd minutes!")  
