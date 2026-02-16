from datetime import datetime, timedelta

def get_next_date():
    date_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        current_date = datetime.strptime(date_input, "%Y-%m-%d")
        next_date = current_date + timedelta(days=1)
        print(f"Next date: {next_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")

get_next_date()