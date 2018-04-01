import os,random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key,filename):
    chunksize=64*1024  #maximum size of the data
    outputFile="(encrypted)"+filename  #name of the file where encrypted image is to be stored.
    filesize=str(os.stat(filename).st_size).zfill(16)  #size of the chosen file for encryption.
    #os.path.getsize(filename) returns the same thing
    #as os.stat(filename).st_size
    IV='' #Initialization Vector

    for i in range(16):
        IV+=chr(random.randint(0,0xFF))   #choosing a random 16-byte IV

    encryptor=AES.new(key,AES.MODE_CBC,IV)   #creating encryptor cipher which uses AES
    with open(filename,'rb') as infile:  #input file opened in read-binary mode
        with open(outputFile,'wb') as outfile:  #output file opened to write the output of encrytion into it
            outfile.write(filesize)
            outfile.write(IV)
            while True:
                chunk=infile.read(chunksize)
                if len(chunk)==0:
                    break        #if there is nothing in the input file, nothing left to be encrypted
                elif len(chunk)%16!=0:
                    chunk+=' '*(16-(len(chunk)%16))   #if length of the chunk does not fit the 16 byte block of data, then do padding on the
                                                      #remaining blocks of data to make encryption consistent.
                #finally write the encrypted data into the output file.
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key,filename):
    chunksize=64*1024   #maximum size of the data
    outputFile=filename[11:]  #first 11 characters are removed for not including '(encrypted)' in the name of
                              #decrypted file

    with open(filename,'rb') as infile:   #input file opened in read-binary mode
        filesize=long(infile.read(16))
        IV=infile.read(16)     #IV is same as the output of encrypt

        decryptor=AES.new(key,AES.MODE_CBC,IV)  #creating decryptor cipher which uses AES
        with open(outputFile,'wb') as outfile:  #creating output file for posting the output of decryption into it
            while True:
                chunk=infile.read(chunksize)
                if len(chunk)==0:
                    break                    #if nothing in the chunk, no decryption needed
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)     #truncating all the padding added at the time of encryption process
                                           #and reduces the size of the output file to that of the original file.

#utility function for generating key

def getKey(password):
    hasher=SHA256.new(password)  #SHA2(Secure Hashing Algorithm 2 series) algorithm used for getting a unique hash for given password
    return hasher.digest()  #returns a bytestring of the hasher hash produced by the SHA2 algorithm

#main function

def Main():
    choice=raw_input("Select (E)ncrypt or (D)ecrypt: ")
    if choice=='E':
        filename=raw_input("File to encrypt: ")
        password=raw_input("Password: ")
        encrypt(getKey(password),filename)
        print "Done."
    elif choice=='D':
        filename=raw_input("File to decrypt: ")
        password=raw_input("Password: ")
        decrypt(getKey(password),filename)
        print "Done."
    else:
        print "No option selected, closing..."

if __name__=='__main__':
    Main()
