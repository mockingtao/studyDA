
# clean comment
def fcm(s):
	if '条' in s:
		return (int(s.split(' ')[0]))
	else:
		return('缺失数据')

def fpr(s):
	if '￥' in s:
		return (float(s.split(' ')[-1]))
	else:
		return('缺失数据')

def fcl(s):
	



path='/Users/matao/Study/data_Analyst/data_ch02_1/商铺数据.csv'
f = open(path, 'r', encoding='utf8')
for i in f.readlines()[:10]:
	cm = fcm(i.split(',')[2])
	pr = fpr(i.split(',')[4])
	print(pr)
	
