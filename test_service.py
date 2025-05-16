import requests

base_url = "http://localhost:3000"

# Information necessary for save
# Can edit to return different inventory, or progress stamps, if necessary
save_payload = {
    "userId": "Kris",
    "slot": "slot1",
    "progress": {
        "hp": 100,
        "inventory": ["Twisted Sword", "Double Dark Burger"],
        "location": "Mallus"
    }
}

# Save progress
save_response = requests.post(f"{base_url}/save", json=save_payload)
print("Save response:", save_response.json())

# Load progress error test
load_params = {
    "userId": "player_test_error",
    "slot": "slot3"
}
load_response = requests.get(f"{base_url}/load", params=load_params)
print("Load response:", load_response.json())

# Load progress
load_params = {
    "userId": "Kris",
    "slot": "slot1"
}

# Request to GET load data
load_response = requests.get(f"{base_url}/load", params=load_params)
print("Load response:", load_response.json())
