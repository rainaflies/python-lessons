# Music Player

## Overview

This Python program is a simple music player that plays different musical instrument sounds. It uses the playsound library to play sounds and prints out a series of emojis that represent the instrument being played. The instruments available are: Violin, Guitar, Drum, Sax, and Piano.

## Requirements

You will need Python 3.x installed and the Python package 'playsound'. You can install it via pip:

```
pip3 install playsound
```

## Usage

The application presents a menu with options for each instrument sound. You should enter the corresponding number to play a sound.

1. 🎻
2. 🎸
3. 🥁
4. 🎷
5. 🎹

To stop the program, you can use the keyboard interrupt, usually `Ctrl+C`.

## File Structure

The application expects .mp3 sound files for each instrument in a `sounds` directory in the same location as the script. The sound files should be named as follows:

- Violin.mp3
- Guitar.mp3
- Drum.mp3
- Sax.mp3
- Piano.mp3

For example, if your script is in `/home/user/music_player`, your `Violin.mp3` should be located at `/home/user/music_player/sounds/Violin.mp3`.

## Troubleshooting

If you enter an option that is not in the menu, the application will notify you that it's not a valid option.

## License

This project is open source under the MIT license.

## Contributing

Pull requests are welcome.
