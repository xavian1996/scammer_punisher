import requests
import random
import string
import threading
import time

#function to generate random emails and passwords
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def send_data():
    #url to send data to
    url = "https://godsrods.com/P2dvZHM9N0M0czJGOGUxeDdN"

    #dict containe data ti be sent !
    data_dic = {'mima':random_char(7) + "gmail.com",'poussa':random_char(100),'Connexion':'submit'}
    response = requests.post(url,data = data_dic)
    if response:

        print(f"Data Sent => {count}")
        print(f'Status Code => {response.status_code}')

    else:
        print('Faield To Send Data')
count = 0

while True:#looping the fuction to make it send data to the infinite XD
    try :
        count += 1
        thread1 = threading.Thread(target=send_data(),args=())
        thread2 = threading.Thread(target=send_data(), args=())

        print('Thread 1 => ')
        thread1.start()
        print('-------------------')
        print('Thread 2 => ')
        thread2.start()

    except:
        print("Failed to send data !")
