import os
import time

# List to hold blocked websites
website_list = []

def blocked_collection():
    """
    Collects a list of websites to block from the user and validates their format.
    """
    global website_list
    print("What websites would you like to block? (please enter like this: www.facebook.com)")
    websites_to_block = str(input())

    # Validate format of the website
    if "www." not in websites_to_block:
        print("You did not enter the website in the right format, try again.")
        blocked_collection()

    website_list.append(websites_to_block)
    second_question()

def second_question():
    """
    Asks the user if they want to block more websites or proceed with the given list.
    """
    print("Type 'more' to add more websites to block. If you're done type 'done'.")
    answer = input()

    if answer == "more":
        blocked_collection()
    elif answer == "done":
        add_to_block()
    else:
        print("You didn't enter either term above, try again")
        second_question()

def timer():
    """
    Collects the time duration (in minutes) for which the websites should be blocked.
    """
    print("How long would you like to have your sites turned off in minutes?")
    try:
        times = int(input())
    except:
        print("That didn't work for us. Please enter a whole number like 1 to represent 1 minute of off time.")
        timer()
    actual_time = times * 60
    blocked_timer(actual_time, times)

def blocked_timer(actual_time, times):
    """
    Blocks the websites for the specified duration.
    """
    print("Turning off your blocked websites now...")
    time.sleep(3)
    print(f"Your websites are officially blocked for {times} minutes")

    # Close some common browsers (this will not truly block the websites but serves as a way to remind the user)
    os.system("Killall 'Google Chrome'")
    time.sleep(3)
    os.system("open -a Google_Chrome")
    os.system("Killall 'Safari.app'")
    os.system("Killall 'Firefox'")

    time.sleep(actual_time)
    turnoff()

def add_to_block():
    """
    Add the list of websites to the hosts file, effectively blocking them.
    """
    try:
        add_sites = open('/path/to/hosts','a')  # Adjust path accordingly
    except:
        # If there's an error while opening the file, a potential fix_login thread is executed (not provided in the initial code)
        s = threading.Thread(target=fix_login, daemon=True)
        s.start()
        s.join()

    for i in website_list:
        add_sites.write('\n\n\n' + '127.0.0.1' + '        ' + i)
        print(f"{i} has been added...")
    add_sites.close()
    
    # Read and print contents from the file (assuming for confirmation)
    host2 = open('/path/to/hosters','r')  # Adjust path accordingly
    message = host2.read()
    print(message)
    host2.close()

    timer()

def turnoff():
    """
    Reset the hosts file, effectively unblocking all the websites.
    """
    os.system("rm -r /path/to/hosts")  # Adjust path accordingly
    os.system("touch /path/to/hosts")  # Adjust path accordingly
    grab_host = open('/path/to/hosts','w')  # Adjust path accordingly
    grab_host.write('##\n# Host Database\n#\n# localhost is used to configure the loopback interface\n# when the system is booting.  Do not change this entry.\n##\n127.0.0.1       localhost\n255.255.255.255 broadcasthost\n::1             localhost')
    grab_host.close()
    
    host2 = open('/path/to/hosts','r')  # Adjust path accordingly
    message = host2.read()
    print(message)
    host2.close()

    print("Your websites are back online!")
    quit()

# Start the website collection
blocked_collection()
