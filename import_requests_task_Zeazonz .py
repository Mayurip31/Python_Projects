import requests
import uuid
import json

# Fetch JSON data from the provided URL
url = 'https://whatismyip.callgoose.com/devops/devops.json'
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error fetching JSON data: {response.status_code}")
else:
    data = response.json()
    
    # Print the fetched data to inspect its structure
    print("Fetched data:")
    print(json.dumps(data, indent=4))  # Pretty-print the JSON response

    # Take user inputs
    name = input("Enter your name: ")
    language = input("Enter your language: ")
    bio = input("Enter your bio: ")

    # Check if inputs are valid
    if not name or not language or not bio:
        print("All fields are required!")
    else:
        # Generate a random UUID for the user ID and a fixed version
        user_id = str(uuid.uuid4())  # Generate a random ID
        version = 3.75  # Version can be adjusted as required

        # Create a new user data entry
        user_data = {
            'name': name,
            'language': language,
            'bio': bio,
            'id': user_id,
            'version': version
        }

        # Append the new data to the list
        data.append(user_data)

        # Print the modified data (optional)
        print("Updated data:")
        print(json.dumps(data, indent=4))

        # Send the modified data to the POST endpoint
        post_url = 'https://httpbin.org/post'

        try:
            post_response = requests.post(post_url, json=data)
            post_response.raise_for_status()  # Raise an error for bad responses
            print("POST response from server:")
            print(post_response.json())  # Print the response from the server
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
