import ddddocr
import requests
from io import BytesIO
import logging





class CaptchaSolver:
    @staticmethod
    def solve_captcha_from_url(image_url):
        """通过图片 URL 识别验证码"""
        ocr = ddddocr.DdddOcr()
        try:
            logging.info(f"正在从 URL 下载图片: {image_url}")
            response = requests.get(image_url)
            response.raise_for_status()  # 检查请求是否成功

            image_bytes = BytesIO(response.content)

            logging.info("图片下载成功，正在识别验证码...")
            captcha_text = ocr.classification(image_bytes.read())
            logging.info("验证码识别成功")
            return captcha_text
        except Exception as e:
            logging.error(f"验证码识别失败: {e}")
            return None

    @staticmethod
    def solve_captcha_from_path(image_path):
        """通过本地图片路径识别验证码"""
        ocr = ddddocr.DdddOcr()
        try:
            logging.info(f"正在读取本地图片: {image_path}")
            with open(image_path, 'rb') as f:
                image_bytes = f.read()

            logging.info("图片读取成功，正在识别验证码...")
            captcha_text = ocr.classification(image_bytes)
            logging.info("验证码识别成功")
            return captcha_text
        except Exception as e:
            logging.error(f"验证码识别失败: {e}")
            return None


# 使用示例
'''
if __name__ == "__main__":
    # 替换为你的验证码图像 URL 或路径
    captcha_image_url = "http://example.com/captcha.png"  # 示例 URL
    captcha_image_path = "captcha.png"  # 示例本地路径

    # 通过 URL 识别验证码
    captcha_text_url = CaptchaSolver.solve_captcha_from_url(captcha_image_url)
    if captcha_text_url:
        logging.info(f"通过 URL 识别的验证码为: {captcha_text_url}")
    else:
        logging.warning("通过 URL 识别验证码失败")

    # 通过本地路径识别验证码
    captcha_text_path = CaptchaSolver.solve_captcha_from_path(captcha_image_path)
    if captcha_text_path:
        logging.info(f"通过路径识别的验证码为: {captcha_text_path}")
    else:
        logging.warning("通过路径识别验证码失败")

'''
