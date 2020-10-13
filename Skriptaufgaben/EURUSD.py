import requests

command = input("What amount do you want to convert into the other respective currency?\n")
command = command.replace(',','.')

if "€" in command:
    eurrate = requests.get('https://api.exchangeratesapi.io/latest').json()

    command = command.replace('€','')
    eur = float(command)
    print(eur,'€')
    print(round(eur * eurrate['rates']['USD'],2), '$')

elif "$" in command:
    usdrate = requests.get('https://api.exchangeratesapi.io/latest?base=USD').json()

    command = command.replace('$','')
    usd = float(command)
    print(usd,'$')
    print(round(usd * usdrate['rates']['EUR'],2), '€')

else:
    print("I don't know which currency you want to convert.")