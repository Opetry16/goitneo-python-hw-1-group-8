from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    """Function of the list of colleagues to be congratulated this week."""
    birthdays_by_day = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            day_of_week = (today + timedelta(days = delta_days)).strftime('%A')
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthdays_by_day[day_of_week].append(name)         
    for day, names in birthdays_by_day.items():
        if names:
            print(f"{day}: {', '.join(names)}")
            
            
    users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
]

    get_birthdays_per_week(users)