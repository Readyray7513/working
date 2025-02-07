# Time Converter (12-Hour to 24-Hour Format)  

This Python script converts time ranges from a 12-hour format (e.g., `"9 AM to 5 PM"`) to a 24-hour format (e.g., `"09:00 to 17:00"`). It uses **regular expressions (regex)** to validate input and ensures proper formatting.  

## Features  
✅ Converts standard time formats:  
   - `"9 AM to 5 PM"` → `"09:00 to 17:00"`  
   - `"10:30 PM to 8 AM"` → `"22:30 to 08:00"`  
   - `"12 AM to 12 PM"` → `"00:00 to 12:00"`  

✅ Handles both **hour-only** and **hour:minute** formats  
✅ Validates **minute values** (rejects `"9:60 AM to 5:60 PM"`)  
✅ Raises **errors for incorrect formats**  

## Installation  
No installation required—just run the script using Python 3.  

## Usage  
Run the script:  
python working.py

You'll be prompted to enter a time range:  
Hours: 9 AM to 5 PM
09:00 to 17:00


### Testing  
The script includes `pytest` tests. To run them:  
pytest test_working.py


## Error Handling  
If the input format is incorrect, the program prints `"Invalid input"` and exits gracefully.  

## Example Valid Inputs  
✔ `"9 AM to 5 PM"` → `"09:00 to 17:00"`  
✔ `"10:30 PM to 8 AM"` → `"22:30 to 08:00"`  
✔ `"12 AM to 12 PM"` → `"00:00 to 12:00"`  

## Example Invalid Inputs  
❌ `"9:60 AM to 5:60 PM"` → **Invalid (minutes > 59)**  
❌ `"9 AM - 5 PM"` → **Invalid format (must use "to")**  
❌ `"09:00 AM - 17:00 PM"` → **Invalid format**  

## Contributing  
Feel free to fork this repo and submit pull requests!  

## License  
This project is free to use and modify.  
