import optparse
from selenium import webdriver
import threading

def check_xss(url):
    driver = webdriver.Chrome()
    with open("xsspayload.txt",encoding="utf-8") as file:
        payloads = file.readlines()
        for payload in payloads:
            payload = payload.strip()
            try:
                driver.get(url + payload)
                message = driver.switch_to.alert.text
                if message is not None:
                    print("[+]url:"+url+",payload is:" + payload)
            except:
                pass
def main():
    print('''                                                                                        
 \@@`  ,@@/  ]@@@@@   ]@@@@@         ,/@@@@^                                                  
  \@@`,@@^  @@/` ,\  @@/` ,\        =@@[  [^                                                  
   \@@@@`   @@@\`    @@@\`          =@@@]    ,@@@@@^ =@@@@@\  @@@@@@@\ =@@@@@@@` /@@@@@^ =@@@@
   =@@@@*    *[@@@@*  *[@@@@* ]]]]`   ,\@@@^ @@/      ,]/@@@  @@^  =@@ =@@   @@^=@@]]]@@ =@@` 
  /@@`\@@`  `   *@@^ `   *@@^ [[[[` ,    =@@ @@@     @@[  @@  @@^  =@@ =@@   @@^=@@`     =@@  
 @@@`  =@@^ @@@@@@/  @@@@@@/        =@@@@@@`  \@@@@^ \@@@/@@  @@^  =@@ =@@   @@^ ,@@@@@^ =@@           
                                                                                Auther:ghtwf01
                                                                                have fun~                                                                                  
    ''')
    global num
    num = 0
    threads = []
    parser = optparse.OptionParser("-u <target host> -m <method> -u <target url>")
    try:
        parser.add_option('--u1', dest='url1', type='string', help='目标网址')
    except:
        pass
    try:
        parser.add_option('--u2', dest='url2', type='string', help='目标网址')
    except:
        pass
    try:
        parser.add_option('--u3', dest='url3', type='string', help='目标网址')
    except:
        pass
    (options, args) = parser.parse_args()
    try:
        url1 = options.url1
        if url1 is not None:
            num+=1
    except:
        pass
    try:
        url2 = options.url2
        if url2 is not None:
            num += 1
    except:
        pass
    try:
        url3 = options.url3
        if url3 is not None:
            num += 1
    except:
        pass
    try:
        url4 = options.url4
        if url4 is not None:
            num += 1
    except:
        pass
    try:
        url5 = options.url5
        if url5 is not None:
            num += 1
    except:
        pass
    print("[+]"+str(num)+" targets detected,running......")
    if num == 1:
        check_xss(url1)
    if num == 2:
        t1 = threading.Thread(target=check_xss,args=((url1),))
        threads.append(t1)
        t2 = threading.Thread(target=check_xss, args=((url2),))
        threads.append(t2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    if num == 3:
        t1 = threading.Thread(target=check_xss,args=((url1),))
        threads.append(t1)
        t2 = threading.Thread(target=check_xss, args=((url2),))
        threads.append(t2)
        t3 = threading.Thread(target=check_xss, args=((url3),))
        threads.append(t3)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
if __name__ == "__main__":
    main()
    
