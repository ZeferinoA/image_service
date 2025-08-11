import requests
import os

# The address where your Flask microservice is running
BASE_URL = "http://127.0.0.1:5001"

# The image file
IMAGE_PATH = "test_photo.png"

def run_test():
    """
    Tests the full upload and retrieval cycle of the microservice.
    """
    print("--- Running Microservice Test ---")

    # 1. --- UPLOAD THE IMAGE ---
    # This part programmatically requests data from the microservice
    print(f"\n[REQUEST] Uploading '{IMAGE_PATH}' to {BASE_URL}/upload...")

    try:
        with open(IMAGE_PATH, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(f"{BASE_URL}/upload", files=files)

        # Check if the upload was successful
        if response.status_code == 201:
            # 2. --- RECEIVE THE RESPONSE (IMAGE ID) ---
            # This part shows the test program receiving data
            image_id = response.json()['id']
            print(f"[RESPONSE] Success! Image stored with ID: {image_id}")
        else:
            print(f"[ERROR] Upload failed with status {response.status_code}: {response.text}")
            return

    except requests.exceptions.ConnectionError as e:
        print(f"[FATAL ERROR] Could not connect to the microservice at {BASE_URL}.")
        return

    # 3. --- RETRIEVE THE IMAGE ---
    # This part uses the received ID to make another request
    print(f"\n[REQUEST] Retrieving image with ID '{image_id}'...")
    response = requests.get(f"{BASE_URL}/image/{image_id}")

    if response.status_code == 200:
        # 4. --- RECEIVE THE RESPONSE (IMAGE DATA) & SAVE ---
        save_path = f"retrieved_{os.path.basename(IMAGE_PATH)}"
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"[RESPONSE] Success! Image data received and saved as '{save_path}'")
        print("\n--- Test Complete ---")
    else:
        print(f"[ERROR] Retrieval failed with status {response.status_code}: {response.text}")


if __name__ == "__main__":
    run_test()