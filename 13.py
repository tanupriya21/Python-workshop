def returnsum(dict):
    sum=0
    for i in dict.values():
        sum=sum+i
    return sum
dict={'data1':100,'data2':-54,'data3':247}
print("sum:",returnsum(dict))