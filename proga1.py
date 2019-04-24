
import hashlib
#кандидат пременяет MD5 к конкатенации ID, секретного (в данном случае разделяемого) ключа и случайной последовательности, присланной ему.

id_=2
random_number='ce79ec7f045c5a9356c828b11f93c101'
our_hash='99740999119bb0c6021d0741ff9365b4'


id_=2
random_number='364e49f697c13c77407968b44c92c101'
our_hash='16cf0431c0d9cb28221cd9a019bbba43'



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



for i in range(16777216):
    NUM = convert_base(i)
    print(NUM)
    var2=id_.to_bytes(1, 'big') + bytes(str(NUM), encoding='utf-8') + bytes.fromhex(random_number)


    #наш возможный пароль
    h2 = (hashlib.md5(var2)).hexdigest()

    if h2==our_hash:
        print('our_pass----------->>>>>>>>>>',NUM)          ######### ответ    88C01A
        break

############################################################################################################

# является криптографическим хешем, полученным с использованием алгоритма MD5 от конкатенации кода сообщения,
# идентификатора, длины сообщения, случайной последовательности, полученной сервером в пункте 1 (Request Athenticator),
#  атрибутов передаваемых в данном пакете и разделяемого секрета

