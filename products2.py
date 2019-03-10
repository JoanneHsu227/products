#檢查檔案
import os #operating system 必須載入作業系統

def read_file(filename): #讀取檔案
	products = [] #不管是否有找到都先使用空清單
	with open(filename,'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過，繼續下個迴圈
			name, price = line.strip().split(',')
		#		print(name,price)
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
#	products = []
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		products.append([name,price]) #每次裝完清單就append進入大清單的車廂
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products: #用a一次又一次的從清單拿出來
		print(p[0], '的價格是', p[1])

#清單寫入文件裡
def write_file(filename , products):
	with open(filename ,'w' ) as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #相對路徑or 絕對路徑 
	#詢問作業系統此檔案是否在同資料夾中
		print('是的，找到檔案')
		products = read_file(filename)
	else:
		print('否，找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv' , products)

main()