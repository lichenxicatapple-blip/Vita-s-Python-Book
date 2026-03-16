# 趣味读书风格测验

print("=== 测测你的读书风格 ===")
print()

score = 0

# 问题 1
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

# 问题 2
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

# 问题 3
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

# 根据总分输出结果
print()
print("=== 测试结果 ===")

if score >= 8:
    print("你是「学究型读者」：严谨认真，喜欢深度思考，适合啃大部头经典。")
elif score >= 5:
    print("你是「品味型读者」：享受阅读的过程，有自己的偏好，读书是一种生活方式。")
else:
    print("你是「探索型读者」：好奇心强，什么都想翻翻看，阅读面广泛。")
