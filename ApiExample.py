import random
import requests

def get_dog_images(breed, count=1):
    base_url = "https://dog.ceo/api/breed/{}/images/random/{}"
    api_url = base_url.format(breed, count)

    try:
        response = requests.get(api_url)

        if response.status_code == 200:

            data = response.json()
            image_urls = data.get("message", [])

            return image_urls
        else:
            print(f"Hata: {response.status_code}")
            return None
    except Exception as e:
        print(f"Hata: {e}")
        return None

dog_breed = ["labrador","akita","eskimo","dingo"]
dog_selection =random.choice(dog_breed)

print("selected dog pictures = ",dog_selection)

image_count = 5
result = get_dog_images(dog_selection, image_count)

if result:
    for i, url in enumerate(result):
        print(f"Resim {i + 1}: {url}")
else:
    print("Veri çekme başarısız.")
