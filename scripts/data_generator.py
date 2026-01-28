import csv
import os
import random
import time
from datetime import datetime
from uuid import uuid4

# Configuration
OUTPUT_DIR = "app/input_data"
EVENTS_PER_FILE = 1000
FILE_INTERVAL = 10
NUM_USERS = 100

# Sample data
USER_IDS = [f"USER_{i:06d}" for i in range(1, NUM_USERS + 1)]

PRODUCTS = [
    {"product_id": "PROD001", "product_name": "Laptop", "price": 999.99},
    {"product_name": "Mouse", "price": 29.99},
    {"product_id": "PROD003", "product_name": "Keyboard", "price": 79.99},
    {"product_id": "PROD004", "product_name": "Monitor"},
    {"product_id": "PROD005", "product_name": "Headphones", "price": 149.99},
    {"product_id": "PROD006", "product_name": "Webcam", "price": -120.00},
    {"product_id": "PROD007", "product_name": "USB Cable", "price": 12.99},
    {"product_id": "PROD008", "product_name": "Phone", "price": 699.99},
    {"product_id": "PROD009", "product_name": "Tablet", "price": 449.99},
    {"product_id": "PROD010", "price": 249.99},
]

EVENT_TYPES = ["view", "add_to_cart", "purchase", "remove_from_cart"]

SESSIONS = {}

def generate_event():
    """Generate a single user event"""
    user_id = random.choice(USER_IDS)
    product = random.choice(PRODUCTS)
    event_type = random.choices(EVENT_TYPES, weights=[0.6, 0.4, 0.2, 0.1])[0]

    if user_id not in SESSIONS:
        session_id = str(uuid4())
        SESSIONS[user_id] = session_id
    else:
        session_id = SESSIONS[user_id]

    event = {
        "user_id": user_id,
        "event_type": event_type,
        "event_timestamp": datetime.now(),
        "product_id": product.get("product_id", None),
        "product_name": product.get("product_name", ""),
        "product_price": product.get("price", 0.0),
        "session_id": session_id,
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


def main():
    """Main loop - generate files continuously"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        while True:
            generate_csv_file()
            time.sleep(FILE_INTERVAL)
    except KeyboardInterrupt:
        print("\n\n[STOPPED] Event generation stopped by user")


if __name__ == "__main__":
    main()
