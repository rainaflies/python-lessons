# OpenAI Planets

A simple Python app that uses OpenAI's ChatGPT and DALL-E APIs to show information and images about planets in the Solar System.

## Dependencies

- `openai`
- `opencv-python`

You can install these dependencies using pip:

```
pip3 install openai opencv-python
```

## API Key

You need to have your OpenAI API key for the program to work. This key should be entered in the file named openai_planets.py, replacing the "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" string with your actual API key.

## Usage

Run the main.py script using Python: `python3 main.py`. Upon starting, you will be presented with a menu of planets to choose from:

```
Please pick a planet:
1. Mercury
2. Venus
3. 🌎
4. Mars
5. Jupiter
6. Saturn
7. Uranus
8. Neptune
9. Pluto
--------------------------------------------------
```

Enter the number corresponding to the planet you want to learn about.

The app will query ChatGPT and DALL-E to display relevant information and a picture of the chosen planet. When the picture is displayed, press Esc to close the window and return to the program.
