import re
import os
from ics import Calendar, Event
from datetime import datetime
import pytz

def parse_event(event_str):
    event_pattern = re.compile(r'(.+?) \((.+?), (.+?), (?:ora )?(.+?), (.+?)\)')
    match = event_pattern.match(event_str)
    if not match:
        return None
    name, day, date, time, location = match.groups()

    # Convert to a standard date format
    day_map = {
        'vineri': 'Friday',
        'sâmbătă': 'Saturday',
        'duminică': 'Sunday',
        'luni': 'Monday',
        'marți': 'Tuesday',
        'miercuri': 'Wednesday',
        'joi': 'Thursday'
    }
    month_map = {
        'ianuarie': 'January',
        'februarie': 'February',
        'martie': 'March',
        'aprilie': 'April',
        'mai': 'May',
        'iunie': 'June',
        'iulie': 'July',
        'august': 'August',
        'septembrie': 'September',
        'octombrie': 'October',
        'noiembrie': 'November',
        'decembrie': 'December'
    }

    day_en = day_map.get(day.strip().lower(), day)
    date_parts = date.split()
    day_number = date_parts[0]
    month_en = month_map.get(date_parts[1].strip().lower(), date_parts[1])
    year = "2024"
    formatted_date = f"{year}-{month_en}-{day_number}"

    return {
        "name": name.strip(),
        "date": formatted_date,
        "time": time.strip(),
        "location": location.strip()
    }

def read_events_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    event_strings = content.split('\t')
    events = []
    for event_str in event_strings:
        event = parse_event(event_str)
        if event:
            events.append(event)
    return events

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'input.txt')
events = read_events_from_file(file_path)

clndr = Calendar()

tz = pytz.timezone('Europe/Bucharest')

for event in events:
    if event["time"] == "TO BE CONFIRMED" or event["location"] == "TO BE CONFIRMED":
        continue

    e = Event()
    e.name = event["name"]

    if '.' in event['time']:
        time_format = "%Y-%B-%d %H.%M"
    else:
        time_format = "%Y-%B-%d %H:%M"

    event_datetime = datetime.strptime(f"{event['date']} {event['time']}", time_format)
    event_datetime = tz.localize(event_datetime)
    e.begin = event_datetime
    e.location = event["location"]
    clndr.events.add(e)

output_file_path = os.path.join(current_dir, 'Calendar.ics')
with open(output_file_path, 'w', encoding='utf-8') as my_file:
    my_file.writelines(clndr)
