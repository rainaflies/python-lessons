import os
import openai
import cv2
import urllib.request

# Enter your own OpenAI API key here:
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def show_planet_info(planet):
  """
  Generate and print two sentences about the specified planet using OpenAI's GPT-3.5 Turbo model.

  This function uses OpenAI's GPT-3.5 Turbo model to generate a response to a prompt asking for two sentences
  about a given planet. The response is then printed to the console.

  Parameters:
  planet (str): The name of the planet for which to generate information. This should be a valid planet name.
  
  Returns:
  None.
  """

  prompt = "Write two sentences about the planet " + planet
  print(f"Generating information about {planet} using OpenAI...")

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
      {
        "role": "user", 
        "content": prompt
      }
    ]
  )  
  print(response.choices[0].message.content)


def show_planet_picture(planet):
  """
  Generate and display an image of the specified planet using OpenAI's DALL-E and OpenCV.

  This function uses OpenAI's DALL-E to generate an image of a given planet as seen from space, 
  against a black background. The image is saved locally as 'Planet.png'. The saved image is then
  displayed using OpenCV.

  Parameters:
  planet (str): The name of the planet for which to generate an image. This should be a valid planet name.

  Returns:
  None.

  Note:
  To use this function, you must have the `openai`, `urllib`, and `opencv-python` packages installed 
  and be authenticated with the OpenAI API. Also, ensure you have the rights to save files in the 
  working directory.
  """

  # Download the planet image from OpenAI DALL-E
  prompt = "An image of the planet " + planet + " as seen from space against a black background."
  print(f"Generating image of {planet} using DALL-E...")

  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024",
  )
  url = response["data"][0]["url"]
  filename = planet + ".png"
  urllib.request.urlretrieve(url, filename)

  # Show the planet image using OpenCV
  img = cv2.imread(filename, cv2.IMREAD_COLOR)
  cv2.imshow(planet, img)

  # Wait for any key to be pressed and then close the OpenCV window
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  # Delete the downloaded image file after the OpenCV window is closed
  os.remove(filename)
