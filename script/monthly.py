#!/usr/bin/env python3
"""
WorkFlow: md to html, send mail, create new md

NOTE: Must be launched on the new month
"""


def send_email(sender, password, receiver, subject, body):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    html = MIMEText(body, "html")
    message.attach(html)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()


def md_convert(path):
    import pypandoc
    output = pypandoc.convert_file(path, 'html', outputfile="body.html")


def set_date():
    import datetime as dt
    past_month = format(dt.date.today().replace(day=1) - dt.timedelta(days=1),
                        '%B')
    curr_month = format(dt.date.today().replace(day=1), '%B')
    curr_year = format(dt.date.today().replace(day=1), '%Y')
    curr_nmonth = format(dt.date.today().replace(day=1), '%m')
    return ([past_month, curr_month, curr_year, curr_nmonth])


def create_report():
    with open(
            "report/monthly-report-{0}-{1}.md".format(set_date()[2],
                                                      set_date()[3]),
            "w+") as f:
        f.write("Monthly Report")
        f.close()


def main():
    password = "sozqatwpkftkttjf"
    sender_email = "andrea.casadei@yoroi.company"
    receiver_email = "andrea.casadei@yoroi.company"
    subject = "test HTML email with python"
    signature = open('signature.html', 'r').read()
    text = open('body.html', 'r').read()
    report_name = "report/monthly-report-{0}-{1}.md".format(
        set_date()[2],
        set_date()[3])

    body = "Ciao Zoff,<br>" + \
           "<h1>{0}</h1>".format(set_date()[0]) + \
           "<html> <body>" + \
           "{0}".format(text) + \
           "<br> <br> Saluti,<br>" + \
           "{0}".format(signature) + \
           "</body> </html>"

    md_convert(report_name)
    create_report(report_name)
    # send_email(sender_email, password, receiver_email, subject, body)
    print("OK")


if __name__ == "__main__":
    main()
