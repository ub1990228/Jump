import PIL                             # 图像处理模块
import numpy                           # 图像处理模块
import matplotlib.pyplot as plt        # 画图模块
import matplotlib.widgets as Button    # 按钮模块
import warnings                        # 屏蔽警告
# 不让打印告警信息
warnings.filterwarnings('ignore')


if __name__ == '__main__':
    # 创建一个空白的图像对象
    figure = plt.figure()
    # "重新"按钮的位置大小
    reelect_button_position = plt.axes([0.79, 0.8, 0.1, 0.08])
    # 按钮背景图片
    m = numpy.array(PIL.Image.open('image/bt.png'))
    # 设置重新按钮图片
    reelect_button = Button(reelect_button_position, label='', image=m)
    # "自动"按钮的位置大小
    auto_button_position = plt.axes([0.79, 0.65, 0.1, 0.08])
    # 按钮背景图片
    m1 = numpy.array(PIL.Image.open('image/bt1.png'))
    # 设置重新按钮图片
    auto_button = Button(auto_button_position, label='', image=m1)
    plt.show()
