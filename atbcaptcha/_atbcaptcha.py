from logging import getLogger
from typing import Literal

from PIL import (Image,
                 ImageDraw,
                 ImageFont
                )

from ._font import Font
from ._utils import random_color

class ATBCaptcha:
    _image_frames: list[Image.Image] = []
    def __init__(self,
                 text: str,
                 size: int = 12,
                 ) -> None:
        '''
        :param str text: 
        :param int size: 
        :param str font: 
        :param int border: 
        '''
        x, y = int(size)*len(text), int(size)
        logger = getLogger('atbcaptcha')
        self._base_frame = Image.new(mode='RGB',
                                     size=(x, y),
                                     color='white'
                                    )

        font = self._load_font(size)
        draw = ImageDraw.Draw(self._base_frame)
        draw.text(xy=(x//2, y//2),
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
    
    def generate(self, fps: Literal[15, 30]) -> None:
        '''
        Generate the Animeted Text-Based Captcha.

        :param int fps: The frames per second of the captcha, `MUST` be 15 or 30.
        :return: None.
        :raise ValueError: When input fps isn't 15 or 30.
        '''
        if fps not in {15, 30}:
            raise ValueError('Only 15 or 30 fps are supported.')
        self._fps = fps
        frame_list: list[Image.Image] = []
        for i in range((fps+1)//2):
            frame_list += self._create_frame()
        self._image_frames = frame_list[:]

    def save(self) -> None:
        self._image_frames[0].save()

    @staticmethod
    def _load_font(size: int) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(font=Font.HACK_NERD_FONT, size=size)

    

    def _create_frame(self) -> list:
        size = self._base_frame.size
        frames = [Image.new(mode='RGB', size=size) for i in range(3)]
        for i in range(size[0]):
            for j in range(size[1]):
                pixel = self._base_frame.getpixel((i, j))
                if any(pixel):
                    for frame in frames:
                        frame.putpixel(xy=(i, j),
                                       value=random_color()
                                      )
                else:
                    color = random_color()
                    for frame in frames:
                        frame.putpixel(xy=(i, j),
                                       value=color
                                      )

        return frames