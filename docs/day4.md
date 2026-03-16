# Day 4：批量处理不求人

昨天我们让程序学会了做判断，今天来学一个更强大的能力：**循环**。

## 场景

假设你有一份班级成绩单，要把每个同学的分数从百分制转成等级制。一个一个手动转？要是有 200 个同学呢？

循环就是让程序自动重复做一件事。你只需要写一遍逻辑，剩下的重复劳动交给 Python。

这也是编程最让人兴奋的地方：你处理 5 条数据和处理 50000 条数据，写的代码几乎一模一样。

## for 循环：逐个处理

`for` 循环的意思是"对于这里面的每一个东西，都做一遍下面的操作"。

```python
names = ["小明", "小红", "小刚", "小美"]

for name in names:
    print(f"你好，{name}!")
```

输出：

```
你好，小明!
你好，小红!
你好，小刚!
你好，小美!
```

逐行理解：

- 第一行创建了一个列表（Day 5 会详细讲），里面有四个名字
- `for name in names:` 的意思是：每次从 `names` 里取一个值，放到 `name` 这个变量里
- 缩进的 `print` 那一行是"要重复做的事情"
- Python 会自动把列表里的值一个一个取出来，循环四次

### range()：生成一串数字

如果你想循环特定的次数，用 `range()`：

```python
for i in range(5):
    print(i)
```

输出：

```
0
1
2
3
4
```

`range(5)` 生成 0 到 4 这五个数字。注意：从 0 开始，不包含 5。这是编程界的惯例，刚开始可能不习惯，用多了就好了。

`range` 还可以指定起始值和步长：

```python
# 从 1 到 10
for i in range(1, 11):
    print(i)

# 从 0 到 100，每次加 10
for i in range(0, 101, 10):
    print(i)
```

### 在循环里做计算

循环最常见的用途是累加和统计。比如算 1 到 100 的总和：

```python
total = 0

for i in range(1, 101):
    total = total + i

print(f"1 到 100 的总和是：{total}")
```

> 小技巧：`total = total + i` 有一个简写方式：`total += i`，效果完全一样。类似的还有 `-=`、`*=`、`/=`。

## while 循环：满足条件就一直做

`for` 循环适合"我知道要做多少次"的场景。`while` 循环则适合"我不知道要做多少次，但满足某个条件就一直做下去"。

还记得 Day 3 的猜数字练习吗？当时只能猜一次，不太过瘾。用 `while` 循环可以让用户一直猜，直到猜对为止：

```python
secret = 42

guess = int(input("猜一个 1 到 100 的数字："))

while guess != secret:
    if guess > secret:
        print("太大了，再试试")
    else:
        print("太小了，再试试")
    guess = int(input("再猜一次："))

print("恭喜你，猜对了!")
```

`while guess != secret:` 的意思是：只要 `guess` 不等于 `secret`，就继续执行循环体里的代码。一旦猜对了（`guess == secret`），条件不再满足，循环结束，执行后面的 `print`。

### 小心无限循环

`while` 循环有一个陷阱：如果条件永远为真，循环就永远不会停下来。比如：

```python
# 千万别运行这段代码！
while True:
    print("停不下来了...")
```

万一不小心写出了无限循环，按 **Ctrl+C** 可以强制停止程序。

## 循环里的 break 和 continue

有时候你想在循环中途退出，或者跳过某一次循环：

**break** -- 直接结束整个循环：

```python
for i in range(100):
    if i == 5:
        print("找到 5 了，不找了")
        break
    print(i)
```

输出 0、1、2、3、4，然后"找到 5 了，不找了"。后面的 6、7、8... 不会再执行。

**continue** -- 跳过本次循环，继续下一次：

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

这段代码只输出奇数：1、3、5、7、9。遇到偶数时 `continue` 跳过了 `print`，直接进入下一次循环。

## 动手做：批量成绩统计

来写一个实用的小程序：输入一组成绩，统计平均分、最高分和最低分。

```python
print("=== 成绩统计工具 ===")
print("逐个输入成绩，输入 q 结束")
print()

scores = []
count = 0
total = 0

while True:
    user_input = input(f"请输入第 {count + 1} 个成绩（输入 q 结束）：")

    if user_input.lower() == "q":
        break

    score = float(user_input)
    scores.append(score)
    total += score
    count += 1

if count > 0:
    average = total / count
    highest = max(scores)
    lowest = min(scores)

    print()
    print(f"共录入 {count} 个成绩")
    print(f"平均分：{average:.1f}")
    print(f"最高分：{highest:.1f}")
    print(f"最低分：{lowest:.1f}")
else:
    print("没有录入任何成绩")
```

这段代码里有几个新东西，先知道怎么用就行，Day 5 会详细讲：
- `scores = []` 创建一个空列表
- `scores.append(score)` 往列表末尾添加一个元素
- `max()` 和 `min()` 分别取列表里的最大值和最小值

## 小练习

**练习 1：九九乘法表**

用两层 for 循环打印九九乘法表。提示：可以用 `print(..., end=" ")` 让 print 不换行。打完一行后用 `print()` 换行。

**练习 2：密码验证**

预设一个正确的密码。让用户输入密码，最多尝试 3 次。如果输对了就显示"登录成功"，3 次都没对就显示"账号已锁定"。

提示：可以用 `for i in range(3)` 来限制次数，配合 `break` 在猜对时退出。

**练习 3：累加计算器**

让用户不断输入数字，程序实时显示当前的累加总和。输入 0 时停止并输出最终结果。

## 今日小结

今天你学会了：

- `for` 循环：遍历列表、用 `range()` 循环特定次数
- `while` 循环：满足条件就一直执行
- 在循环里做累加和统计
- `break` 跳出循环，`continue` 跳过本次循环
- `Ctrl+C` 强制停止失控的程序

明天我们要学"列表"和"字典"，用它们来整理和管理一组数据，就像 Excel 的行和列一样。

---

**配套文件下载：** [batch.py](downloads/batch.py){ download }
