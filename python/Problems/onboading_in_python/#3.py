# 369 게임
# 숫자도 string 으로 바꿔서 접근부터 생각해보자.. 

number = 33

count = 0
for num in range(1, number + 1):
    num_str = str(num)
    clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')
    count += clap_count

print(count)