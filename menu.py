#讀取檔案
menu=[]
with open('美食menu.txt', 'r', encoding='utf-8') as f:
	for word in f:
		if '美食,價格' in word:
			continue
		item, price = word.strip().split(',')
		menu.append([item, price])
print(menu)

#讓使用者寫入檔案
while True:
	name = input('請輸入食物品名')
	if name == 'q':
		break
	price1 = input('請輸入價格')
	menu.append([name, price1])

#印出所有購買紀錄
for k in menu:
	print('美食名稱是',k[0],'價格是',k[1])

#寫入檔案
with open('menu_update.txt','w',encoding = 'utf-8') as file:
	file.write('商品,價格\n')
	for t in menu:
		file.write(t[0] + ',' + t[1] + '\n')