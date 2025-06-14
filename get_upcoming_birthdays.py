# from datetime import datetime

# def get_upcoming_birthdays (users):
#     next_week_birthday_dict = []
#     day_today = datetime.today().date()
    
#     for user in users:
#         birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#         timedelta_of_birthdayth = birthday_this_year.toordinal() - day_today.toordinal()
#         if birthday_this_year < day_today and  timedelta_of_birthdayth < 7:
#             next_week_birthday_dict.pop(user)
#         return(next_week_birthday_dict)    
            
# dict_of_birthdays = get_upcoming_birthdays (users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
# )  

# from datetime import datetime, timedelta

# def get_upcoming_birthdays(users):
#     next_week_birthdays = []
#     today = datetime.today().date()
#     end_of_week = today + timedelta(days=7)

#     for user in users:
#         birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#         birthday_this_year = birthday.replace(year=today.year)

#         # If birthday already passed this year, assume it's next year
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
#         if today <= birthday_this_year <= end_of_week and birthday_this_year.weekday() == 5:
#             birthday_this_year = birthday_this_year.replace(day = birthday_this_year.day + 2 )
#             next_week_birthdays.append(user.update({"birthday": birthday_this_year}))
        
#         if today <= birthday_this_year <= end_of_week and birthday_this_year.weekday() == 6:
#             birthday_this_year = birthday_this_year.replace(day = birthday_this_year.day + 1 )
#             next_week_birthdays.append(user.update({"birthday": birthday_this_year}))
            
#         if today <= birthday_this_year <= end_of_week:
#             next_week_birthdays.append(user)

#     return next_week_birthdays

# # Example:
# dict_of_birthdays = get_upcoming_birthdays(users=[
#     {"name": "John Doe", "birthday": "1985.06.14"},
#     {"name": "Jane Smith", "birthday": "1990.06.15"}
# ])

# print(dict_of_birthdays)


from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    next_week_birthdays = []
    today = datetime.today().date()
    end_of_week = today + timedelta(days=7)

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday already passed this year, assume it's next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_of_week:
            user_copy = user.copy()
            
            # If the birthday is on Saturday (5), move it to Monday
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday → Monday
                birthday_this_year += timedelta(days=1)

            user_copy["birthday"] = birthday_this_year.strftime("%Y-%m-%d")
            next_week_birthdays.append(user_copy)

    return next_week_birthdays

# Example:
dict_of_birthdays = get_upcoming_birthdays(users=[
    {"name": "John Doe", "birthday": "1985.06.14"},  # Saturday
    {"name": "Jane Smith", "birthday": "1990.06.17"}  # Tuesday
])

print(dict_of_birthdays)
