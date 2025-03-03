import os

print("Environment Variables:")
for key, value in os.environ.items():
    if key.strip() == "BING_SEARCH_KEY":
        print(f"{key}: {value}")
