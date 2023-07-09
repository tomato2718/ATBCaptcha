from logging import basicConfig
from logging import getLogger
from json import dumps

from . import ATBCaptcha, Font, Color
from ._argparser import arg_parser

logger = getLogger('atbcaptcha')
basicConfig(
    format='[%(levelname)-5s %(asctime)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger.setLevel('INFO')

if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

def main():
    logger.info('Parsing arguments.')
    args = arg_parser().parse_args()
    logger.debug(
        f'Arguments:\n{dumps(vars(args), indent=4)}'
    )

    logger.info('Creating ATBCaptcha object.')
    img = ATBCaptcha(
        text=args.text, 
        font=args.font if args.font else Font.HACK_NERD_FONT,
        size=args.size,
    )

    logger.info('Generating Captcha.')
    img.generate(
        fps=args.fps,
        color=getattr(Color, args.color.upper()),
    )

    logger.info('Saveing Captcha.')
    img.save(args.output)

    logger.info('Done.')

if __name__ == '__main__':
    logger.info('Starting module.')
    main()
