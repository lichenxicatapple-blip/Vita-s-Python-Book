# 通讯录管理器

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
