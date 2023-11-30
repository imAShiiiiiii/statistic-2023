import pandas as pd
import matplotlib.pyplot as plt
from pyreadstat import pyreadstat
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体


def 读取SPSS数据文件(文件位置及名称, 是否保留标签值: bool):
    数据表, metadata = pyreadstat.read_sav(
        文件位置及名称, apply_value_formats=是否保留标签值, formats_as_ordered_category=True)
    return 数据表

def 相关系数判断(系数:int):
    if 系数 >=0.8:
        return '极强相关'
    elif 系数 >= 0.6:
         return '强相关'
    elif 系数 >= 0.4:
         return '中等强度相关'
    elif 系数 >= 0.2:
         return '弱相关'
    else:
         return '极弱相关或无相关'


def 有序变量描述统计函数(表名, 变量名):
    result = 表名[变量名].value_counts(sort=False)
    描述统计表 = pd.DataFrame(result)
    描述统计表['比例'] = 描述统计表['count'] / 描述统计表['count'].sum()
    描述统计表['累计比例'] = 描述统计表['比例'].cumsum()
    return 描述统计表


def 绘制直方图(表名):
    x = 表名.index
    y = 表名['count'].values
    fig, ax2 = plt.subplots()
    ax2.bar(x, y)
    plt.show()
