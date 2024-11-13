from datetime import datetime, date, timedelta


def calculate_expiration_date(current_date: date):
    return current_date + timedelta(days=365)



