'''
Not for import.
'''

__all__ = ['ATBCaptcha']

from logging import getLogger
from typing import Literal

from PIL import (Image,
                 ImageDraw,
                 ImageFont
                )

from ._styles import Color
from ._utils import random_pixels

# TODO: Implement the logger

class ATBCaptcha:
    '''
    The class to create Animated Text-Based Captcha.
    '''
    _base_frame: Image.Image
    _fps: Literal[15, 30]
    _color: list[tuple[int, int, int]]
    _image_frames: list[Image.Image] = []
    _logger = getLogger('atbcaptcha')

    def __init__(self,
                 text: str,
                 font: str,
                 size: int = 12,
                 ) -> None:
        '''
        Constructor method.

        :param str text: Text to display on captcha.
        :param str font: Path of a TrueType font.
        :param int size: Size of the text.
        '''
        x, y = int(size)*len(text), int(size)
        self._base_frame = Image.new(
            mode='RGB',
            size=(x, y),
            color='white'
        )
        font = self._load_font(font, size)
        draw = ImageDraw.Draw(self._base_frame)
        draw.text(
            xy=(x//2, y//2),
            text=text,
            fill=(0, 0, 0),
            font=font,
            anchor='mm'
        )
            
    @property
    def base_frame(self) -> Image.Image:
        '''
        Return the base frame of the animated captcha.

        :return: The base frame.
        :rtype: `Image.Image`
        '''
        return self._base_frame

    @property
    def image_frames(self) -> list[Image.Image]:
        '''
        Return the frames of the animated captcha.

        :return: List of the frames.
        :rtype: `list`
        '''
        return self._image_frames
    
    def generate(self,
                 fps: Literal[15, 30],
                 color: list[tuple[int, int, int]] = Color.DEFAULT
                 ) -> None:
        '''
        Generate the Animeted Text-Based Captcha.

        Data structure of `color` MUST be like follows::

            [
                (0, 0, 0),
                (50, 50, 50),
                (100, 100, 100),
                (150, 150, 150),
                (200, 200, 200),
                (252, 252, 252),
            ]

        :param int fps: The frames per second of the captcha, `MUST` be 15 or 30.
        :param list[tuple[int, int, int]] color: A list of tuples use to generate the captcha.
        :return: None.
        :raise ValueError: When input fps isn't 15 or 30.
        '''
        if fps not in (15, 30):
            raise ValueError('The value of fpt MUST be 15 or 30.')
        self._fps = fps
        size = self._base_frame.size
        image_frames = [Image.new(mode='RGB', size=size) for i in range(fps)]
        for i in range(size[0]):
            for j in range(size[1]):
                delay = 1 if any(self._base_frame.getpixel((i, j))) else 3
                pixels = random_pixels(
                    style=color,
                    length=fps//delay,
                    repeat=delay
                )
                self._image_frames = self._put_pixels(
                    image_frames=image_frames,
                    x=i,
                    y=j,
                    pixels=pixels
                )

    def save(self, path: str) -> None:
        '''
        Output the file.

        :param str path: The path of where the captcha will be saved.
        '''
        duration = {
            15: 66.7,
            30: 33.3
        }
        self._image_frames[0].save(
            path,
            format='GIF',
            save_all=True,
            append_images=self._image_frames[1:],
            duration=duration[self._fps],
            loop=0
        )

    @staticmethod
    def _load_font(font: str, size: int) -> ImageFont.FreeTypeFont:
        '''
        Load the font which to use for captcha.

        :param str font: Path of a TrueType font.
        :param int size: Size of the font.
        '''
        return ImageFont.truetype(font=font, size=size)
    
    @staticmethod
    def _put_pixels(image_frames: list[Image.Image], 
                    x: int, 
                    y: int, 
                    pixels: list[tuple[int, int, int]]
                    ) -> list[Image.Image]:
        '''
        Modifies the pixel at the given position to all frames.
        
        .. note::
            `image_frames` and `pixels` MUST have same length.

        :param list[Image.Image] image_frames: The frames of the animated captcha.
        :param int x: X-Coordinate of the pixel.
        :param int y: Y-Coordinate of the pixel.
        :param list[tuple[int, int, int]] pixels: List of the pixels to put.
        :return: Modified image_frames.
        :rtype: `list[Image.Image]`
        :raise ValueError: image_frames and pixels have different lengths.
        '''
        if len(image_frames) != len(pixels):
            raise ValueError('image_frames and pixels have different lengths')
        for i, frame in enumerate(image_frames):
            frame.putpixel(
                xy=(x, y),
                value=pixels[i]
            )
        return image_frames