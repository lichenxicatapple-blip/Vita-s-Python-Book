# Day 7：认识对象 -- 点号背后的秘密

学到这里，你可能已经注意到一个奇怪的现象：有些操作是 `函数名(数据)` 的写法，比如 `len(scores)`、`print(name)`；而有些操作是 `数据.操作名()` 的写法，比如 `scores.append(1)`、`name.upper()`。

为什么会这样？今天我们来揭开这个谜底。

## 你其实一直在用"对象"

在 Python 里，几乎所有东西都是**对象**。一个字符串是对象，一个列表是对象，一个数字也是对象。

对象是什么？简单说，对象就是**数据和操作打包在一起的东西**。

拿字符串来举例。`"你好"` 这个字符串不仅仅是两个字，它还自带了一套操作方法：

```python
text = "hello, python"

print(text.upper())        # HELLO, PYTHON（全部转大写）
print(text.title())        # Hello, Python（每个单词首字母大写）
print(text.replace("python", "world"))  # hello, world（替换内容）
print(text.split(", "))    # ['hello', 'python']（按分隔符拆分）
```

这些用点号 `.` 调用的操作，叫做对象的**方法**。方法是"属于某个对象的函数"。

列表也是一样：

```python
fruits = ["苹果", "香蕉", "橘子"]

fruits.append("葡萄")     # 在末尾添加
fruits.insert(0, "西瓜")  # 在指定位置插入
fruits.sort()              # 排序
fruits.reverse()           # 反转
```

### 方法和函数的区别

- **函数**（如 `len()`、`print()`、`max()`）是独立的工具，你把数据传给它，它处理完返回结果
- **方法**（如 `.append()`、`.upper()`、`.sort()`）是对象自带的操作，通过点号调用

打个比方：`len(scores)` 像是你拿一把尺子去量列表有多长；`scores.sort()` 像是列表自己主动把里面的东西排好序。

两者在实际使用中经常配合，不需要纠结什么时候用哪种，用多了自然就记住了。

## 对象还有"属性"

除了方法（能做的事），对象还可以有**属性**（自带的数据）。属性也用点号访问，但不带括号：

```python
text = "hello"
# 字符串没有太多直接可见的属性，但后面我们自己定义的对象会大量用到

# 一个直观的例子：复数
c = 3 + 4j       # Python 支持复数，这里只是演示属性的用法
print(c.real)     # 3.0（实部，这是属性）
print(c.imag)     # 4.0（虚部，这是属性）
```

记住：**带括号的是方法（做事），不带括号的是属性（取值）**。

## 为什么需要"对象"这种设计

在学怎么自己造对象之前，先聊聊：为什么编程语言要搞出"对象"这个概念？

早期的编程方式是这样的：数据归数据，函数归函数，两边分开管理。你定义一堆变量来存数据，再定义一堆函数来处理这些数据。代码少的时候没什么问题，但一旦程序变大，你就会遇到麻烦。

想象你在管理一个通讯录。用之前学的方式，你可能会这么写：

```python
# 数据散落各处
name1 = "小明"
phone1 = "13800138000"
email1 = "xiaoming@example.com"

name2 = "小红"
phone2 = "13900139000"
email2 = "xiaohong@example.com"

# 函数也不知道该配哪些数据
def show_contact(name, phone, email):
    print(f"{name}: {phone}, {email}")
```

只有两个联系人还凑合，如果有 200 个呢？变量名怎么取？传参数时 `name1` 和 `phone2` 不小心配错了怎么办？

问题的根源在于：**姓名、电话、邮箱明明是属于同一个人的信息，却被拆散存在了不相关的变量里**。

对象的设计思想就是解决这个问题：**把紧密相关的数据和操作绑在一起，当作一个整体来管理**。

这其实很符合人的自然思维。你在生活中不会把"杯子的颜色"、"杯子的容量"和"用杯子喝水"这三件事分开想。它们天然就属于同一个东西 -- 杯子。对象的设计让代码也能这样组织：把属于同一个事物的一切收纳在一起。

数据量小的时候你可能感受不明显，但当程序复杂起来，这种"把相关的东西打包在一起"的思路会让代码清晰得多，也不容易出错。

## 自己定义一个对象：class

Python 自带的字符串、列表、字典都是别人写好的对象类型。我们也可以自己定义新的类型，用 `class` 关键字。

用 class 来定义一个联系人类型：

```python
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def show(self):
        print(f"姓名：{self.name}")
        print(f"电话：{self.phone}")
        if self.email:
            print(f"邮箱：{self.email}")
```

一行一行来看：

- `class Contact:` -- 定义一个叫 Contact 的类。类名习惯用大写字母开头
- `def __init__(self, name, phone, email=""):` -- 这是一个特殊方法，在创建对象时自动执行。`__init__` 前后各有两个下划线。它的作用是设定这个对象有哪些属性
- `self` -- 代表对象自己。每个方法的第一个参数都是 `self`，调用时不用手动传，Python 会自动处理
- `self.name = name` -- 把传入的 `name` 参数保存为对象的属性。之后可以用 `对象.name` 来访问
- `def show(self):` -- 定义一个方法，用来展示联系人信息

