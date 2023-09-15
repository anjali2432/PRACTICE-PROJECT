def generate_timetable(start_time, end_time, interval):
    """
    This function generates a time table for a given start time, end time, and interval.
    """
    current_time = start_time
    while current_time < end_time:
        print(current_time.strftime('%H:%M'))
        current_time += interval

if __name__ == '__main__':
    from datetime import datetime, timedelta
    
    # Define start time, end time, and interval
    start_time = datetime.strptime('08:00', '%H:%M')
    end_time = datetime.strptime('18:00', '%H:%M')
    interval = timedelta(minutes=30)
    
    # Generate and print the time table
    generate_timetable(start_time, end_time, interval)
