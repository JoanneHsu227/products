#檢查檔案
import os #operating system 必須載入作業系統

products = [] #不管是否有找到都先使用空清單
if os.path.isfile('products.csv'): #相對路徑or 絕對路徑 
#詢問作業系統此檔案是否在同資料夾中
	print('是的，找到檔案')

	#讀取檔案
	with open('products.csv','r' , encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過，繼續下個迴圈
			s = line.strip().split(',')
	#		print(name,price)

			products.append([s])
	print(products)


else:
	print('否，找不到檔案')


#讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name , price] #一次一次的裝入清單
	products.append(p) #每次裝完清單就append進入大清單的車廂
print(products)
print(products[0][0]) 

for a in products: #用a一次又一次的從清單拿出來
	print(a)

#清單寫入文件裡
with open('products.csv','w' , encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
