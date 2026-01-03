import requests
from datetime import datetime
import smtplib

MY_LAT=-4.1101 #your latitude
MY_LNG=117.9552 #your longitude

my_email='app@gmail.com'
password="password"

def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    data=response.json()
    iss_lattitude=float(data["iss_position"]['latitude'])
    iss_longitude=float(data["iss_position"]['longitude'])
    if abs(iss_lattitude-MY_LAT)<=5 and abs(iss_longitude-MY_LNG)<=5:
        return True
    return False


def is_night():

    parameters={
        "lat":MY_LAT,
        "lng":MY_LNG,
        'formatted':0
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    print(data)
    sunrise=int(data["results"]['sunrise'].split("T")[1].split(":")[0])
    sunset=int(data["results"]['sunset'].split("T")[1].split(":")[0])
    curr_hour=datetime.now().hour

    if curr_hour>=sunset and curr_hour<=sunrise:
        return True
    return False

if is_near() and is_night():

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="apptesting@gmail.com",msg="Subject:ISS OVERHEAD\n\nGo outside and look above")
