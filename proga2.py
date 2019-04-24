import hashlib

#       MD5 (код + идентификатор + длина + RequestAuth + атрибуты + секрет)

# MD5(Code+ID+Length+RequestAuth+Attributes+Secret)
code_=11                                                       #
id_=6
len='0064'
Request_Athenticator='0ca6e3402091853d31c2787f5674f35e'




all_atrib='1b06000000064f1f0102001d0410ce79ec7f045c5a9356c828b11f93c10153455256455231181920f503b3000001370001c0a83c67000000030eb7990d0050123497ac0d74367e5e9be9b26a8cc6c4f2'

our_hash='35ef916dfc2a385dadf14c5c13a068d4'

for i in range(100000):

    # наш возможный пароль
    var2=code_.to_bytes(1,'big')+id_.to_bytes(1,'big')+bytes.fromhex(len)+bytes.fromhex(Request_Athenticator)+bytes.fromhex(all_atrib)+bytes(str(i), encoding='utf-8')
    h2 = (hashlib.md5(var2)).hexdigest()

    if h2 == our_hash:
        print('our_pass----------->>>>>>>>>>', i)  ######### ответ    88C01A
        break


def convert_base(num, to_base=16, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]






code_=11                                                       #
id_=26
len='0064'
Request_Athenticator='3fa1e5ad1dede17e6c6f268b754ba74a'




all_atrib='1b06000000064f1f0102001d0410b269e723c57252b3b62ff18b4c92c1015345525645523118190fe902620000013700017f00000100000003357cd71d0050124f0fb3153bd645f0d839c2f50b994b07'

our_hash='a9d875bfa2e77da5280c1576c5d9c0b9'

for i in range(16777216):
    NUM = convert_base(i)
    # наш возможный пароль
    var2=code_.to_bytes(1,'big')+id_.to_bytes(1,'big')+bytes.fromhex(len)+bytes.fromhex(Request_Athenticator)+bytes.fromhex(all_atrib)+bytes(str(NUM), encoding='utf-8')
    h2 = (hashlib.md5(var2)).hexdigest()

    if h2 == our_hash:
        print('our_pass----------->>>>>>>>>>', NUM)  ######### ответ    88C01A
print('*')