使用方法：

```python
# 创建两个联系人对象
alice = Contact("Alice", "13800138000", "alice@example.com")
bob = Contact("Bob", "13900139000")

# 访问属性
print(alice.name)     # Alice
print(bob.phone)      # 13900139000

# 调用方法
alice.show()
print()
bob.show()
```

输出：

```
姓名：Alice
电话：13800138000
邮箱：alice@example.com

姓名：Bob
电话：13900139000
```

对比一下之前的写法：以前 `name1`、`phone1`、`email1` 散落各处，现在 `alice.name`、`alice.phone`、`alice.email` 都绑定在 `alice` 这个对象上。谁的信息一目了然，不可能配错。

### self 到底是什么

`self` 是最容易让初学者困惑的点。其实它就是"这个对象自己"。

当你写 `alice.show()` 时，Python 在背后做的事情相当于 `Contact.show(alice)`，把 `alice` 传给了 `self`。所以方法内部的 `self.name` 就是 `alice.name`。

你只需要记住两条规则：
1. 定义方法时，第一个参数永远写 `self`
2. 在方法内部访问对象的属性和其他方法，都通过 `self.xxx`

## 给对象添加更多功能

让我们给 Contact 类加点实用的方法：

```python
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def show(self):
        """展示联系人信息"""
        print(f"姓名：{self.name}")
        print(f"电话：{self.phone}")
        if self.email:
            print(f"邮箱：{self.email}")

    def to_dict(self):
        """把联系人转成字典格式"""
        return {
            "姓名": self.name,
            "电话": self.phone,
            "邮箱": self.email,
        }

    def update_phone(self, new_phone):
        """更新电话号码"""
        self.phone = new_phone
        print(f"{self.name} 的电话已更新为 {new_phone}")
```

```python
alice = Contact("Alice", "13800138000", "alice@example.com")

# 更新电话
alice.update_phone("13700137000")

# 转成字典
print(alice.to_dict())
```

每个方法做一件事，职责清晰。想加新功能？再定义一个方法就行。

## 动手做：通讯录管理器

把 Contact 类用起来，做一个小型通讯录。这次我们用两个类配合：`Contact` 代表单个联系人，`AddressBook` 代表整个通讯录。

```python
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def show(self):
        """展示联系人信息"""
        info = f"  {self.name} | {self.phone}"
        if self.email:
            info += f" | {self.email}"
        print(info)


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email=""):
        """添加联系人"""
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"已添加联系人：{name}")

    def search(self, keyword):
        """按姓名搜索联系人"""
        results = [c for c in self.contacts if keyword in c.name]
        if results:
            print(f"找到 {len(results)} 个结果：")
            for c in results:
                c.show()
        else:
            print("没有找到匹配的联系人")

    def show_all(self):
        """显示所有联系人"""
        if not self.contacts:
            print("通讯录为空")
            return
        print(f"共 {len(self.contacts)} 个联系人：")
        for c in self.contacts:
            c.show()


def main():
    book = AddressBook()

    while True:
        print("\n=== 通讯录 ===")
        print("1. 添加联系人")
        print("2. 搜索联系人")
        print("3. 查看全部")
        print("4. 退出")

        choice = input("请选择操作（1-4）：")

        if choice == "1":
            name = input("姓名：")
            phone = input("电话：")
            email = input("邮箱（没有就直接按回车）：")
            book.add(name, phone, email)
        elif choice == "2":
            keyword = input("请输入要搜索的姓名：")
            book.search(keyword)
        elif choice == "3":
            book.show_all()
        elif choice == "4":
            print("再见!")
            break
        else:
            print("无效的选择，请输入 1-4")


main()
```

注意 `AddressBook` 内部用到了 `Contact`：`add` 方法创建一个 Contact 对象，存到自己的 `self.contacts` 列表里。对象之间可以这样组合使用，就像现实中"通讯录"里包含多张"名片"。

## 小练习

**练习 1：图书类**

定义一个 `Book` 类，属性包含书名、作者和价格。添加一个 `discount(rate)` 方法，返回打折后的价格。创建几本书的对象，调用 discount 看看结果。

**练习 2：成绩单类**

定义一个 `Student` 类，属性包含姓名和一个成绩列表。添加以下方法：
- `add_score(score)` 添加一门成绩
- `average()` 返回平均分
- `highest()` 返回最高分
- `show_report()` 打印成绩报告

**练习 3：改进通讯录**

给上面的通讯录添加"删除联系人"功能。提示：可以先搜索找到联系人，然后用列表的 `.remove()` 方法删除。

## 今日小结

今天你学会了：

- Python 里几乎所有东西都是**对象**，对象 = 数据 + 操作
- 用点号调用的是**方法**（对象自带的函数）和**属性**（对象自带的数据）
- 对象背后的设计哲学：把紧密相关的数据和操作绑在一起，让代码的组织方式更接近人的自然思维
- 用 `class` 定义自己的对象类型
- `__init__` 方法在创建对象时自动执行，用来设定属性
- `self` 代表对象自身
- 多个类可以组合使用

明天是最后一天，我们要读取真实的 CSV 数据文件，用前七天学的所有技能做一个完整的数据分析项目。
