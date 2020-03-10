# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:17:16 2019

@authors: Christian and Mitch
"""


def main():
    
    primes = pickPrimes()

    while(True):
        print("[1]:Encrypt with generated key\n[2]:Encrypt with provided key\n[3]:Digitally sign something")
      
        text = input("Please select what you want to do: ")
        text = int(text)
        
        if(text > 0 and text < 4):
            break
        
        
    if(text == 1):
          message = input("Please enter the message that you want to encrypt: ")
          res = encrypt(message, primes[0],primes[1])
          
          print("encrypted message: ", res[0])
          mes = input("would you like the message decrypted? (y=1/n=0) ")
          mes = int(mes)
          
          if(mes == 1):
              p = decrypt(res[0] , res[1], primes[0] * primes[1])
              print("Decrypted message: ", p)
    
    elif(text == 2):
        message = input("Please enter the message to be encrypted: ")
        key = input("Please enter the public key: ")
        key = int(key)
        res = encryptWithKey(message, key)
        print("Encrypted message: " ,res[0])
       
        mes = input("would you like the message decrypted? (y=1/n=0) ")
        mes = int(mes)
          
        if(mes == 1):
            p = decrypt(res[0] , res[1], res[2])
            print("Decrypted message: ", p)
    
    else:
        message = input("Please enter your signature: ")
        key = input("Please enter the private key: ")
        key = int(key)
        res = encryptWithKey(message, key)
        print("Your public key is: ", res[1])
        
        print("Encrypted signature: " ,res[0])
       
        mes = input("would you like the message decrypted? (y=1/n=0) ")
        mes = int(mes)
          
        if(mes == 1):
            p = decrypt(res[0], res[1], res[2])
            print("Decrypted message: ", p)
    


def pickPrimes():
    import numpy as np

    r_nums = np.random.randint(100,1000,100)
    #r_nums = [4243,4244,1212,1580,1009]
    
    primes = []
    
    x = 0
    
    for i in range(len(r_nums)):
        
        good_count = 0
        
        n = int(r_nums[i])
        
        if(len(primes) >= 2):
            return primes
        #testing carmichaels numbers
        if (n % 2 == 0 or n % 3 == 0 or n % 11 == 0 or n % 17 == 0 or n % 5 == 0 or n % 13 == 0 or n % 7 == 0 or n % 19 == 0):
            print()
        else:
                        
            for i in range(2, n): 
                if(good_count < 20):
                       #finding relative primality
                   for j in range(2, n, 2):
                       if gcd(i , n) == 1:
                           x = i
                           break  
                   if(x**(n-1) % n == 1):
                       good_count = good_count + 1
                    
                else:
                 #add it to the prime array
                 primes.append(n)
                 break
    
    return primes

def gcd(a,b):
    
    if b == 0:
        return a
    else:
        return gcd(b , a%b)


def fastExp(base, p, m):

    b = int(base)
    r = 1

   # to insure that the value is less than m
    b = b % m

    while p > 0:
        # If the power is even
        if p % 2 == 0:
            b = (b * b) % m
            p = p / 2
        else:
            r = (b * r) % m
            p = p - 1

    return r


def encrypt(message, p, q):

    n = p * q
    fn = (p-1)*(q-1)
    public_key = 0
    private_key = 0
    e_temp = []
    e_message = ""
    up_message = message.lower()

    # getting encryption key
    for i in range(2, fn):
        if gcd(i, fn) == 1:
            public_key = i
            break

    # finding multiplicative inverse
    for i in range(2, fn):
        if((public_key*i) % fn == 1):
            private_key = i
            break

    # this returns the encrypted ascii values of individual characters
    for i in up_message:
        e_temp += [fastExp(ord(i), public_key, n)]
    e_message = ''.join(str(e) for e in e_temp)
    '''
    # tester prints
    print("-------------------BEGIN---------------------")
    print("Message: ", up_message)
    print("n:              ", n)
    print("p:              ", p)
    print("q:              ", q)
    print("fn:             ", fn)
    print("Encryption Key: ", public_key)
    print("Decryption Key: ", private_key)
    print("---------------------------------------------")
    print("Encrypted Message (as string): ", e_message)
    print("")
    print("Encrypted Message (as list): ", e_temp)
    print("---------------------------------------------")
   
       
    
    decrypt(e_temp, private_key, n)
    '''
    return [e_temp, private_key, public_key]

def encryptWithKey(message, pc):

    
    
    while(True):
        primes = pickPrimes()
        fn = (primes[0]-1) * (primes[1] - 1)
        if gcd(pc , fn) == 1:
            break
    
    n =  primes[0] * primes[1]
    public_key = pc
    private_key = 0
    e_temp = []
    e_message = ""
    up_message = message.lower()

    



    # finding multiplicative inverse
    for i in range(2, fn):
        if((public_key*i) % fn == 1):
            private_key = i
            break

    # this returns the encrypted ascii values of individual characters
    for i in up_message:
        e_temp += [fastExp(ord(i), public_key, n)]
    e_message = ''.join(str(e) for e in e_temp)

    '''
    # tester prints
    print("-------------------BEGIN---------------------")
    print("Message: ", up_message)
    print("n:              ", n)
    print("p:              ", primes[0])
    print("q:              ", primes[1])
    print("fn:             ", fn)
    print("Encryption Key: ", public_key)
    print("Decryption Key: ", private_key)
    print("---------------------------------------------")
    print("Encrypted Message (as string): ", e_message)
    print("")
    print("Encrypted Message (as list): ", e_temp)
    print("---------------------------------------------")
   
    '''
    
   # decrypt(e_temp, private_key, n)
    
    return [e_temp, private_key, n]




def decrypt(e_message, private_key, n):
    
    d_temp = [chr((char ** private_key) % n) for char in e_message]
    d_message = ''.join(d_temp)
    '''
    print('Decrypted Message:', d_message)
    print("--------------------END----------------------")
    '''
    return d_message
    
    
main()