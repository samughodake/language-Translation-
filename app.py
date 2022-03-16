from tkinter import *
from tkinter import messagebox  
from tkinter import ttk
import requests
from tkinter import ttk

#reading api key from the text file
f = open("api.txt", "r")
api_key = f.read() 

#dictionary to store the language and its code
langs = {
    "af": "Afrikaans",
    "sq": "Albanian",
    "am": "Amharic",
    "ar":   "Arabic",
    "hy": "Armenian",
    "as": "Assamese",
    "az": "Azerbaijani",
    "bn": "Bangla",
    "ba": "Bashkir",
    "bs": "Bosnian (Latin)",
    "bg": "Bulgarian",
    "yue": "Cantonese (Traditional)",
    "ca": "Catalan",
    "lzh": "Chinese (Literary)",
    "zh-Hans": "Chinese Simplified",
    "zh-Hant": "Chinese Traditional",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "prs": "Dari",
    "dv": "Divehi",
    "nl": "Dutch",
    "en": "English",
    "et": "Estonian",
    "fj": "Fijian",
    "fil": "Filipino",
    "fi": "Finnish",
    "fr": "French",
    "fr-ca": "French (Canada)",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "ht": "Haitian Creole",
    "he": "Hebrew",
    "hi": "Hindi",
    "mww": "Hmong Daw",
    "hu": "Hungarian",
    "is": "Icelandic",
    "id": "Indonesian",
    "ikt": "🆕  Inuinnaqtun",
    "iu": "Inuktitut",
    "iu-Latn": "🆕  Inuktitut (Latin)",
    "ga":    "Irish",
    "it":    "Italian",
    "ja":    "Japanese",
    "kn":    "Kannada",
    "kk":    "Kazakh",
    "km":    "Khmer",
    "tlh-Latn": "Klingon",
    "tlh-Piqd": "Klingon (plqaD)",
    "ko": "Korean",
    "ku": "Kurdish (Central)",
    "kmr": "Kurdish (Northern)",
    "ky": "Kyrgyz",
    "lo": "Lao",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "mi": "Maori",
    "mr": "Marathi",
    "mn-Cyrl": "Mongolian (Cyrillic)",
    "mn-Mong": "Mongolian (Traditional)",
    "my": "Myanmar",
    "ne": "Nepali",
    "nb": "Norwegian",
    "or": "Odia",
    "ps": "Pashto",
    "fa": "Persian",
    "pl": "Polish",
    "pt": "Portuguese (Brazil)",
    "pt-pt": "Portuguese (Portugal)",
    "pa": "Punjabi",
    "otq": "Queretaro Otomi",
    "ro": "Romanian",
    "ru": "Russian",
    "sm": "Samoan",
    "sr-Cyrl": "Serbian (Cyrillic)",
    "sr-Latn": "Serbian (Latin)",
    "sk": "Slovak",
    "sl": "Slovenian",
    "es": "Spanish",
    "sw": "Swahili",
    "sv": "Swedish",
    "ty": "Tahitian",
    "ta": "Tamil",
    "tt": "Tatar",
    "te": "Telugu",
    "th": "Thai",
    "bo": "Tibetan",
    "ti": "Tigrinya",
    "to": "Tongan",
    "tr": "Turkish",
    "tk": "Turkmen",
    "uk": "Ukrainian",
    "hsb": "🆕  Upper Sorbian",
    "ur": "Urdu",
    "ug": "Uyghur",
    "uz": "Uzbek (Latin",
    "vi": "Vietnamese",
    "cy":   "Welsh",
    "yua":  "Yucatec Maya",
}

#list of all supported languages to show in the dropdown
list = [
    "Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Assamese",
    "Azerbaijani",
    "Bangla",
    "Bashkir",
    "Bosnian (Latin)",
    "Bulgarian",
    "Cantonese (Traditional)",
    "Catalan",
    "Chinese (Literary)",
    "Chinese Simplified",
    "Chinese Traditional",
    "Croatian",
    "Czech",
    "Danish",
    "Dari",
    "Divehi",
    "Dutch",
    "English",
    "Estonian",
    "Fijian",
    "Filipino",
    "Finnish",
    "French",
    "French(Canada)",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Haitian Creole",
    "Hebrew",
    "Hindi",
    "Hmong Daw",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "Inuinnaqtun",
    "Inuktitut",
    "Inuktitut(Latin)",
    "Irish",
    "Italian",
    "Japanese",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Klingon",
    "Klingon(plqaD)",
    "Korean",
    "Kurdish (Central)",
    "Kurdish (Northern)",
    "Kyrgyz",
    "Lao",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Maori",
    "Marathi",
    "Mongolian (Cyrillic)",
    "Mongolian (Traditional)",
    "Myanmar",
    "Nepali",
    "Norwegian",
    "Odia",
    "Pashto",
    "Persian",
    "Polish",
    "Portuguese (Brazil)",
    "Portuguese(Portugal)",
    "Punjabi",
    "Queretaro Otomi",
    "Romanian",
    "Russian",
    "Samoan",
    "Serbian (Cyrillic)",
    "Serbian (Latin)",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swahili",
    "Swedish",
    "Tahitian",
    "Tamil",
    "Tatar",
    "Telugu",
    "Thai",
    "Tibetan",
    "Tigrinya",
    "Tongan",
    "Turkish",
    "Turkmen",
    "Ukrainian",
    "Upper Sorbian",
    "Urdu",
    "Uyghur",
    "Uzbek (Latin",
    "Vietnamese",
    "Welsh",
    "Yucatec Maya",
]


