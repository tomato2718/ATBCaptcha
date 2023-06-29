from logging import getLogger

from ._atbcaptcha import ATBCaptcha

logger = getLogger('atbcaptcha')
logger.setLevel('INFO')

if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

if __name__ == '__main__':
    img = ATBCaptcha(text='tomato', 
                     size=72,
                     )
    img.generate(10)
    img.image_frames[0].save('./test.gif',
                             format='GIF',
                             save_all=True,
                             append_images=img.image_frames[1:],
                             duration=33,
                             loop=0
                             )
    # img.base_frame.save('./test.png')