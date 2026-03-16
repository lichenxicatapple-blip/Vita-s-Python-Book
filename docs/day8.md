# Day 8：你的第一个数据分析小工具

最后一天！今天我们要学三件大事：安装第三方库、读写 Excel 文件，然后用前七天的所有技能做一个完整的数据分析项目。

## 第一部分：模块、pip 和第三方库

### 什么是模块

你在前面的教程里已经见过 `import` 了，但一直没有正式介绍它。现在来补上。

Python 的强大之处在于它有海量的现成工具可以直接拿来用，不用什么都自己从零写。这些工具以**模块**的形式存在。

模块就是别人写好的一个 Python 文件（或一组文件），里面包含了各种函数和类。你用 `import` 把它引入到自己的程序里，就能使用里面的功能。

模块分两种：

**内置模块** -- Python 自带的，装好 Python 就能直接用：

```python
import csv          # 处理 CSV 文件
import json         # 处理 JSON 数据
import os           # 和操作系统交互（文件、目录操作等）
import math         # 数学函数
import random       # 生成随机数
```

**第三方库** -- 其他开发者写的，需要先安装才能用：

```python
import openpyxl     # 读写 Excel 文件（需要先安装）
import pandas       # 数据分析神器（需要先安装）
import requests     # 发送网络请求（需要先安装）
```

今天我们要用 `openpyxl` 来读写 Excel 文件。它是第三方库，所以要先装。

### pip：Python 的包管理工具

安装第三方库用 **pip**。pip 是 Python 自带的包管理工具，装好 Python 就已经有了。

打开终端（Mac 自带的终端或 VS Code 的内置终端都行），输入：

```
pip3 install openpyxl
```

> 和 `python3` 一样，Mac 上用 `pip3` 而不是 `pip`。

正常情况下，你会看到一堆下载进度条，最后显示 "Successfully installed openpyxl-x.x.x"，就装好了。

### 配置国内镜像（解决下载慢的问题）

pip 默认从国外的服务器下载，在国内可能很慢甚至超时。解决办法是换成国内的镜像源。

在终端里执行这行命令，一劳永逸地把默认源换成清华大学的镜像：

```
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

执行后会显示类似 "Writing to /Users/xxx/.config/pip/pip.conf" 的提示，说明配置成功了。以后所有 `pip3 install` 都会走国内镜像，速度快很多。

> 除了清华源，还有阿里云（https://mirrors.aliyun.com/pypi/simple/）等选择，效果都差不多。

### 验证安装

在终端里输入 `python3`，进入交互模式，然后：

```python
>>> import openpyxl
>>> print(openpyxl.__version__)
3.1.5
```

没有报错就说明安装成功了。版本号可能和上面不一样，没关系。

## 第二部分：用 openpyxl 读写 Excel

### 读取 Excel 文件

```python
import openpyxl

wb = openpyxl.load_workbook("sales_data.xlsx")
ws = wb.active

for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

逐行解释：

- `openpyxl.load_workbook("sales_data.xlsx")`：打开一个 Excel 文件，返回一个工作簿对象（workbook）
- `wb.active`：获取当前活跃的工作表（就是你打开 Excel 时默认看到的那个 sheet）
- `ws.iter_rows(min_row=2, values_only=True)`：逐行遍历工作表。`min_row=2` 表示从第 2 行开始（跳过标题行），`values_only=True` 表示只取单元格的值

每一行 `row` 是一个元组（和列表类似），比如 `('2024-01-05', '笔记本电脑', '电子产品', 2, 5999)`。

### 读取标题行

```python
import openpyxl

wb = openpyxl.load_workbook("sales_data.xlsx")
ws = wb.active

# 读取第一行作为标题
headers = [cell.value for cell in ws[1]]
print(headers)    # ['日期', '商品', '类别', '数量', '单价']
```

### 把每一行变成字典

结合标题行和数据行，可以把每一行转成字典，用起来更方便：

```python
import openpyxl

def read_excel(filename):
    """读取 Excel 文件，返回字典列表"""
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    headers = [cell.value for cell in ws[1]]
    records = []

    for row in ws.iter_rows(min_row=2, values_only=True):
        record = dict(zip(headers, row))
        records.append(record)

    return records
```

`dict(zip(headers, row))` 做了什么？`zip` 把标题和值一一配对，`dict` 把配对结果变成字典。比如标题是 `['日期', '商品']`，值是 `['2024-01-05', '笔记本电脑']`，结果就是 `{'日期': '2024-01-05', '商品': '笔记本电脑'}`。

### 写入 Excel 文件

```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "统计结果"

# 写入标题行
ws.append(["商品", "销售数量", "销售额"])

# 写入数据行
ws.append(["笔记本电脑", 7, 41993])
ws.append(["蓝牙耳机", 29, 5771])

wb.save("output.xlsx")
```

- `openpyxl.Workbook()` 创建一个新的空白工作簿
- `ws.append([...])` 往工作表末尾追加一行
- `wb.save("output.xlsx")` 保存文件

写好的 `.xlsx` 文件可以直接用 Excel 打开，格式和正常的 Excel 文件一模一样。

## 第三部分：综合项目 -- 销售数据分析

现在来做今天的重头戏。`day8` 文件夹里有一个 `sales_data.xlsx`，是一家小店一月份的销售记录，包含日期、商品、类别、数量和单价。

我们要写一个分析工具，自动生成以下报告：

1. 总销售额
2. 每个类别的销售额和占比
3. 每个商品的销售汇总（按销售额排序）
4. 最畅销的商品
5. 把统计结果保存为新的 Excel 文件

### 完整代码

