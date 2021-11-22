# import smtplib
# from email.mime.text import MIMEText

# Test the sending of email


# Variables in send_email are dependent on the type of email used
# Server used for this project is mailtrap




# Uncomment below

# def send_email(first_name, last_name, score, adjective):
#     port = 
#     smtp_server = 'smtp.mailtrap.io'
#     login = 
#     password = 
#     message = f"<h3>New info_storage Submission</h3>
#     <ul><li>First Name: {first_name} </li>
#     <li>First Name: {last_name} </li>
#     <li>First Name: {score} </li>
#     <li>First Name: {adjective} </li>
#     </ul>
#     "

#     sender_email = 'billy@test.com'
#     receiver_email = 'todd@test.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'mlh-app info_storage'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email


#     # Sending email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())