import base64
import requests
from openai import OpenAI

# Function to encode an image from a URL in Base64 format
def encode_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        print(f"Error fetching image from {url}")
        return None

# Function to get comprehensive descriptions from the OpenAI vision model
def get_image_descriptions(image_urls):
    # Initialize the OpenAI client
    client = OpenAI(api_key="api_key_here")

    # Encode images in Base64 format
    base64_images = []
    for url in image_urls:
        base64_image = encode_image_from_url(url)
        if base64_image:
            base64_images.append(f"data:image/jpeg;base64,{base64_image}")
    
    # Create the message payload for the API request
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Generate descriptions for the provided images in the following styles, "
                        "each around 70 words:\n"
                        "1. Literal description\n"
                        "2. Emotional response\n"
                        "3. Contextual background\n"
                        "4. Narrative description\n"
                        "5. Symbolic interpretation\n"
                        "6. Technical analysis\n"
                        "7. Humorous observation\n"
                        "8. Artistic evaluation\n"
                        "9. Comparative description\n"
                        "10. Visual storytelling\n"
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": base64_images[0],
                        "detail": "high",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": base64_images[1],
                        "detail": "high",
                    },
                },
            ],
        }
    ]

    # Make the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=300,
    )

    # Return the generated description
    return response.choices[0].message['content'] if response.choices else "No description generated."

# Main function
if __name__ == "__main__":
    # List of image URLs to analyze
    image_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
    ]

    all_descriptions = get_image_descriptions(image_urls)

    # Print the generated descriptions
    print("Generated Descriptions:\n")
    print(all_descriptions)
