scores = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 95, "数学": 91, "英语": 93},
    "王五": {"语文": 56, "数学": 56, "英语": 96},
    "赵六": {"语文": 87, "数学": 78, "英语": 95},
    "孙七": {"语文": 89, "数学": 68, "英语": 94},
}
#嵌套字典命名

# 2. 计算总分 & 平均分
def calc(stu):
    total = sum(scores[stu].values())
    avg = total / 3
    return total, avg

for stu in scores:
    t, a = calc(stu)
    print(f"{stu}: 总分={t}, 平均分={a:.1f}")

# 3. 补充新同学
scores["郑十"] = {"语文": 92, "数学": 91, "英语": 86}
print("\n已添加郑十")

# 4. 找总分最高
best_student = max(scores, key=lambda s: calc(s)[0])
best_total, _ = calc(best_student)
print(f"\n总分最高：{best_student}，总分={best_total}")

# 5. 给赵六数学 +5 并更新
scores["赵六"]["数学"] += 5
t, a = calc("赵六")
print(f"\n赵六数学+5 后：总分={t}, 平均分={a:.1f}")

# 6. 每科平均分 & 最高分学生
subjects = ["语文", "数学", "英语"]
for sub in subjects:
    vals = [scores[stu][sub] for stu in scores]
    avg_sub = sum(vals) / len(vals)
    max_sub = max(vals)
    tops = [stu for stu in scores if scores[stu][sub] == max_sub]
    print(f"\n{sub} 平均分={avg_sub:.1f}，最高分学生：{','.join(tops)}")
