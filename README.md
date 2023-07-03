# Animated Text-Based Captcha
## Summary
> **Currently under development**


## Requirements
### System
- `docker >= 23.0`
- `python >= 3.10.10`

### Python
- `Pillow >= 9.5.0`

## Setup
### Installation
- TBA.
```sh
>>> 
```

## Usage
### Start Up
- Import this Project as a module.
```py
'''
For more informations, see `docs/`.
'''
from atbcaptcha import ATBCaptcha, Font, Color

# Create an ATBCaptcha object
img = ATBCaptcha(
    text='Text to display', 
    font=Font.HACK_NERD_FONT,
    size=72,
)
# Generate the captcha
img.generate(
    fps=30,
    color=Color.DEFAULT,
)
# Output the captcha
img.save(args.output)
```

- Use Python to execute this project.
```sh
>>> python -m atbcaptcha -h
>>> python -m atbcaptcha foo -o ./output.gif
>>> python -m atbcaptcha bar -o ./test.gif --size 72
>>> python -m atbcaptcha foobar -o ./test.gif --size 72 --fps 30   
```

- Use Docker to execute this project.
```sh
>>> TBA.
```

### Arguments
#### Requirement 
- `text`: The text to display on captcha.
- `--output`: The path of where the captcha to be save.

#### Optional
- `--font`: Path of a TrueType font, HackNerdFont will be use as default if not specified.
- `--size`: Size of the font, in pixels. (Default = 12)
- `--color`: Color of the captcha, currently only default in supported.
-  `--fps`: The fps of captcha. (Default = 15)

## Run the tests
- TBA.
```sh
>>> python -m tests
```

## Support
### Author
- `yveschen2718@gmail.com`
### Maintainer
- `yveschen2718@gmail.com`