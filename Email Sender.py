import smtplib

def send_email(subject, message, from_addr, to_addr, password):
    server = smtplib.SMTP("(link unavailable), 587")
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, f"Subject: {subject}\n\n{message}")
    server.quit()
    
subject = "Test Email"
message = "This is the test email sent using Python"
from_addr = "adebayoabdulmalik12@gmail.com"
to_addr = "harbdulmarleyk@gmail.com"
password = "Malik@2003" 

send_email(subject, message, from_addr, to_addr, password) 

 
    