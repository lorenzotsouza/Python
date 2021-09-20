def add_time(start, duration, day=None):

    start_hr = int(start[:-2].split(":")[0])
    start_min = int(start[:-2].split(":")[1])
    duration_hr = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])
    period = start[-2:]
    weekday = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]

    if start_hr == 12 and period == "AM":
        start_hr = 0
    if start_hr == 12 and period == "PM":
        start_hr = 0

    if start_min + duration_min > 60:
        end_min = start_min + duration_min - 60
        if period == "PM":
            end_hr = start_hr + duration_hr + 1 + 12
        else:
            end_hr = start_hr + duration_hr + 1
    else:
        end_min = start_min + duration_min
        if period == "PM":
            end_hr = start_hr + duration_hr + 12
        else:
            end_hr = start_hr + duration_hr

    if end_hr // 24 < 1:
        day_count = ""
    elif end_hr // 24 == 1:
        day_count = " (next day)"
    else:
        day_count = " (" + str(end_hr // 24) + " days later)"

    if end_hr - ((end_hr // 24) * 24) < 12:
        if end_hr - ((end_hr // 24) * 24) == 0:
            new_hr = end_hr - ((end_hr // 24) * 24) + 12
        else:
            new_hr = end_hr - ((end_hr // 24) * 24)
        new_period = " AM"
    else:
        if end_hr - ((end_hr // 24) * 24) == 12:
            new_hr = end_hr - ((end_hr // 24) * 24)
        else:
            new_hr = end_hr - ((end_hr // 24) * 24) - 12
        new_period = " PM"

    if day != None:
        week_day_count = int(weekday.index(
            day.lower().capitalize())) + end_hr // 24
        new_weekday = ", " + weekday[week_day_count % 7]
    else:
        new_weekday = ""

    new_time = str(new_hr) + ":" + str(end_min).zfill(
        2) + new_period + new_weekday + day_count

    return new_time
