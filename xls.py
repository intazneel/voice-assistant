import pyttsx3
import datetime
import pythoncom
import speech_recognition as sr
import playsound
import xlrd
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak('good morning!')
	elif hour>=12 and hour<18:
		speak('good afternoon!')

	else:
		speak('good evening!')

	speak('welcome to rebel foods kitchen. PLease tell me how may i help you')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('gmailaccountname','password')
	server.sendmail('gmailaccountname', to, content)
	server.close()




loc = (r"C:\Users\Shaikh_Boyzzz\Desktop\Book1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0) 
tan = (sheet1.cell_value(0, 0))


loc = (r"C:\Users\Shaikh_Boyzzz\Desktop\Book1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0) 
zeel = (sheet1.cell_value(1, 0))


loc = (r"C:\Users\Shaikh_Boyzzz\Desktop\Book1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0) 
ahm = (sheet1.cell_value(2, 0))


loc = (r"C:\Users\Shaikh_Boyzzz\Desktop\Book1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0) 
ed = (sheet1.cell_value(3, 0))


loc = (r"C:\Users\Shaikh_Boyzzz\Desktop\Book1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0) 
code = (sheet1.cell_value(4, 0))

if __name__== "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()

	
		if "noodles" in query:
			speak("yes noodles is available")

		if "tomato" in query:
			speak("yes tomato is available")

		if "chicken" in query:
			speak("yes chicken is available")

		if "sugur" in query:
			speak("yes sugur is available")




		if "rice" in query:
			speak("yes rice is available")


		if "tomato" in query:
			speak(tan)

		if "chicken" in query:
			speak(zeel)

		if "rice" in query:
			speak(ahm)

		if "sugur" in query:
			speak(ed)

		if "noodles" in query:
			speak(code)

		if "send email" in query:
			try:
				speak("what should i say?")
				content = takeCommand()
				to = "receivergmail"
				sendEmail(to, content)
				speak("email has been sent")
			except Exception as e:
				print(e)
				speak("sorry")