import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def plt_eksgn_layer():

    names = ['1', '2', '3', '4', '5', '6']
    x = range(len(names))
    y = [88.59, 91.41, 89.07, 88.41, 87.62, 86.48]
    y1 = [86.92, 89.38, 87.11, 86.90, 85.44, 84.08]
    # plt.plot(x, y, 'ro-')
    # plt.plot(x, y1, 'bo-')
    # plt.xlim(-1, 11) # 限定横轴的范围
    font1 = {'family': 'Times New Roman','weight': 'normal','size': 23,}
    font2 = {'family': 'Times New Roman','weight': 'normal','size': 23,}

    plt.ylim(80.00, 95.00)  # 限定纵轴的范围
    plt.plot(x, y, marker='o', mec='r', mfc='w', label=u'Micro-F1')
    plt.plot(x, y1, marker='*', ms=10, label=u'Macro-F1')
    plt.legend(prop = font1)  # 让图例生效
    plt.xticks(x, names, rotation=0)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"Number of Graph Layer", fontdict=font2)  # X轴标签
    plt.ylabel("F1-score (%)",fontdict=font2)  # Y轴标签
    plt.title("EKSGN",fontdict=font2)  # 标题
#
    # plt.show()
    path = './figure/'
    if not os.path.exists(path):
        os.makedirs(path)
    # plt.savefig(path + 'scatter.jpg')  # 保存图片
    # plt.savefig(path + 'dialog_turn.jpg')  # 保存图片\n",
    plt.savefig(path + 'number_layer_eksgn.svg', format='svg', dpi=150)  # 输出
    plt.show()

if __name__ == '__main__':
    plt_eksgn_layer()