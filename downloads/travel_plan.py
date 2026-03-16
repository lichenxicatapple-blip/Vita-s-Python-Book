# 旅行计划清单整理工具

travel_plan = [
    {"城市": "成都", "天数": 3, "预算": 2000, "必去": "锦里、宽窄巷子"},
    {"城市": "大理", "天数": 4, "预算": 2500, "必去": "洱海、古城"},
    {"城市": "厦门", "天数": 3, "预算": 2200, "必去": "鼓浪屿、曾厝垵"},
]

print("=== 旅行计划 ===")
print()

total_days = 0
total_budget = 0

for stop in travel_plan:
    print(f"{stop['城市']}：{stop['天数']}天，预算{stop['预算']}元")
    print(f"  必去：{stop['必去']}")
    total_days += stop["天数"]
    total_budget += stop["预算"]

print()
print(f"总行程：{total_days} 天")
print(f"总预算：{total_budget} 元")

# 用列表推导式提取所有城市名
city_names = [stop["城市"] for stop in travel_plan]
print(f"途经城市：{'、'.join(city_names)}")
