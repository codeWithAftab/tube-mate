from cgi import print_environ
import imp
from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup

def get_hall_ticket2022june(enr_no,prog):
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
                "naac.png": "https://ignouhall.ignou.ac.in/HallTickets/Hall0622/naac.png"
    }
    for key in replace_list:
        print(key)
        content= content.replace(key,replace_list[key])


    return content
 