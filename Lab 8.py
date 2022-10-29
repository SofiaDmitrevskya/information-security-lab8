#!/usr/bin/env python
# coding: utf-8

# In[17]:


a = ord("а")
alphabet = [ chr(i) for i in range (a, a+32)]
a = ord("0")
for i in range(a, a+10):
    alphabet.append(chr(i))
a = ord("А")
for i in range(1040, 1072):
    alphabet.append(chr(i))
    
P1="НаВашисходящийот1204"
P2="ВСеверныйфилиалБанка"


# In[18]:


def vzlom(P1, P2):
    code = []
    for i in range(20):
        code.append(alphabet[(alphabet.index(P1[i]) + alphabet.index(P2[i])) %len(alphabet) ])
    print(code)
    p3 = "".join(code)
    print(p3)


# In[19]:


vzlom(P1, P2)


# In[22]:


def shifr(P1):
    dicts = {"а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ё": 7, "ж": 8, "з": 9, "и": 10,
             "й": 11, "к": 12, "л": 13, "м": 14, "н": 15, "о": 16, "п": 17, "р": 18, "с": 19, 
             "т": 20, "у": 21, "ф": 22, "х": 23, "ц": 24, "ч": 25, "ш": 26, "щ": 27, "ъ": 28, 
             "ы": 29, "ь": 30, "э": 31, "ю": 32, "я": 32, "А":33 , "Б": 34, "В": 35 , "Г":36,
             "Д":37 , "Е":38 , "Ё":39 , "Ж":40 , "З":41, "И":42,"Й":43 , "К":44 , "Л":45 , 
             "М":46 , "Н":47 , "О":48 , "П":49 , "Р":50 , "С":51 , "Т":52 , "У":53 , "Ф":54, 
             "Х":55 , "Ц":56 , "Ч":57, "Ш":58,"Щ":59 , "Ъ":60 , "Ы":61 , "Ь":62 , "Э":63 , 
             "Ю":64 , "Я":65 , "1":66 , "2":67 , "3":68 , "4":69 , "5":70 , "6":71 , 
             "7": 72, "8":73 , "9":74 , "0":75
    }
    
    dict2 = {v: k for k, v in dicts.items()}
    text = P1
    gamma = input("Введите гамму")
    digits_gamma = list()
    digits_text = list()
    
    for i in text:
        digits_text.append(dicts[i])
    print("Числа текста ", digits_text)
    
    for i in gamma:
        digits_gamma.append(dicts[i])
    print("Числа гаммы ", digits_gamma)
    
    digits_result = list()
    ch = 0
    for i in text:
        try:
            a = dicts[i] + digits_gamma[ch]
        except:
            ch = 0
            a = dicts[i] + digits_gamma[ch]
        if a > 75:
            a = a%75
            print(a)
        ch=ch+1
        digits_result.append(a)
        
    print("Числа шифровки ", digits_result)
    
    text_crypted = ""
    for i in digits_result:
        text_crypted = text_crypted + dict2[i]
    print("Шифровка ", text_crypted)
    
    digits = list()
    for i in text_crypted:
        digits.append(dicts[i])
    ch = 0
    digits1 = list()
    for i in digits:
        try:
            a = i - digits_gamma[ch]
        except:
            ch=0
            a = i - digits_gamma[ch]
        if a<1:
            a = 75+a
        digits1.append(a)
        ch=ch+1
        
    text_decr = ""
    for i in digits1:
        text_decr = text_decr + dict2[i]
    print("Расшифровка", text_decr)


# In[23]:


shifr(P1)


# In[ ]:




