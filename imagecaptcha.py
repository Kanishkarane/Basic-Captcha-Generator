
from captcha.image import ImageCaptcha
image=ImageCaptcha(width=280,height=90)
captcha_text="Kanishka"
data=image.generate(captcha_text)
image.write(captcha_text,'CAPTCHA.PNG')

from PIL import Image
Image.open('CAPTCHA.png').show()

