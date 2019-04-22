receiver = "sukrishn@ucsd.edu"
body = "Hello there from Yagmail YEEEEET"
filename = "./Reports/report.pdf"

class Alert:

    sender_email = "habtest3@gmail.com"

    def send_email(self,receivers = None, subject_txt = None, msg = None, file_path = None):

        import yagmail
        yag = yagmail.SMTP(Alert.sender_email)
        yag.send(
            to=receivers,
            subject=subject_txt,
            contents=msg,
            attachments=file_path 
        )

sup = Alert()
sup.send_email(receiver, "YEETERSONS", body, filename)




