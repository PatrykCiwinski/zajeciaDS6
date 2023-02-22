colors = {"blue":"niebieski",
          "green":"zielony",
          "black":"czarny",
          "yellow":"zolty",
          "brown":"brazowy",
          "red":"czerwony",
          "white":"bialy",
          "purple":"fioletowy"}

while True:
    what_lang = input("jakie tłumaczenie (ang-pl - 1, pl-ang - 2) ")
    if what_lang != "1" and what_lang!="2":
        continue
    if what_lang == '2':
        what_color=input("jaki kolor przetłumaczyć ").lower().strip()
        tłumaczenie=[k for k, v in colors.items() if v==what_color][0]
        print(tłumaczenie)
    elif what_lang == '1':
        what_color = input("what color do you want to translate ").lower().strip()
        translate = colors[what_color]
        print(translate)
    next = input("czy kontynuować (t/n) ")
    if next =="n":
        break