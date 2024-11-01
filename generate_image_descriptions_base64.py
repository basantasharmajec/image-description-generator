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
                        "0. Human-Centric description\n"
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
                        "11. Historical context\n"
                        "12. Personal reflection\n"
                        "13. Philosophical insight\n"
                        "14. Cultural significance\n"
                        "15. Visual aesthetics\n"
                        "16. Environmental commentary\n"
                        "17. Social critique\n"
                        "18. Mood interpretation\n"
                        "19. Future implications\n"
                        "20. Sensory exploration\n"
                        "21. Artistic style analysis\n"
                        "22. Color theory application\n"
                        "23. Audience interpretation\n"
                        "24. Artistic movement context\n"
                        "25. Genre classification\n"
                        "26. Character study\n"
                        "27. Symbolism in colors\n"
                        "28. Lighting analysis\n"
                        "29. Composition breakdown\n"
                        "30. Emotion conveyed\n"
                        "31. Action analysis\n"
                        "32. Perspective exploration\n"
                        "33. Photographic technique discussion\n"
                        "34. Event significance\n"
                        "35. Impressionist interpretation\n"
                        "36. Impression of the artist\n"
                        "37. Juxtaposition analysis\n"
                        "38. Theme exploration\n"
                        "39. Abstract interpretation\n"
                        "40. Realism critique\n"
                        "41. Cultural commentary\n"
                        "42. Nature versus technology discussion\n"
                        "43. Narrative conflict\n"
                        "44. Moment captured\n"
                        "45. Scale and proportion analysis\n"
                        "46. Emotional resonance\n"
                        "47. Inspiration behind the piece\n"
                        "48. Tension and release in the image\n"
                        "49. Symbolic representations of figures\n"
                        "50. Visual metaphors\n"
                        "51. Viewer engagement\n"
                        "52. Reflections on humanity\n"
                        "53. Identity exploration\n"
                        "54. Visual poetry\n"
                        "55. Spatial dynamics\n"
                        "56. Movement analysis\n"
                        "57. Impact of surroundings\n"
                        "58. Repetition and patterns\n"
                        "59. Spatial relationships\n"
                        "60. Impact of scale\n"
                        "61. Textural elements\n"
                        "62. Play of light and shadow\n"
                        "63. The element of surprise\n"
                        "64. Cultural heritage\n"
                        "65. Representation of time\n"
                        "66. Evolution of styles\n"
                        "67. Artistic techniques comparison\n"
                        "68. Historical significance of subject\n"
                        "69. Global cultural impacts\n"
                        "70. Critique of consumerism\n"
                        "71. Relationship to modern life\n"
                        "72. Exploration of conflict\n"
                        "73. Social movements reflected\n"
                        "74. Intertextual references\n"
                        "75. Iconography analysis\n"
                        "76. Role of technology in creation\n"
                        "77. Dreams and reality dichotomy\n"
                        "78. Disruption of norms\n"
                        "79. Memory and nostalgia\n"
                        "80. Gender representation\n"
                        "81. Nature of beauty\n"
                        "82. Exploration of solitude\n"
                        "83. Exploration of community\n"
                        "84. Image as a narrative device\n"
                        "85. Accessibility of art\n"
                        "86. Influence of pop culture\n"
                        "87. Science and art intersection\n"
                        "88. Evolution of artistic mediums\n"
                        "89. Examination of authenticity\n"
                        "90. Subversion of expectations\n"
                        "91. Exploration of freedom\n"
                        "92. Memory and identity\n"
                        "93. Reflection of societal values\n"
                        "94. Transformation through art\n"
                        "95. Exploration of power dynamics\n"
                        "96. Connection to audience\n"
                        "97. Role of imagination\n"
                        "98. Visual impact on perception\n"
                        "99. Ethereal qualities\n"
                        "100. Significance of the mundane\n"
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
        max_tokens=1200,  # Increased token limit to accommodate more descriptions
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
