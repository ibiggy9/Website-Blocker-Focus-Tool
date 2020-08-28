import os
import time
import getpass
import threading

def fix_login():
    print("You did not run this script as a superuser, please login.")
    password = getpass.getpass()
    print(os.getcwd())
    command = 'python37 blocked.py'
    os.popen(f"sudo -S {command}", 'w').write(password)

website_list = []
def blocked_collection():
    global website_list
    print("What websites would you like to block? (please enter like this: www.facebook.com)")
    websites_to_block = input()
    
    if "www." not in websites_to_block:
        print("You did not enter the website in the right format, try again.")
        blocked_collection()
    
    website_list.append(websites_to_block)
    second_question(website_list)
  

def second_question(website_list):
    print("Type 'more' to add more websites to block. If you're done type 'done'.")
    answer = input()

    if answer == "more":
        blocked_collection()
    elif answer == "done":
        add_to_block(website_list)
    
    else:
        print("You didnt enter either term above, try again")
        second_question(website_list)
        

def timer():
    print("How long would you like to have your sites turned off in minutes?")
    try:
        times = int(input())
    except: 
        print("That didn't work for us. Please enter a whole number like 1 to represent 1 minute of off time.")
        timer()
    actual_time = times*60
    blocked_timer(actual_time, times)


def blocked_timer(actual_time, times):
    print("Turning off your blocked websites now...")
    time.sleep(3)
    print(f"Your websites are officially blocked for {times} minutes")
    os.system("Killall 'Google Chrome'")
    time.sleep(3)
    os.system("open -a Google_Chrome")
    os.system("Killall 'Safari.app'")
    os.system("Killall 'Firefox'")
    time.sleep(actual_time)
    turnoff()

def add_to_block(website_list):
    try:
        add_sites = open('/etc/hosts','a')
    except:
        s = threading.Thread(target=fix_login, daemon = True)
        s.start()
        s.join()
        


    for i in website_list:
        add_sites.write('\n\n\n' + '127.0.0.1' + '        ' + i )
        print(f"{i} has been added...")
    add_sites.close()
    host2 = open('/etc/hosters','r')
    message = host2.read()
    print(message)
    host2.close()
    timer()


def turnoff():
    os.system("rm -r /etc/hosts")
    os.system("touch /etc/hosts")
    grab_host = open('/etc/hosts','w')
    grab_host.write('##\n# Host Database\n#\n# localhost is used to configure the loopback interface\n# when the system is booting.  Do not change this entry.\n##\n127.0.0.1       localhost\n255.255.255.255 broadcasthost\n::1             localhost')
    grab_host.close()
    host2 = open('/etc/hosts','r')
    message = host2.read()
    print(message)
    host2.close()
    print("Your websites are back online!")
    quit()
  

blocked_collection()





    
           
