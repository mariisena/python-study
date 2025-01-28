import datetime, bday_messages
from bday_messages import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 5, 15)
if next_birthday < today:
    next_birthday = datetime.date(today. year + 1, 5, 15)

days_away = (next_birthday - today).days

if days_away == 0:
    random_message = random.choice(bday_messages)
    print(random_message)
else:
    print(f"My next birthday is {days_away} days away!")

past_event = datetime.date(2000, 7, 1)
days_since_event = (today - past_event).days
years_since_event = days_since_event // 365
months_since_event = (days_since_event % 365) // 30

print(f"It has been {years_since_event} years and {months_since_event} months since the event on {past_event}.")