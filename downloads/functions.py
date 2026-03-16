# 用函数重构 AA 制聚餐费用计算器

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
    print("=== AA 制聚餐费用计算器（函数版） ===")

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
