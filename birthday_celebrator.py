import time  #? to sleep
from datetime import datetime  #? birthday calculation
from datetime import date  #? learning today
import webbrowser as wb  #? url opering
from functools import wraps  #? decorator

#? getting birth date
date_of_birth = datetime.strptime(input(
    'Please, enter the "birthday" of whom will be celebrated by you: (dd.mm.yyyy): '), "%d.%m.%Y")
#? getting name and capitalize it
birthday_person = str(
    input('Please enter a "name" of whose birthday this is: ')).capitalize()


#? calculating age of the person
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


age = calculate_age(date_of_birth)
age_sec = datetime.now() - date_of_birth


#? celebration decorator
def celebrator(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        w_max = "*"*150
        print(f"{w_max}\t\n\t{orig_func(*args, **kwargs)}\t\n{w_max}")
    return wrapper


#? congratulatory address for birthday
@celebrator
def birthday(age):
    w_min = "*"*10
    return f"{w_min}Happy birthday, {birthday_person}! You've survived {age_sec.total_seconds()} seconds from now on. Have magnificent {age} with your loved ones{w_min}"


birthday(age) # Celebration starts here...
time.sleep(5) #! Thus, printed text can be read easily by everyone who is literated.

#? A final countdown!
for countdown in range(age, 0, -1):
    print(countdown)
    if age < 5:
        time.sleep(3.3) # you have more time
    elif 5 < age < 10:
        time.sleep(1.25) # when you're a child
    elif 10 < age < 20:
        time.sleep(.86) # but when you grow
    elif 20 < age < 30:
        time.sleep(.55) # older and older
    elif 30 < age < 50:
        time.sleep(.33) # time works for relativity
    else:
        time.sleep(0.11) #* and then, time flies like an arrow; fruit flies like a banana!

#? Just a random funny birthday celebration song which is created by Ata Demirer the Turkish stand up comedian.
url = "https://www.youtube.com/watch?v=04V7Llpn6iM"
wb.open(url, new=2)