```python
import openpyxl


def load_data(filename):
    """从 Excel 文件读取销售数据"""
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    headers = [cell.value for cell in ws[1]]

    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        record = dict(zip(headers, row))
        record["小计"] = record["数量"] * record["单价"]
        records.append(record)

    return records


def analyze_total(records):
    """计算总销售额"""
    return sum(r["小计"] for r in records)


def analyze_by_category(records):
    """按类别统计销售额"""
    categories = {}
    for r in records:
        cat = r["类别"]
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += r["小计"]
    return categories


def analyze_by_product(records):
    """按商品统计销售数量和销售额"""
    products = {}
    for r in records:
        name = r["商品"]
        if name not in products:
            products[name] = {"数量": 0, "销售额": 0}
        products[name]["数量"] += r["数量"]
        products[name]["销售额"] += r["小计"]
    return products


def print_report(records):
    """打印完整的分析报告"""
    total = analyze_total(records)
    categories = analyze_by_category(records)
    products = analyze_by_product(records)

    print("=" * 50)
    print("        一月份销售数据分析报告")
    print("=" * 50)

    print(f"\n总销售额：{total:,.0f} 元")
    print(f"总记录数：{len(records)} 条")

    print("\n--- 按类别统计 ---")
    for cat, amount in categories.items():
        ratio = amount / total * 100
        print(f"  {cat}：{amount:>10,.0f} 元（占比 {ratio:.1f}%）")

    print("\n--- 按商品统计 ---")
    sorted_products = sorted(
        products.items(),
        key=lambda x: x[1]["销售额"],
        reverse=True,
    )
    for name, info in sorted_products:
        print(f"  {name}：卖出 {info['数量']} 件，销售额 {info['销售额']:,.0f} 元")

    top = sorted_products[0]
    print(f"\n最畅销商品：{top[0]}（销售额 {top[1]['销售额']:,.0f} 元）")


def save_report(products, filename):
    """把商品统计结果保存为 Excel 文件"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "商品汇总"

    ws.append(["商品", "销售数量", "销售额"])

    sorted_products = sorted(
        products.items(),
        key=lambda x: x[1]["销售额"],
        reverse=True,
    )
    for name, info in sorted_products:
        ws.append([name, info["数量"], info["销售额"]])

    wb.save(filename)


def main():
    records = load_data("sales_data.xlsx")
    print_report(records)

    products = analyze_by_product(records)
    save_report(products, "product_summary.xlsx")
    print("\n商品汇总已保存到 product_summary.xlsx，可以用 Excel 打开查看")


main()
```

### 运行

确保你已经安装了 openpyxl（`pip3 install openpyxl`），然后在终端里：

```
cd 你的路径/tutorial/day8
python3 analyzer.py
```

运行后终端会打印分析报告，同时文件夹里会多出一个 `product_summary.xlsx`，直接用 Excel 打开就能看到整理好的数据。

### 代码回顾

看看 `main()` 函数，只有五行，但调度了整个程序：读取数据、打印报告、保存结果。每一步做什么一目了然。这就是用函数组织代码的好处。

再看看整个程序用到了哪些技能：

- **变量和数据类型**（Day 2）：存储金额、数量等数据
- **条件判断**（Day 3）：`if cat not in categories` 判断是否已存在
- **循环**（Day 4）：遍历每条销售记录
- **列表和字典**（Day 5）：组织和汇总数据
- **函数**（Day 6）：把逻辑拆分成独立的功能块
- **第三方库**（今天）：用 openpyxl 读写 Excel

八天学的东西，全都用上了。

## 回顾：这八天你学了什么

| 天数 | 学到的技能 |
|------|-----------|
| Day 1 | 安装环境、print、终端和 cd 命令、交互模式、看懂报错 |
| Day 2 | 变量、数据类型、input、计算、f-string |
| Day 3 | if/elif/else、比较运算、逻辑运算 |
| Day 4 | for 循环、while 循环、break/continue |
| Day 5 | 列表、字典、嵌套结构、列表推导式 |
| Day 6 | 函数定义、参数、返回值、代码组织 |
| Day 7 | 对象的概念、class、属性和方法 |
| Day 8 | pip 安装第三方库、读写 Excel、综合数据分析项目 |

## 接下来可以做什么

八天的教程到这里就结束了，但你的 Python 旅程才刚开始。

**立刻能做的事：**
- 找一个你工作中经常手动处理的 Excel 文件，试着用 Python 来自动化
- 把今天的分析工具改一改，去处理你自己的数据

**值得继续学的内容：**
- **pandas 库**：`pip3 install pandas`。专门做数据分析的工具，一行代码读取 Excel、几行代码完成筛选/分组/统计，是数据工作者的必备技能
- **matplotlib 库**：`pip3 install matplotlib`。画图表用的。做完数据分析后，直接生成柱状图、折线图、饼图
- **xlsxwriter 库**：`pip3 install xlsxwriter`。可以生成带格式的 Excel 文件（加粗、颜色、合并单元格等）

**学习资源：**
- Python 官方文档：https://docs.python.org/zh-cn/3/
- openpyxl 文档：https://openpyxl.readthedocs.io/
- 遇到问题直接搜索错误信息，Stack Overflow 上几乎什么问题都有人问过

八天时间，你已经从零基础走到了能写出实用工具的程度。继续保持好奇心和动手的习惯，Python 会成为你工作中越来越趁手的工具。

---

**配套文件下载：** [analyzer.py](downloads/analyzer.py){ download="analyzer.py" } | [sales_data.xlsx](downloads/sales_data.xlsx){ download="sales_data.xlsx" }
