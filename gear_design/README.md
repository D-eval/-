# 齿轮参数自动设计

## 使用方法:

先修改a.py中的输入参数, 然后运行:

```zsh
python3 a.py
```

## 输入输出
输入:
* 输入功率 P
* 小齿轮转速 n
* 传动比 i
* 循环次数 N
* 小齿轮齿数 z

输出:
* 调整后的齿数z1,z2
* 模数m
* 压力角alpha
* 中心距a
* 齿宽b1,b2

还有一些不能更改的条件, 如果想改可以去AllCharts.py里按照机械设计书上的图表录入插值的数据

* 7级精度
* 小齿轮40Cr(调质),齿面硬度280
* 大齿轮45钢(调质),齿面硬度240
* $\phi_d=0.8$