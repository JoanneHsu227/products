products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name , price] #一次一次的裝入清單
	products.append(p) #每次裝完清單就append進入大清單的車廂
print(products)
print(products[0][1]) 

for a in products: #用a一次又一次的從清單拿出來
	print(a)

with open('products.csv','w' , encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')