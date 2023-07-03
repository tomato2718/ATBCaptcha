from logging import getLogger

from . import ATBCaptcha, Font, Color
from ._argparser import arg_parser

logger = getLogger('atbcaptcha')
logger.setLevel('INFO')

if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

def main():
    args = arg_parser().parse_args()
    img = ATBCaptcha(
        text=args.text, 
        font=args.font if args.font else Font.HACK_NERD_FONT,
        size=args.size,
    )
    img.generate(
        fps=args.fps,
        color=getattr(Color, args.color.upper()),
    )
    img.save(args.output)

if __name__ == '__main__':
    main()
