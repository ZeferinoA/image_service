### Dependencies needed
pip install Flask

### How to Request Data

Method: POST
Endpoint: http://127.0.0.1:5000/upload

```
import requests

upload_url = "http://127.0.0.1:5000/upload"

# Open the image file in binary read mode
with open('my_photo.jpg', 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(upload_url, files=files)
```

### How to Receive Data

Method: GET
Endpoint: http://127.0.0.1:5000/image/{image_id}

```
import requests

image_id = "123e4567-e89b-12d3-a456-426614174000" 

retrieve_url = f"http://127.0.0.1:5000/image/{image_id}"

response = requests.get(retrieve_url)

if response.status_code == 200:
    with open('retrieved_from_server.jpg', 'wb') as f:
        f.write(response.content)
    print("Image data received and saved successfully.")
else:
    print(f"Failed to retrieve image: {response.text}")
```
