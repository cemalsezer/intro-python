"""
Tek indextekiler Büyük 
Cift indextekiler küçük olacak

"""

# döngü ile metnin olduğu dizine girip tek indexlileri
# upper fonksiyonu ile büyüt


# defaulText = "hi my name is john and i am learning python"


# def cvrtText(textParam):
#     afterText = ""
#     for indexText in range(len(textParam)):
#         if indexText % 2 == 0:
#             afterText += textParam[indexText].upper()
#         else:
#             afterText += textParam[indexText].lower()
#     print(afterText)


# cvrtText(defaulText)


# defaulText=input("Write your text: ")

# def cvrtText(textParam):
#     afterText = ""
#     for indexText in range(len(textParam)):
#         if indexText % 2 == 0:
#             afterText += textParam[indexText].upper()
#         else:
#             afterText += textParam[indexText].lower()
#     print(afterText)


# cvrtText(defaulText)


defaulText=input("Write your text: ")

def cvrtText(textParam):
    afterText = ""
    for indexText,textOrgi in enumerate(textParam):
        if indexText % 2 == 0:
            afterText += textOrgi.upper()
        else:
            afterText += textOrgi.lower()
    print(afterText)


cvrtText(defaulText)