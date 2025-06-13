from datetime import datetime

def get_days_from_today (date):
    format_input_date = datetime.strptime(date, "%Y-%m-%d")
    date_today = datetime.today()
    difference_between_dates = date_today.toordinal() - format_input_date.toordinal()
    return (difference_between_dates)

print (get_days_from_today ('2025-6-14'))