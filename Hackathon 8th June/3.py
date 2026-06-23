import sys

n = int(sys.stdin.readline())
views_list = list(map(int, sys.stdin.readline().split()))

total = sum(views_list)
maximum = max(views_list)

streak = 1
streak_max = 1

for i in range(1, n):
    if views_list[i] > views_list[i-1]:
        streak += 1 
        streak_max = max(streak, streak_max)
    else:
        streak = 1

print("Total Views: ", total)
print("Average Views: ", f"{total/n :.2f}")
print("Peak Day Views: ", maximum)
print("Longest Rising Streak: ", streak_max, end ='')
print(" days")