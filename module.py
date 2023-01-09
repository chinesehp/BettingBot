from email.message import EmailMessage
import ssl
import smtplib

def moneyline_to_frac(odd):
    if(odd[0]=='−'):
        odd=-1*float(odd[1:])
    else: odd = float(odd)

    if(abs(odd)<100):
        return odd
    if (odd < 0):
        return (100 / abs(odd)) + 1
    return (odd / 100) + 1

def compare_matches(match_a,match_b):
    #get the better of the bets and return match_a
    if(match_a.fighter_a.last_name == match_b.fighter_a.last_name):
        if(match_a.odds_a<match_b.odds_a):
            match_a.odds_a=match_b.odds_a
            match_a.bookie_a=match_b.bookie_a
        if(match_a.odds_b<match_b.odds_b):
            match_a.odds_b=match_b.odds_b
            match_a.bookie_b=match_b.bookie_b
    if(match_a.fighter_a.last_name == match_b.fighter_b.last_name):
        if (match_a.odds_a < match_b.odds_b):
            match_a.odds_a = match_b.odds_b
            match_a.bookie_a = match_b.bookie_b
        if (match_a.odds_b < match_b.odds_a):
            match_a.odds_b = match_b.odds_a
            match_a.bookie_b = match_b.bookie_a
    match_a.calc_arb()
    return match_a



def is_in(match_a,match_b):
    if (match_a.fighter_a.last_name == match_b.fighter_a.last_name and match_a.fighter_b.last_name == match_b.fighter_b.last_name ):
        return True
    elif (match_a.fighter_a.last_name == match_b.fighter_b.last_name and match_a.fighter_b.last_name==match_b.fighter_a.last_name):
        return True
    return False


def send_mail(body ='lol'):
    email_sender ='waltuhbai@gmail.com'
    email_password ='yagjqhhntaohnpdq'
    email_receiver = 'stevenmag14@hotmail.com'
    subject ='ARB OPPORTUINITY FOUND'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context =context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
