from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = birthday.replace(year=today.year)

        # Determine the date of the next birthday
        if congratulation_date < today:
            # If the birthday has already passed this year, consider next year
            congratulation_date = congratulation_date.replace(year=today.year + 1)

        # Calculate the difference between the birthday and today
        days_until_birthday = (congratulation_date - today).days

        # Check if the birthday falls within the next 7 days
        if days_until_birthday > 7:
            continue

         # Move the congratulation date to the next Monday if the birthday falls on a weekend
        weekday = congratulation_date.weekday()
        if weekday >= 5:
            congratulation_date += timedelta(days=7 - weekday)

        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Example usage:
users = [
    {"name": "John", "birthday": "2000.04.18"},
    {"name": "Alice", "birthday": "2001.04.20"},
    {"name": "Bob", "birthday": "2002.04.24"},
    {"name": "Emily", "birthday": "2003.04.25"},
    {"name": "David", "birthday": "2004.04.30"},
]
print(get_upcoming_birthdays(users))