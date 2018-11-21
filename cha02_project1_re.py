path = '/Users/matao/Study/data_Analyst/data_ch02_1/商铺数据.csv'
f = open(path, 'r',encoding='utf8')
f.seek(0)
final_data = []

def clean_comment(s):
    if '条' in s:
        return s.split(' ')[:1]
    else:
        return '无效数据' 
    
def clean_price(s):
    if '￥' in s:
        return s.split('￥')[-1]
    else:
        return '无效数据'
    
def clean_commentlist(s):
    if '\n' in s:
        return('无效数据')
    else:
        taste = float(s[0][2:])
        enviroment = float(s[1][2:])
        service = float(s[2][2:5])
        return([taste, enviroment, service])
        
    
for line in f.readlines()[1:]:
    data = line.split(',')
    classify = data[0]
    name = data[1]
    comment = clean_comment(data[2])
    star = data[3]
    price = clean_price(data[4])
    address = data[5]
    commentlist = clean_commentlist(data[-1].split('                                '))
    taste = commentlist[0]
    enviroment = commentlist[1]
    service = commentlist[2]
    if '无效数据' not in [comment,price,commentlist]:
        final_data2 = [['classify', classify], 
                    ['name',name], 
                    ['comment', comment],
                    ['star',star],
                    ['price', price],
                    ['address',address],
                    ['taste',taste],
                    ['enviroment',enviroment],
                    ['service',service]]
        print(final_data2)



    #comment = clean_comment(data[2])
    #price = clean_price(data[4])
    #print(price)
    #print(comment)
    #print(data[-1])
    #commentlist = clean_commentlist(data[-1].split('                                '))
    
    
    