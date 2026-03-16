# Day 6：别重复自己

前五天下来，你可能已经发现一个问题：有些代码写了好几遍，每次都差不多。比如"读取用户输入并转成数字"、"计算一组数据的平均值"，每次都重写一遍很烦。

今天学的**函数**，就是解决这个问题的。

## 什么是函数

函数就是**一段有名字的代码块，可以反复调用**。

你其实已经用过很多函数了：`print()`、`input()`、`len()`、`max()`、`round()`... 这些都是 Python 自带的函数。今天我们要学的是自己写函数。

打个比方：你做菜时经常需要"切丁"这个操作。与其每次都从头描述怎么切，不如把它总结成一个步骤叫"切丁"，以后直接说"把胡萝卜切丁"就行了。函数就是你自己总结出来的"操作步骤"。

## 定义一个函数

用 `def` 关键字定义函数：

```python
def greet():
    print("你好！欢迎来到 Python 世界！")
```

- `def` 是 "define"（定义）的缩写
- `greet` 是函数的名字，你自己取
- 名字后面的小括号 `()` 不能省
- 冒号 `:` 和缩进的规则和 `if`、`for` 一样

定义函数不会执行里面的代码，只是"登记"了这个操作。要执行它，需要**调用**：

```python
greet()     # 输出：你好！欢迎来到 Python 世界！
greet()     # 可以调用多次
```

## 参数：让函数更灵活

上面的 `greet()` 每次输出的内容都一样，不太灵活。加上**参数**，就能让函数处理不同的数据：

```python
def greet(name):
    print(f"你好，{name}！欢迎来到 Python 世界！")

greet("小明")    # 你好，小明！欢迎来到 Python 世界！
greet("小红")    # 你好，小红！欢迎来到 Python 世界！
```

`name` 就是参数，相当于一个占位符。调用时传入具体的值，函数内部就用这个值来工作。

可以有多个参数：

```python
def introduce(name, city, hobby):
    print(f"我叫{name}，来自{city}，喜欢{hobby}")

introduce("小明", "成都", "看书")
introduce("小红", "杭州", "旅行")
```

### 默认参数

有些参数可以给一个默认值，调用时如果不传就用默认的：

```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("小明")               # 你好，小明！
greet("小明", "早上好")      # 早上好，小明！
```

## 返回值：让函数给你一个结果

函数不仅能"做事"（比如打印），还能"算出一个结果"交给你。用 `return` 把结果返回：

```python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

scores = [85, 92, 78, 90, 88]
avg = calculate_average(scores)
print(f"平均分：{avg:.1f}")    # 平均分：86.6
```

`return` 做两件事：把值交出去，同时结束函数的执行。

没有 `return` 的函数（或者只写 `return` 不带值）返回 `None`，表示"没有结果"。

### return 和 print 的区别

初学者容易混淆这两个。简单说：

- `print()` 是给人看的，把内容显示在屏幕上
- `return` 是给程序用的，把结果交给调用者，可以存到变量里继续使用

```python
def add_print(a, b):
    print(a + b)       # 显示在屏幕上，但没有返回值

def add_return(a, b):
    return a + b       # 返回结果，不显示在屏幕上

result1 = add_print(1, 2)    # 屏幕显示 3，但 result1 是 None
result2 = add_return(1, 2)   # 屏幕不显示，result2 是 3

print(result2 * 10)           # 30，可以继续用这个结果
```

## 实际例子：重构 AA 制计算器

还记得 Day 2 的 AA 制计算器吗？我们用函数重写一下，让代码更清晰：

```python
def get_number(prompt, number_type=float):
    """获取用户输入并转成数字"""
    while True:
        user_input = input(prompt)
        try:
            return number_type(user_input)
        except ValueError:
            print("输入不合法，请输入一个数字")

def calculate_share(total, people, tip_rate=0):
    """计算每人应付金额（含小费）"""
    total_with_tip = total * (1 + tip_rate / 100)
    return round(total_with_tip / people, 2)

def main():
    print("=== AA 制聚餐费用计算器 ===")

    total = get_number("请输入聚餐总金额：")
    people = get_number("请输入聚餐人数：", int)
    tip_rate = get_number("请输入小费比例（%，不需要就输入 0）：")

    per_person = calculate_share(total, people, tip_rate)

    print(f"\n总金额：{total:.2f} 元")
    if tip_rate > 0:
        print(f"小费：{tip_rate}%")
    print(f"聚餐人数：{people} 人")
    print(f"每人应付：{per_person:.2f} 元")

main()
```

对比 Day 2 的版本，这个版本：

- `get_number()` 函数封装了"获取输入并转类型"的逻辑，还加上了输入校验。写一次，用三次
- `calculate_share()` 把计算逻辑独立出来，一看函数名就知道它干什么
- `main()` 函数把主流程串起来，读起来像一篇简短的说明文

这段代码里出现了两个新东西，简单说明一下：

- `try/except`：尝试执行某个操作，如果出错就执行另一段代码，而不是让程序崩溃。这里用来处理用户输入了非数字的情况
- 函数定义下面用三引号 `"""..."""` 写的那行文字叫**文档字符串**，用来说明这个函数是干什么的。不影响运行，但能帮你和别人理解代码

## 变量的作用域

函数内部创建的变量，只在函数内部有效，外面访问不到：

```python
def my_function():
    secret = "只有函数内部能看到我"
    print(secret)

my_function()       # 正常输出
# print(secret)     # 报错！函数外面不认识 secret
```

这是个好事情。每个函数管好自己的变量，不会互相干扰。

## 小练习

**练习 1：温度转换函数**

写两个函数：
- `celsius_to_fahrenheit(c)` 把摄氏度转成华氏度
- `fahrenheit_to_celsius(f)` 把华氏度转成摄氏度

然后写一个小程序，让用户选择转换方向，输入温度，输出结果。

**练习 2：成绩等级函数**

写一个函数 `get_grade(score)`，输入分数返回等级（"优秀"、"良好"、"中等"、"及格"、"不及格"）。然后用这个函数处理一组成绩，输出每个人的等级。

**练习 3：简易通讯录（函数版）**

把 Day 5 练习里的通讯录改成函数版。定义这些函数：
- `add_contact(contacts, name, phone)` 添加联系人
- `find_contact(contacts, name)` 查找联系人
- `show_all(contacts)` 显示所有联系人

用一个 `while` 循环做主菜单，让用户选择操作。

## 今日小结

今天你学会了：

- 用 `def` 定义函数，把重复的逻辑封装起来
- 用**参数**让函数处理不同的数据
- 用**默认参数**简化调用
- 用 `return` 返回计算结果
- `return` 和 `print` 的区别
- 变量的作用域：函数内的变量只在函数内有效

明天我们要学"对象"，搞清楚 `.upper()`、`.append()` 这些点号操作背后的秘密。
