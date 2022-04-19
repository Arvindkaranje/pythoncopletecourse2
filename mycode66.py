# 83
# exercise
# akbar padke sunao
# fetch the news from news api.org
# create ur own account fetch top news from their into python
# install pywin32
# create speak function to speak the  news headings
# this speak function should speak the top 10 newses from the news api website
# use json module where prase all the string values from the website and fetch the news
.1

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__=="__main__":
    speak("Arvind karanje is here he will finish everything")