# Day 3：做个小测验分类游戏

昨天我们学了变量和计算，今天来让程序学会**做判断**。

## 场景

你在网上肯定做过那种趣味测试："测测你是什么类型的旅行者"、"你的性格像哪种动物"。这类测试的核心逻辑其实很简单：根据你的回答，走不同的分支，最后给出不同的结论。

今天我们就用 Python 来做一个这样的小测验。

## if 语句：让程序学会选择

到目前为止，我们写的代码都是"从上到下一行一行执行"。但现实中很多事情需要判断：如果天气好就出门，否则宅家里。

Python 里做判断用 `if` 语句：

```python
weather = "晴天"

if weather == "晴天":
    print("出门走走吧!")
```

几个要注意的地方：

- `==` 是判断"是否相等"，注意有**两个**等号。一个等号 `=` 是赋值（给变量装东西），两个等号 `==` 是比较
- `if` 那一行最后有一个**冒号** `:`，不能漏
- `print` 这行前面有**四个空格**的缩进。这不是为了好看，而是 Python 用来表示"这行代码属于 if 的管辖范围"。如果条件不成立，缩进里的代码就不会执行

## if-else：二选一

如果想在条件不成立时做另一件事，加上 `else`：

```python
temperature = 35

if temperature > 30:
    print("太热了，开空调!")
else:
    print("温度还行，开窗通风吧")
```

## if-elif-else：多个分支

如果有好几种情况要区分，用 `elif`（是 "else if" 的缩写）：

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

Python 从上到下逐个检查条件，第一个满足的分支会被执行，后面的就跳过了。上面这段代码里，`score` 是 85，第一个条件 `>= 90` 不满足，第二个 `>= 80` 满足，所以输出"良好"。后面的 `>= 60` 和 `else` 都不会再看了。

## 比较运算符

做判断时，我们需要比较两个值的大小或是否相等：

```python
print(5 == 5)     # True，等于
print(5 != 3)     # True，不等于
print(5 > 3)      # True，大于
print(5 < 3)      # False，小于
print(5 >= 5)     # True，大于或等于
print(5 <= 3)     # False，小于或等于
```

比较的结果是布尔值，只有 `True` 或 `False` 两种。还记得 Day 2 提到的布尔类型吗？这就是它大展身手的地方。

## 逻辑运算符：组合多个条件

有时候一个条件不够用，需要组合多个条件一起判断：

**and** -- 所有条件都满足才是 True：

```python
age = 25
income = 8000

if age >= 18 and income >= 5000:
    print("符合申请条件")
```

**or** -- 只要有一个条件满足就是 True：

```python
day = "周六"

if day == "周六" or day == "周日":
    print("周末愉快!")
```

**not** -- 取反，True 变 False，False 变 True：

```python
is_raining = False

if not is_raining:
    print("不下雨，出门走走")
```

## 动手做：趣味读书风格测验

现在我们来做一个完整的小测验：测测你是哪种类型的读书人。

```python
print("=== 测测你的读书风格 ===")
print()

score = 0

print("问题 1：你通常在什么时候看书？")
print("A. 早上，头脑清醒的时候")
print("B. 晚上，安静放松的时候")
print("C. 通勤路上，利用碎片时间")
answer1 = input("请输入你的选择（A/B/C）：").upper()

if answer1 == "A":
    score = score + 3
elif answer1 == "B":
    score = score + 2
elif answer1 == "C":
    score = score + 1

print()
print("问题 2：你更喜欢哪类书？")
print("A. 经典文学、哲学")
print("B. 小说、散文")
print("C. 实用技能、工具书")
answer2 = input("请输入你的选择（A/B/C）：").upper()

if answer2 == "A":
    score = score + 3
elif answer2 == "B":
    score = score + 2
elif answer2 == "C":
    score = score + 1

print()
print("问题 3：你一般怎么读一本书？")
print("A. 从头到尾，一字不落")
print("B. 先看目录，挑感兴趣的章节")
print("C. 随手翻翻，看到有意思的就停下来")
answer3 = input("请输入你的选择（A/B/C）：").upper()

if answer3 == "A":
    score = score + 3
elif answer3 == "B":
    score = score + 2
elif answer3 == "C":
    score = score + 1

print()
print("=== 测试结果 ===")

if score >= 8:
    print("你是「学究型读者」：严谨认真，喜欢深度思考，适合啃大部头经典。")
elif score >= 5:
    print("你是「品味型读者」：享受阅读的过程，有自己的偏好，读书是一种生活方式。")
else:
    print("你是「探索型读者」：好奇心强，什么都想翻翻看，阅读面广泛。")
```

这段代码里出现了一个新东西：`.upper()`。它的作用是把用户输入的字母统一转成大写。这样不管用户输入 "a" 还是 "A"，程序都能正确识别。

## 小练习

**练习 1：成绩等级判断**

写一个程序，让用户输入考试分数（0-100），根据分数输出等级：
- 90 分及以上：优秀
- 80-89 分：良好
- 70-79 分：中等
- 60-69 分：及格
- 60 分以下：不及格

**练习 2：猜数字**

程序里预设一个数字（比如 42），让用户猜。如果猜对了，输出"恭喜你，猜对了！"；如果猜的数字偏大，提示"太大了"；如果偏小，提示"太小了"。

**练习 3：判断闰年**

让用户输入一个年份，判断它是不是闰年。闰年的规则是：
- 能被 4 整除，但不能被 100 整除
- 或者能被 400 整除

提示：用 `%` 取余来判断能否整除。`year % 4 == 0` 表示能被 4 整除。

## 今日小结

今天你学会了：

- 用 `if` 让程序根据条件做不同的事情
- `if-else` 处理二选一的情况
- `if-elif-else` 处理多个分支
- 比较运算符：`==`、`!=`、`>`、`<`、`>=`、`<=`
- 逻辑运算符：`and`、`or`、`not`
- 用 `.upper()` 统一用户输入的大小写

明天我们要学"循环"，让程序自动重复做事情，批量处理数据。

---

**配套文件下载：** [quiz.py](downloads/quiz.py){ download }
