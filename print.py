#/usr/bin/python
#coding=utf-8
f=open('d:/repo/MS/print.txt','w')
f.seek(40,0)
f.write('公司名称:\n\n')
f.seek(25,1)
f.write('收货方')
f.seek(25,1)
f.write('发货方\n')
f.seek(28,1)
f.write('姓名:')
f.seek(28,1)
f.write('姓名:\n')
f.seek(28,1)
f.write('联系方式:')
f.seek(24,1)
f.write('联系方式:\n')
f.seek(28,1)
f.write('地址:')
f.seek(28,1)
f.write('地址:\n')
f.write('-'*1000+'\n')
f.write('产品型号:\t'+'单价:\t'+'数量:\t'+'总价:\n')
f.write('\n'*15)
f.write('-'*1000+'\n')
f.seek(80,1)
f.write('合计:\n')
f.seek(80,1)
f.write('库存:\n\n')
f.seek(80,1)
f.write('开单人:\n')
f.seek(80,1)
f.write('日期:\n')
f.close()


