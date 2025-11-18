from datetime import datetime, timedelta


cities = {
    "San Francisco": -7,
    "New York": -4,
    "London": 1,
    "Dubai": 4,
    "Bangalore": 5.5,
    "Singapore": 8,
    "Tokyo": 9,
    "Sydney": 10,
    "Wellington": 12
}


utc_now = datetime.utcnow()

print("Current Time in 9 World Cities:\n")

for city, offset in cities.items():
    city_time = utc_now + timedelta(hours=offset)
    
    print(f"{city:12s} → {city_time.strftime('%Y-%m-%d %H:%M:%S')}")
