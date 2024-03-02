import pywhatkit
try:

    pywhatkit.sendwhatmsg("+52numero", "hello word", 8, 22)
    pywhatkit.sendwhatmsg_instantly("+52444444444", "hello word")


    print("mensaje enviado")
except:
    print("error")
