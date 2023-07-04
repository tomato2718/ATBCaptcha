import pytest
from PIL import ImageFont

from atbcaptcha._atbcaptcha import ATBCaptcha

##### FIXTURES #####
@pytest.fixture(scope='module')
def atbcaptcha(text: str, font: str, size: int) -> ATBCaptcha:
    atbcaptcha = ATBCaptcha(
        text=text,
        font=font,
        size=size,
    )
    return atbcaptcha
    

##### TESTS #####
class TestATBCaptcha:
    @staticmethod
    def test_generate(atbcaptcha: ATBCaptcha):
        with pytest.raises(ValueError):
            atbcaptcha.generate(fps=20)
        atbcaptcha.generate(fps=15)
        for frame in atbcaptcha.image_frames:
            assert frame != atbcaptcha.base_frame
        atbcaptcha.generate(fps=30)
        for frame in atbcaptcha.image_frames:
            assert frame != atbcaptcha.base_frame
    
    @staticmethod
    @pytest.mark.skip(reason='IO method.')
    def test_save(atbcaptcha: ATBCaptcha):
        pass

    @staticmethod
    def test__load_font(atbcaptcha: ATBCaptcha, font: str, size: int):
        img_font = atbcaptcha._load_font(
            font=font,
            size=size,
        )
        assert isinstance(img_font, ImageFont.FreeTypeFont)

    @staticmethod
    @pytest.mark.skip(reason='Tested in TestATBCaptcha.test_generate.')
    def test__put_pixels():
        pass