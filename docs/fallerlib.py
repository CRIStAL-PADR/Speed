 IP_master= "172.17.217.217"
 IP_slave= "172.17.217.60"

def startM(IP,sNr,turn):

     if sNr = 1 and turn = 1:
         if IP==IP_master:
             r= requests.get("http:"+IP_master+"startM?sNr=1&turn=1")
         else:
             r= requests.get("http:"+IP_slave+"startM?sNr=1&turn=1")
        
    elif sNr = 1 and turn = -1:
        if IP==IP_master:
             r= requests.get("http:"+IP_master+"startM?sNr=1&turn=-1")
        else:
             r= requests.get("http:"+IP_slave+"startM?sNr=1&turn=-1")

    elif sNr = 2 and turn = 1
         r= requests.get("http:"+IP_slave+"startM?sNr=2&turn=1")
    elif sNr = 2 and turn = -1:
        r= requests.get("http:"+IP_slave+"startM?sNr=2&turn=-1")
    else:
         print("Error!!!")

    r.status_code
    print(r.status_code)

    if r!200:
        throw expression("....")


def stop(IP,sNr):
    if sNr = 1:
        if IP==IP_master:
             r= requests.get("http:"+IP_master+"stopM?sNr=1")
        else:
             r= requests.get("http:"+IP_slave+"stop?sNr=1")
    elif sNr = 2:
        r= requests.get("http:"+IP+"stopM?sNr=2")
    else:
         print("Error")

    r.status_code
    print(r.status_code)

    if r!200: 
        throw expression("....")

def changePWM(IP,sNr, diff):

     if sNr = 1 and diff = 5:
         if IP==IP_master:
             r= requests.get("http:"+IP_master+"changePWMTV?sNr=1&diff=5")
         else:
             r= requests.get("http:"+IP_slave+"changePWMTV?sNr=1&diff=5")
    elif sNr=1 and diff = -5:
        if IP==IP_master:
             r= requests.get("http:"+IP_master+"changePWMTV?sNr=1&diff=-5")
        elif sNr=1 and diff = -5:
            r= request.get("http:"+IP_slave+"changePWMTV?sNr=1&diff-=5")

    elif sNr = 2 and diff = 5:
        r= requests.get("http:"+IP_slave+"changePWMTV?sNr=2&diff=5")
    elif sNr=2 and diff = -5:
        r= requests.get("http:"+IP_slave+"changePWMTV?sNr=2&diff=-5")
    else:
        print("Error")

   r.status_code
   print(r.status_code)
   
   if r!200:
        throw expression("...")

def getBat(n):
    if n=1:
        r=requests.get("http:"+IP_master+"getBat?n=1")
    elif n=2:
        r=requests.get("http:"+IP_slave+"getBat?n=2")
    else:
        print("Error")


def init(IP):
    IP_master= IP
    IP_slave = getOtherEsp(IP)

def getOtherEsp(X):
    r = requests.get("http:"+"getOtherEsp(IP_slave)")
    if (V):
       print( r.status_code)
    else:
        raise Exception ("....")