#function to detect the language
def detect_lang():

    def check():
       
        url = "https://microsoft-translator-text.p.rapidapi.com/Detect"
        querystring = {"api-version":"3.0"} 

        #storing the input in a string to detect its language    
        inp_str=input_text.get("1.0",END)
        inp_str = inp_str.strip("\n")

        #if the input is empty, showing the error mwssage
        if not inp_str:
            top = Tk()  
            top.geometry("100x100")  
            messagebox.showerror("Error","Text Field is empty")  
            top.mainloop() 

        #else detecting the language
        else:

            payload = "[\r\n    {\r\n        \"Text\": \""+ inp_str+".\"   }\r\n]"
            #encoding the entire payload to support the characters of all languages
            payload = payload.encode()
            headers = {
                'content-type': "application/json",
                'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
                'x-rapidapi-key': api_key
                }
            
            #making a request to the API
            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            d = response.json()[0]['language']

            #api returns the code of the detected languages, checking the language from its code from the dictionary 
            dl=langs.get(f"{d}")

            #showing the detected language
            dl = "Language detected: "+ dl
            d_lang.configure(text=dl)
    

    #detect language window
    t1 = Tk()
    t1.title("Detect Language")
    t1.geometry("550x410") 
    l1 = Label(t1, text="Detect Language", justify=CENTER)
    l1.configure(font=("Courier", 16, "normal"))
    l1.pack() 
    top.title("Detect Language") 
    l2 =Label(t1,text="Enter text in any language to detect")
    l2.configure(font=("Courier", 14, "normal"))
    l2.pack()  
    input_text = Text(t1, height=6, width=35, font=("Courier", 14, "normal"))
    input_text.pack()
    btn = Button(t1, text="Check", command=check)
    btn.configure(font=("Courier", 13, "normal"), bg="#BFD4D8")
    btn.pack()
    d_lang = Label(t1)
    d_lang.configure(font=("Courier", 14, "normal"))
    d_lang.pack()
    t1.mainloop()

#function to translate the text from one language to other
def translate_text():

    #function to make the drop down menu of languages searchable
    def check_input(event):
        value = event.widget.get()

        if value == '':
            combo_box['values'] = list
        else:
            data = []
            for item in list:
                if value.lower() in item.lower():
                    data.append(item)

            combo_box['values'] = data

    def trans_text():

        #getting the original text
        inp=input_t.get("1.0",END)

        #removing empty lines from the text
        inp = inp.strip("\n")

        #getting the language in which we want to translate
        selected_lang = combo_box.get()
        global lang_key
        
        for key, value in langs.items():
            if(value == selected_lang):
                lang_key = key #getting the language code

        #showing the error if the input field is empty       
        if not inp:
            top = Tk()  
            top.geometry("100x100")  
            messagebox.showerror("Error","Text Field is empty")  
            top.mainloop()

        else:

            url = "https://microsoft-translator-text.p.rapidapi.com/translate"
            
            #appending the language code in which we want to translate the text to the querystring
            querystring = {f"to":{lang_key},"api-version":"3.0","profanityAction":"NoAction","textType":"plain"}

            payload = "[\r{\r \"Text\": \""+ inp+"\"\r }\r]"
            payload = payload.encode()
            headers = {
            'content-type': "application/json",
            'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
            'x-rapidapi-key': api_key
            }

            #making an API request
            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

            translated_text = response.json()[0]['translations'][0]['text']
            
            #showing the translated text
            output_t.insert(END," ")
            output_t.insert(END, translated_text)
            
    #GUI for translating text
    t = Tk()
    t.title("Translate Text")
    t.geometry("700x490")

    lb1 = Label(t, text="Enter the original text: ", justify=CENTER)
    lb1.configure(font=("Courier", 14, "normal"))
    lb1.pack()

    input_t = Text(t, height=7, width=48, font=("Courier", 14, "normal"))
    input_t.pack()

    lb = Label(t, text="Select the language to which you want to translate: ", justify=CENTER)
    lb.configure(font=("Courier", 14, "normal"))
    lb.pack()

    # creating Combobox
    combo_box = ttk.Combobox(t, font=("Courier", 12, "normal"))
    combo_box['values'] = list
    combo_box.current(22)
    combo_box.bind('<KeyRelease>', check_input)
    combo_box.pack()

    btn = Button(t, text="Translate", command=trans_text)
    btn.configure(font=("Courier", 13, "normal"), bg="#BFD4D8")
    btn.pack()
    
    lb2 = Label(t, text="Translated Text:  ", justify=CENTER)
    lb2.configure(font=("Courier", 14, "normal"))
    lb2.pack()

    output_t = Text(t, height=7, width=48, font=("Courier", 14, "normal"))
    output_t.pack()

    t.mainloop()

#creating the application main window.   
top = Tk() 
top.title("Translate App")
top.geometry("500x350") 
l1 = Label(top, text="Translate App", justify=CENTER)
l1.configure(font=("Courier", 16, "bold"), foreground="#92755C")
l1.grid(row=0, column=0)
top.title("Translate App") 

l2 = Label(top, text="Detect the language: ", )
l2.configure(font=("Courier", 14, "normal"))
l2.grid(row=1, column=0)

bt = Button(top, text="Click here", padx=2, pady=2, command=detect_lang)
bt.grid(row=1, column=1)
bt.configure(font=("Courier", 13, "normal"), bg="#BFD4D8")

l3 = Label(top, text="Translate Text in any language: ")
l3.configure(font=("Courier", 14, "normal"))
l3.grid(row=2, column=0)

bt2 = Button(top, text="Click here", padx=2, pady=2 , command=translate_text)
bt2.grid(row=2, column=1)
bt2.configure(font=("Courier", 13, "normal"), bg="#BFD4D8")

top.mainloop()  