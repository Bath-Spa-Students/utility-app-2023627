print (
    """welcome to
░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█ 　 ░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ 
─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄ 　 ░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ 
──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ 　 ░█──░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄""")
print("""Drinks
    _______________________________________
   | items   | price  | stock |  code      |
   |_________|________|_______|____________|
   |juice    |1 AED   |   5   |A01         |
   |pepsi    |4 AED   |   3   |A02         |
   |prime    |30 AED  |   7   |A03         |
   |red bull |10 AED  |   4   |A04         |
   |water    |1 AED   |   5   |A05         |
   |_________|________|_______|____________|""")
print(""" snacks
    _______________________________________
   | items   | price  | stock |  code      |
   |_________|________|_______|____________|
   |Cheetos  |10 AED  |   5   |B01         |
   |Oreo     |3 AED   |   4   |B02         |
   |lays     |2 AED   |   6   |B03         |
   |Takis    |14 AED  |   7   |B04         |
   |snickers |3 AED   |   6   |B06         |
   |_________|________|_______|____________|""")
      
a=str(input("-------------------------------------\nEnter the product code:\n"))
if a=='A01':
    print('you have choosen juice')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    juice = 1*b
    if c==juice:
       print("Take your juice")
    elif c>juice:
       print("Take your change with juice",c-juice)
    elif c<juice:
        print("Add more money",juice-c)
        float(input("pay the rest of the amount):\n"))
if a=='A02':
    print('you have choosen pepsi')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    pepsi = 4*b
    if c==pepsi:
       print("Take your pepsi")
    elif c>pepsi:
       print("Take your change with pepsi",c-pepsi)
    elif c<pepsi:
        print("Add more money",pepsi-c)
        float(input("pay the rest of the amount):\n"))
if a=='A03':
    print('you have choosen prime')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    prime = 30*b
    if c==prime:
       print("Take your prime")
    elif c>prime:
       print("Take your change with prime",c-prime)
    elif c<prime:
        print("Add more money",prime-c)
        float(input("pay the rest of the amount):\n"))
if a=='A04':
    print('you have choosen red bull')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    red_bull = 10*b
    if c==red_bull:
       print("Take your red bull")
    elif c>red_bull:
       print("Take your change with red bull",c-red_bull)
    elif c<red_bull:
        print("Add more money",red_bull-c)
        float(input("pay the rest of the amount):\n"))
if a=='A05':
    print('you have choosen water')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    water = 1*b
    if c==water:
       print("Take your water")
    elif c>water:
       print("Take your change with water",c-water)
    elif c<water:
        print("Add more money",water-c)
        float(input("pay the rest of the amount):\n"))
if a=='B01':
    print('you have choosen cheetos')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    cheetos = 10*b
    if c==cheetos:
       print("Take your cheetos")
    elif c>cheetos:
       print("Take your change with cheetos",c-cheetos)
    elif c<cheetos:
        print("Add more money",cheetos-c)
        float(input("pay the rest of the amount):\n"))
if a=='B02':
    print('you have choosen oreo')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    oreo = 3*b
    if c==oreo:
       print("Take your oreo")
    elif c>oreo:
       print("Take your change with oreo",c-oreo)
    elif c<oreo:
        print("Add more money",oreo-c)
        float(input("pay the rest of the amount):\n"))
if a=='B03':
    print('you have choosen lays')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    lays = 2*b
    if c==lays:
       print("Take your lays")
    elif c>lays:
       print("Take your change with lays",c-lays)
    elif c<lays:
        print("Add more money",lays-c)
        float(input("pay the rest of the amount):\n"))
if a=='B04':
    print('you have choosen takis')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    takis = 14*b
    if c==takis:
       print("Take your takis")
    elif c>takis:
       print("Take your change with takis",c-takis)
    elif c<takis:
        print("Add more money",takis-c)
        float(input("pay the rest of the amount):\n"))
if a=='B05':
    print('you have choosen snickers')
    b=float(input("How many?(please add after seeing stock in table):\n"))
    c=float(input("pay the amount:\n"))
    snickers = 3*b
    if c==snickers:
       print("Take your snickers")
    elif c>snickers:
       print("Take your change with snickers",c-snickers)
    elif c<snickers:
        print("Add more money",snickers-c)
        float(input("pay the rest of the amount):\n"))      

while True:
     d = str(input("Buy something else? yes/no:\n"))

     if d == 'no':
        print("\nTHANK YOU for using the vending machine")
        break
     elif d == 'yes':
        a = str(input("-------------------------------------\nEnter the product code:\n"))

        if a == 'A01':
            print('you have chosen juice')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            juice = 1 * b
            if c == juice:
                print("Take your juice")
            elif c > juice:
                print("Take your change with juice", c - juice)
            elif c < juice:
                print("Add more money", juice - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'A02':
            print('you have chosen pepsi')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            pepsi = 4 * b
            if c == pepsi:
                print("Take your pepsi")
            elif c > pepsi:
                print("Take your change with pepsi", c - pepsi)
            elif c < pepsi:
                print("Add more money", pepsi - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'A03':
            print('you have chosen prime')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            prime = 30 * b
            if c == prime:
                print("Take your prime")
            elif c > prime:
                print("Take your change with prime", c - prime)
            elif c < prime:
                print("Add more money", prime - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'A04':
            print('you have chosen red bull')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            red_bull = 10 * b
            if c == red_bull:
                print("Take your red bull")
            elif c > red_bull:
                print("Take your change with red bull", c - red_bull)
            elif c < red_bull:
                print("Add more money", red_bull - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'A05':
            print('you have chosen water')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            water = 1 * b
            if c == water:
                print("Take your water")
            elif c > water:
                print("Take your change with water", c - water)
            elif c < water:
                print("Add more money", water - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'B01':
            print('you have chosen cheetos')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            cheetos = 10 * b
            if c == cheetos:
                print("Take your cheetos")
            elif c > cheetos:
                print("Take your change with cheetos", c - cheetos)
            elif c < cheetos:
                print("Add more money", cheetos - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'B02':
            print('you have chosen oreo')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            oreo = 3 * b
            if c == oreo:
                print("Take your oreo")
            elif c > oreo:
                print("Take your change with oreo", c - oreo)
            elif c < oreo:
                print("Add more money", oreo - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'B03':
            print('you have chosen lays')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            lays = 2 * b
            if c == lays:
                print("Take your lays")
            elif c > lays:
                print("Take your change with lays", c - lays)
            elif c < lays:
                print("Add more money", lays - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'B04':
            print('you have chosen takis')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            takis = 14 * b
            if c == takis:
                print("Take your takis")
            elif c > takis:
                print("Take your change with takis", c - takis)
            elif c < takis:
                print("Add more money", takis - c)
                float(input("pay the rest of the amount):\n"))

        elif a == 'B05':
            print('you have chosen snickers')
            b = float(input("How many? (please add after seeing stock in table):\n"))
            c = float(input("pay the amount:\n"))
            snickers = 3 * b
            if c == snickers:
                print("Take your snickers")
            elif c > snickers:
                print("Take your change with snickers", c - snickers)
            elif c < snickers:
                print("Add more money", snickers - c)
                float(input("pay the rest of the amount):\n"))

