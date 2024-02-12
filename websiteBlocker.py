from tkinter import *
import re  # Import regular expressions for pattern matching
import platform

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('THE DESTROYER')
Label(root, text='THE DESTROYER', font='arial 20 bold').pack(side=TOP)
Label(root, text='GLADE', font='arial 10 bold').pack(side=BOTTOM)
Label(root, text='BLOCK THIS: ', font='arial 15 bold').place(x=5, y=60)
Websites = Text(root, font='arial 10', height=2, width=40, wrap=WORD, padx=5, pady=5)
Websites.place(x=140, y=60)


def Blocker():

    system = platform.system()
    if system == 'Windows':
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
        redirect = '127.0.0.1'
    elif system == 'Linux':
        host_path = '/etc/hosts'
        redirect = '127.0.0.1'
    elif system == 'Darwin':  # MacOS
        host_path = '/etc/hosts'
        redirect = '127.0.0.1'
    else:
        print('Unsupported OS')
        return
    
    website_lists = Websites.get(1.0, END)
    websites = [website.strip() for website in website_lists.split(",")]  # Clean up whitespace

    with open(host_path, 'r+') as host_file:
        content = host_file.read()

        for website in websites:
            pattern = r"^\s*127\.0\.0\.1\s+" + re.escape(website) + r"\s*$"  # Exact match
            if re.search(pattern, content, flags=re.MULTILINE):
                Label(root, text='Already Blocked', font='arial 12 bold').place(x=200, y=200)
            else:
                host_file.write(redirect + " " + website + '\n')
                Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)

        host_file.truncate()  # Truncate the file to ensure changes take effect
'''
def Blocker():
    website_lists = Websites.get(1.0, END)
    websites = [website.strip() for website in website_lists.split(",")]

    for website in websites:
        try:
            answers = dns.resolver.resolve(website, 'A')  # Resolve A record
            original_ip = answers[0].to_text()  # Get the original IP address

            # Redirect to 127.0.0.1 using a local DNS server (replace with your preferred server)
            dns.resolver.override_system_resolver(dns.resolver.Resolver(configure=False))
            dns.resolver.override_system_resolver.nameservers = ['127.0.0.1']

            Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)

        except dns.resolver.NXDOMAIN:
            Label(root, text="Invalid Website", font='arial 12 bold').place(x=230, y=200)
        except dns.resolver.NoAnswer:
            Label(root, text="Could Not Resolve", font='arial 12 bold').place(x=230, y=200)
        except dns.resolver.Timeout:
            Label(root, text="DNS Timeout", font='arial 12 bold').place(x=230, y=200)
        except Exception as e:
            Label(root, text="Error: " + str(e), font='arial 12 bold').place(x=230, y=200)
'''

block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker, width=6, bg='royal blue1',
               activebackground='sky blue')
block.place(x=230, y=150)
root.mainloop()
