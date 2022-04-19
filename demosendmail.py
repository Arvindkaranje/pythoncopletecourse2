# sending mail using pyton
import smtplib
server =smtplib.SMTP('smptp.gmail.com',587)
server.starttls()

server.login('arvindkicchakaranje@gmail.com',24121999)

server.sendmail('arvindkicchakaranje@gmail.com','bidarmona@gmail.com','hiii, msg from python')
print("message sent already check your mail")

