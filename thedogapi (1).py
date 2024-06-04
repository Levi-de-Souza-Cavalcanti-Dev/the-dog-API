from IPython.display import Image, display
import requests

def get_random_dog_image():
    url = "https://api.thedogapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return "Failed to retrieve data"

image_url = get_random_dog_image()
if "Failed" not in image_url:
    display(Image(url=image_url))
else:
    print(image_url)
