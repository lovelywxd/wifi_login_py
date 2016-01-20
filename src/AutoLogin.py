# __author__ = 'wxd'
# Filename: AutoLogin.py
import requests


# simulate all submit procedures. send request and receive response.
# process the exception. python: how to process
def auto_login(user, passwd):
    '''hello,world!'''
    payload = {'username': user, 'password': passwd}
    login_url = "http://10.20.164.2:9997/login"
    res = requests.post(login_url, payload)
    if res.text.find("404 Not Found") >= 0:
        print("please connect the wifi Uestc_library firstly!")
    else:
        js_target = 'window.location.href="'
        start = res.text.find(js_target)+len(js_target)
        str1 = res.text[start:]
        end = str1.find('";')
        find_str = str1[0:end]
        if find_str.find("222.197.165.114:8080/login.php") < 0:
            cid = find_str[find_str.find("cid=")+len("cid="):find_str.find("&")]
            # cid = find_str[find_str.find("cid="):find_str.find("&")]  # there is a question.
            url1 = login_url+'?'+"cid="+cid+'&'+"username="+user
            print("passwd->cid: "+cid)
            print("login......")
            res1 = requests.get(url1)
            res2 = requests.get(url1)
            while res1.text == res2.text:
                res2 = requests.get(url1)
            start2 = res2.text.find(js_target)+len(js_target)
            str2 = res2.text[start2:]
            end2 = str2.find('";')
            url2 = str2[0:end2]
            print("url2: "+url2)
            if url2.find("res=success") > 0:
                print("Verify success! Continue to login.")
                # warning: meaning why do this?
                url3 = "http://10.20.164.2:9997/_allowuser.jsp?"+"cid="+cid+"&username=201421010521"
                requests.get(url3)
                requests.get(url2)
                print("login success!")
            else:
                url4 = "http://222.197.165.114:8080/pc.php?sip=10.20.164.2"
                print("Password or username wrong! Go back!"+url4)
        else:
            url1 = find_str
            print("url1: "+url1)
            print("already login!")
version = '0.1'
# End of AutoLogin.py
