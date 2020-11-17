import os
import string
import random

from captcha.image import ImageCaptcha


__all__ = [
    'create_captcha',
]

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
DEFAULT_FONTS = [os.path.join(DATA_PATH, 'fonts/Roboto/Roboto-Regular.ttf')]

ALLOWED_CHARS = string.ascii_uppercase + string.digits


def create_captcha():
    """ 创建图片验证码 """
    image = ImageCaptcha(fonts=DEFAULT_FONTS)
    code = gen_verify_code(4)
    data = image.generate(code)
    image.write(code, 'out.png')


def gen_verify_code(length):
    """ 生成随机验证码 """
    return ''.join(random.choice(ALLOWED_CHARS) for _ in range(length))

if __name__ == '__main__':
    create_captcha()
