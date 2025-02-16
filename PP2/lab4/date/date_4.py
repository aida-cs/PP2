from datetime import datetime

date1 = datetime(2025, 2, 15, 12, 0, 0)  # Example: Feb 15, 2025, at 12:00 PM
date2 = datetime(2025, 2, 10, 8, 30, 0)  # Example: Feb 10, 2025, at 08:30 AM
difference = abs((date1 - date2).total_seconds())

print("Difference in seconds:", difference)