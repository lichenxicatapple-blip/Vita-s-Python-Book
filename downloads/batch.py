# 批量成绩统计工具

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
