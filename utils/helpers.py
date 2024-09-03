from datetime import datetime

def format_date(date_str):
    """
    Format a string into a human-readable date.

    Args:
        date_str (str): The date string to format.

    Returns:
        str: The formatted date string.
    """
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y")

def calculate_wait_time(start_time, end_time):
    """
    Calculate the wait time between two timestamps.

    Args:
        start_time (str): The start time.
        end_time (str): The end time.

    Returns:
        int: The wait time in minutes.
    """
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    return int((end - start).total_seconds() // 60)
