from logging import getLogger

from . import ATBCaptcha, Font

logger = getLogger('atbcaptcha')
logger.setLevel('INFO')

if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

# TODO: Create arg parser.

if __name__ == '__main__':
    img = ATBCaptcha(
        text='POTATO', 
        font=Font.HACK_NERD_FONT,
        size=72,
    )
    img.generate(30)
    img.save('./test.gif')