# Encryption and Decryption using AES

This project is part of my Sophomore year in Bachelor of Information Technology. The project is intended to address the issues of security and ensuring the security of passwords,images and certain other formats of files
by the means of a safe and secure encryption and decryption technique based on AES by the use of a widely known library of Python in the field of Cryptography,that is,Pycrypto library.

## Getting Started

To use this project on your system, you need to follow underlying instructions:

### Prerequisites and Intallation

You need to have python installed on your system. If you don't have Python installed yet, then visit [here](https://www.python.org/getit/) .
And you should be installing Python version greater than 2.1 because Pycrypto has not been tested for Python versions that came before it.

The next step is to install pycrypto library on your system. For doing this, you simply need to enter the following command on bash(For windows users, bash is now available as [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)).

```
pip install pycrypto
```
Next thing you will be needing a xampp or wamp server for locally hosting the website.
You can download and install them from here:
[XAMPP](https://www.apachefriends.org/download.html)-an easy to install Apache distribution containing MariaDB, PHP, and Perl.
[Wampserver](http://www.wampserver.com/en/)-WampServer is a Windows web development environment. It allows you to create web applications with Apache2, PHP and a MySQL database. Alongside, PhpMyAdmin allows you to manage easily your databases.

Now download the github repository and paste it in the folder named *htdocs* inside the xampp location folder.(For more info on htdocs,click [here](https://www.phpknowhow.com/basics/working-with-xampp/)).

Now setup Xampp(or Wamp) server and open the html file downloaded within this repository.
Click on the "Get Started" button and then you will see command line opening up which runs with the hep of PHP and a small shellscript written to open up the command window.

## Running the tests

### Encryption:
Select the Encrypt option by pressing E

![](../master/images/1.JPG)

Now, enter the file to encrypt along with its password(key).

![](../master/images/2.JPG)

Sample file(image) to be encrypted:

![](../master/images/2.1.JPG)

Sample encrypted file:

![](../master/images/2.2.JPG)

**Note**: The encrypted filename has the name of the format **(encrypted)file_name**, but you can change this if you want by editing the source code in python present in the repository.

### Decryption:

Select the Decrypt option by pressing D

![](../master/images/3.JPG)

Now, enter the file to decrypt along with its original password(key) written at the time of its encryption otherwise it will not get decrypted.

![](../master/images/4.JPG)

Now, the file has been decrypted.

## Authors

**Shubham Singh Manhas**-*Tech Lead for this project*

**Satyam Gupta**-*SRS developer*

*Conceptualized and developed under the guidance of Dr. Ankita Jain Bansal(Faculty of IT at NSIT).*


