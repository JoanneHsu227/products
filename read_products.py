products = []
with open('products.csv','r' , encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳過，繼續下個迴圈
		s = line.strip().split(',')
#		print(name,price)

		products.append([s])
print(products)