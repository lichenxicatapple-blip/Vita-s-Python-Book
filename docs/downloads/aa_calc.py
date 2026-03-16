# AA 制聚餐费用计算器

print("=== AA 制聚餐费用计算器 ===")

# 获取用户输入，input() 返回的是字符串，需要转成数字
total = float(input("请输入聚餐总金额："))
people = int(input("请输入聚餐人数："))

# 计算每人应付金额
per_person = total / people

# 格式化输出结果，:.2f 表示保留两位小数
print(f"总金额：{total:.2f} 元")
print(f"聚餐人数：{people} 人")
print(f"每人应付：{per_person:.2f} 元")
