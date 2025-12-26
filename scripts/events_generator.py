import csv
import random
from datetime import datetime

# Configuration
OUTPUT_DIR = "input_data"
EVENTS_PER_FILE = 100
FILE_INTERVAL = 10

# Sample data
USER_IDS = list(range(1, 51))
PRODUCTS = [
    {"product_id": "PROD001", "product_name": "Laptop", "price": 999.99},
    {"product_id": "PROD002", "product_name": "Mouse", "price": 29.99},
    {"product_id": "PROD003", "product_name": "Keyboard", "price": 79.99},
    {"product_id": "PROD004", "product_name": "Monitor", "price": 299.99},
    {"product_id": "PROD005", "product_name": "Headphones", "price": 149.99},
    {"product_id": "PROD006", "product_name": "Webcam", "price": 89.99},
    {"product_id": "PROD007", "product_name": "USB Cable", "price": 12.99},
    {"product_id": "PROD008", "product_name": "Phone", "price": 699.99},
    {"product_id": "PROD009", "product_name": "Tablet", "price": 449.99},
    {"product_id": "PROD010", "product_name": "Smartwatch", "price": 249.99},
]

EVENT_TYPES = ["view", "add_to_cart", "purchase", "remove_from_cart"]


def generate_event():
    """Generate a single user event"""
    user_id = random.choice(USER_IDS)
    product = random.choice(PRODUCTS)
    event_type = random.choices(
        EVENT_TYPES, weights=[0.6, 0.2, 0.1, 0.1] 
    )[0]

    event = {
        "event_timestamp": datetime.now(),
        "user_id": user_id,
        "event_type": event_type,
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "product_price": product["price"],
        "session_id": f"SESSION{user_id % 10}",
    }

    return event


def generate_csv_file():
    """Generate a CSV file with events"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/events_{timestamp}.csv"

    # Generate events
    events = [generate_event() for _ in range(EVENTS_PER_FILE)]

    # Write to CSV
    with open(filename, "w", newline="") as csvfile:
        fieldnames = events[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)
