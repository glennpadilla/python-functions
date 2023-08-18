from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "ja_JP")


def get_and_compare_dates():
    date1_input = input("Enter a date (YYYY-MM-DD): ")
    date2_input = input("Enter another date (YYYY-MM-DD): ")

    date1 = datetime.fromisoformat(date1_input)
    date2 = datetime.fromisoformat(date2_input)

    # new code here
    pretty_date1 = date1.strftime("%Y-%m-%d")
    pretty_date2 = date2.strftime("%B %d %y")

    if date1 < date2:
        print(f"{pretty_date1} is less than {pretty_date2}")
    elif date1 > date2:
        print(f"{pretty_date1} is greater than {pretty_date2}")
    else:
        print("Those are the same day!")


def get_birthday():
    # get birthday input from user (as isoformat)
    # convert that to a datetime using fromisoformat
    is_not_valid = True
    while is_not_valid:
        try:
            birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
            birthday = datetime.fromisoformat(birthday_input)
            break
        except ValueError:
            print("That is not a valid date, please use format YYYY-MM-DD")
            continue
    # get today (today's date/time)
    today = datetime.now()
    # compare birthday month to today's month
    # and
    # compare birthday day to today's day
    if birthday.month == today.month and birthday.day == today.day:
        # calculate the person's age based on todays year - birthday year
        age_in_years = today.year - birthday.year
        print("HAPPY BIRTHDAY!!!")
        print(f"You are {age_in_years} years old!")
    # else not their birthday
    else:
        print("We'll have a nice birthday party, I promise!")
        # send some message of sympathy


get_and_compare_dates()
get_birthday()
