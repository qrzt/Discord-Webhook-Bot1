import requests

banner = """

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝░░░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░░░██╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░██╔╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗██╔╝░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝



"""
print(banner)

options = """
[1] Normal Mode
[2] Spam Mode

"""




def normal_mode():
    url = input("Enter Webhook URL: ")
    custom_user = input("Enter Custom Username: ")

    while True:
        content = str(input("Enter Message: "))
        data = {
            'content' : content,
            'username' : custom_user
        }

        response = requests.post(url,json=data)

        if response.status_code == 204:
            print("Message Sent.")
        else:
            print("ERROR: {response.status_code}")



def spam_mode():
    url = input("Enter Webhook URL: ")
    custom_user = input("Enter Custom Username: ")
    content = str(input("Enter Message: "))
    amt = int(input("How Many Messages To Send: "))


    for i in range(amt):

        data = {
            'content' : content,
            'username' : custom_user
        }

        response = requests.post(url,json=data)

        if response.status_code == 204:
            print("Message Sent.")
        else:
            print("ERROR: {response.status_code}")


print(options)
userinput = str(input(" "))
if userinput == "1":
    normal_mode()
    userinput = str(input(" "))
elif userinput == "2":
    spam_mode()
    userinput = str(input(" "))
