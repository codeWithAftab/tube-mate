from cgi import print_environ
from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from tubemate import settings

def get_hall_ticket(enr_no,prog):
    url = "https://ignouhall.ignou.ac.in/HallTickets/Hall0622/ignouhallticketjune2022.aspx"
    data = {
        "txtEnrNo":enr_no,
        "ddlProgram":prog,
        "CheckDeclaration":"Y",
    }
    r = requests.post(url=url,data=data,verify=False)
    soup = BeautifulSoup(r.content,"html.parser")
    content = r.text

    replace_list = {"logo.jpg":"https://ignouhall.ignou.ac.in/HallTickets/Hall0622/logo.jpg",
                "!important":"",
                "include/ignou.css":"https://ignouhall.ignou.ac.in/HallTickets/Hall0622/include/ignou.css",
                "naac.png": "https://ignouhall.ignou.ac.in/HallTickets/Hall0622/naac.png",
                "<p class=noprint><font class=cfont><a href=javascript:history.back(-1)>Back</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href=javascript:window.print()>Print</a>": '<p class=noprint><font class=cfont><a class="btn btn-warning" href=javascript:history.back(-1)>Back</a> &nbsp;&nbsp;&nbsp;&nbsp;<a class="btn btn-success" href=javascript:window.print()>Print</a>'
    }
    for key in replace_list:
        print(key)
        content= content.replace(key,replace_list[key])


    return content
# def getImage(enroll,prog):
#     url = "https://ignouhall.ignou.ac.in/HallTickets/Hall0622/ignouhallticketjune2022.aspx"
#     data = {
#         "txtEnrNo":enroll,
#         "ddlProgram":prog,
#         "CheckDeclaration":"Y",
#     }
#     r = requests.post(url=url,data=data,verify=False)
#     soup = BeautifulSoup(r.content,"html.parser")
#     image_list = soup.find_all("img")
#     photo = image_list[-2]
#     print(photo)
#     return photo["src"]
