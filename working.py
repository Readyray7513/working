import re  # Importing regex module for pattern matching
import sys  # Importing sys for handling command-line arguments (optional)

def main():
    try:
        # Prompt the user for input and pass it to the convert function
        print(convert(input("Hours: ")))
    except ValueError:
        # Print an error message if the input format is incorrect
        raise ValueError("Invalid input format. Please use the format '9 AM to 5 PM'.")

def convert(s):
    """
    Converts a 12-hour formatted time range (e.g., "9 AM to 5 PM") 
    into a 24-hour format (e.g., "09:00 to 17:00").
    """
    # Regex pattern to match times with optional minutes
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s.strip())
    
    if match:
        # Extract groups from the regex match
        start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()
        
        # Convert extracted string values to integers
        start_hour = int(start_hour)
        start_minute = int(start_minute) if start_minute else 0  # Default to 00 if minutes not provided
        end_hour = int(end_hour)
        end_minute = int(end_minute) if end_minute else 0  # Default to 00 if minutes not provided

        # Check if minutes are valid (0-59)
        if start_minute > 59 or end_minute > 59:
            raise ValueError

        # Convert to 24-hour format using helper function
        start_hour = to_24_hour(start_hour, start_meridiem)
        end_hour = to_24_hour(end_hour, end_meridiem)

        # Format the output as HH:MM to HH:MM (ensuring two digits for hours and minutes)
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    # Raise an error if input doesn't match expected format
    raise ValueError

def to_24_hour(hour, meridiem):
    """
    Converts a 12-hour format time to a 24-hour format.
    - AM (except 12 AM) stays the same.
    - 12 AM becomes 00.
    - PM (except 12 PM) adds 12 to convert to 24-hour format.
    """
    if meridiem == "PM" and hour < 12:
        return hour + 12  # Convert PM to 24-hour format (except 12 PM)
    elif meridiem == "AM" and hour == 12:
        return 0  # Convert 12 AM to 00
    return hour  # Return unchanged for other cases

if __name__ == "__main__":
    main()  # Run the main function only if the script is executed directly
