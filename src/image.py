import os
import string
import random
import base64

from captcha.image import ImageCaptcha


__all__ = [
    'create_captcha',
    'gen_verify_code',
    'Captcha',
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
    stream = image.generate(code)
    # 图片的base64字符串格式：data:image/png;data,<base64字符串>
    print('===', str(base64.b64encode(stream.getvalue()), encoding='utf-8'))
    image.write(code, '{code}.png'.format(code=code))


def gen_verify_code(length=4):
    """ 生成随机验证码 """
    return ''.join(random.choice(ALLOWED_CHARS) for _ in range(length))


class Captcha(object):
    """ 类形式生成图片验证码 """

    def __init__(self, code_len=4, fonts=DEFAULT_FONTS, allowed_chars=ALLOWED_CHARS):
        self.code_len = code_len
        self.fonts = fonts
        self.allowed_chars = allowed_chars

    def create_captcha(self):
        """ 创建图片验证码 """
        image = ImageCaptcha(fonts=self.fonts)
        code = self.gen_verify_code(self.code_len)
        stream = image.generate(code)
        # 图片的base64字符串格式：data:image/png;base64,<base64字符串>
        img_base64 = 'data:image/png;base64,{base64_str}'.format(
            base64_str=str(base64.b64encode(stream.getvalue()), encoding='utf-8'))
        return code, img_base64


    def gen_verify_code(self):
        """ 生成随机验证码 """
        return ''.join(random.choice(self.allowed_chars) for _ in range(self.code_len))
        

if __name__ == '__main__':
    # create_captcha()
    captcha_obj = Captcha()
    code, img_base64 = captcha_obj.create_captcha()
    print(code, img_base64)
