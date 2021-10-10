# if分の練習
x = 10
y = 5
if x >= 10 and y >= 10:
  print('x,yともに10以上です。')
elif x >= 10 or y >= 10:
  print('xまたはyが10以上です')
else:
  print('xもyも10未満です。')


# whileの練習
i = 1
while i < 5:
  print(i)
  i += 1


i = 3
while i:
  print(i)
  i -= 1

for i in range(1, 5):
 print(i)


# for関数、range関数の練習
for i in range(3):
  print(i)

for i in range(10, -10, -5):
  print(i)



# break文によるループの終了
num = 1
for i in range(1, 10):
  num *= 2
  print(i, num)
  if num > 20:
    break


# continueによるループスキップの練習
for i in range(1, 10):
  if i % 3 == 0 or i % 5 == 0:
    continue
  print(i)

# 多重ループ
for i in range(1, 4):
  for j in range(1, 3):
    print(i, j)
