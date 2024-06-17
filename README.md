# events2ics

events2ics is a Python project that converts event details from a text file into an ICS calendar file. It uses Regular Expression to extract event data from the text file and generate a structured calendar file that can be easily imported into calendar applications.

## Features
- Extract event names, dates, times, and locations from a text file
- Generate ICS files for calendar import
- Support for time zones

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/tgpetrica/events2ics.git
   cd events2ics
   ```

2. **Create a virtual environment (optional but recommended)**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required Python libraries**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Prepare**:
    Make sure the input file contains the event details in the specified format.

5. **Run the script**:
    ```sh
    python create_calendar.py
    ```

6. **Done!**:
    The generated `Calendar.ics` file will be saved in the same directory

## Input file format
    Event Name (day, date, time, location)
