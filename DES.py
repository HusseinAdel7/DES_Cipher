import os.path
from sys import platform
import os 
import string
from termcolor import colored
from Crypto.Cipher import DES3
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random 
from Crypto.Cipher import DES3


os.system('clear') 

print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Cryptography ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))

#------------------------------------------------------------------------  
#========================================================================
# Auto Key Cipher 

def DES_Cipher(data):
    Key =Random.new().read(24)
    iv=Random.new().read(8)
    # Mode CBC 
    print("\n")
    print("*********DES CBC Mode************")
    padding= lambda s:s+(8-len(s)%8)*"*"
    enc=DES3.new(Key,DES3.MODE_CBC,iv)
    enc_mess=enc.encrypt(padding(data).encode("ascii"))
    print(enc_mess)
    dec=DES3.new(Key,DES3.MODE_CBC,iv)
    dec_mess=dec.decrypt(enc_mess)
    NewData = dec_mess.decode("ascii")
    VeryNew=NewData.strip("*")
    print(VeryNew)
    # Mode OFB
    print("================")
    print("\n")
    print("*********DES OFB Mode************")
    enco=DES3.new(Key,DES3.MODE_OFB,iv)
    encr_message=enco.encrypt(data.encode("ascii"))
    print(encr_message)
    deco=DES3.new(Key,DES3.MODE_OFB,iv)
    decr_message=deco.decrypt(encr_message)
    AAfData = decr_message.decode("ascii")
    print(AAfData)
    #Mode CTR
    print("====================")
    print("\n")
    print("*********DES CTR Mode************")
    KeyCTR =Random.new().read(16)
    counter = Counter.new(64)
    paddingCTR= lambda s: s + ( 16 - len(s) % 16) * "*"
    encctr = DES3.new(KeyCTR,DES3.MODE_CTR,counter=counter)
    encrpted_messagectr=encctr.encrypt(paddingCTR(data).encode("ascii"))
    print(encrpted_messagectr)
    decctr = DES3.new(KeyCTR,DES3.MODE_CTR,counter=counter)
    decrpted_messagectr=decctr.decrypt(encrpted_messagectr)
    AfData = decrpted_messagectr.decode("ascii")
    ANew=AfData.strip("*")
    print(ANew)





plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
DES_Cipher(plain_Text)

#---------------------------------------------------------------------------------------
print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))

