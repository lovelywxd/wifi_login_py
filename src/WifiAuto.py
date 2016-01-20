"""
    target:
    1. auto scan the system wifi and connect.
    2. auto login. include solve the verify code(big questions),like CMCC.
    3. process the exception.  Complete wifi_login script. if the verification of username&password failed,
    if the response of server is overtime, and if others that need process.
    4. include four part.
    5. the exception process and the log memory.


    NOW: coding....not complete.
"""
import AutoLogin
# import time

if __name__ == '__main__':
    # file_name = 'login_history'
    # f = open(file_name, 'w')
    # file_content = 'Login Time: ' + time.asctime() + '\n'
    print(help(AutoLogin))
    # print(AutoLogin.auto_login.__doc__)
    username = '201421010521'
    password = 'lovelywxd'
    print("username " + username+" is try to login.")
    # file_content += help(AutoLogin)
    # f.write(file_content)
    # f.close()
    AutoLogin.auto_login(username, password)
