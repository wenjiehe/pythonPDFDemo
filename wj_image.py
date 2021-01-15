from PIL import Image, ImageFilter

def main():
    image = Image.open('/Users/hewenjie/Desktop/120x120.png')
    image1 = Image.open('./zhuo.jpeg')
    #打印格式、图片尺寸大小、图片模式
    print(image.format, image.size, image.mode)

    # 裁剪图片
    # rect =  20, 20, 100, 100
    # image.crop(rect)

    # 生成缩略图
    # size = 50, 50
    # image.thumbnail(size)

    #缩放和黏贴图像
    # rect = 0, 0, 120, 120
    # guido_head = image.crop(rect)
    # width, height = guido_head.size
    # image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (100, 60))
    # image1.show() #展示图片

    #旋转和翻转
    # image1.rotate(180).show()
    # image1.transpose(Image.FLIP_LEFT_RIGHT).show()

    #操作像素
    # for x in range(40, 150):
    #     for y in range(40, 180):
    #         # image1.putpixel((x, y), (128, 128, 128))
    #         image1.putpixel((x, y), (222, 0, 23))
    # image1.show()

    #滤镜效果
    image1.filter(ImageFilter.BLUR).show()

if __name__ == '__main__':
    main()