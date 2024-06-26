from datetime import datetime

def get_days_from_today(date):
    try:
        date_from = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError as e:
        print(e)
        return 0
    
    date_to = datetime.today().date()
    interval = date_to - date_from
    return interval.days

# Example usage
print(get_days_from_today('2022-10-09'))