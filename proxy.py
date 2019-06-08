#!/usr/bin/python
#coding: utf-8


from requests import get, post, head
from threading import Thread
import os
import time



btw = '''

\n>>> DORK PROXY CHECKER.
>>> [DEV] : Dork Web(Eric Pedra)                                    <<<
>>> [Facebook] : https://www.facebook.com/Ahmad.AI.Ghazali			     <<<
>>> [Version] : 1.3.V  
>>> [MULTITHREAD] FASTER
>>> SCRIPT PROGRAMMED BY ERIC PEDRA DENGAN PYTHON2.
'''
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
print btw
print ''

def main():
    def tryproxies(proxy):
        with open('VALID PROXIES.txt', 'a+') as validproxiesfile:
            try:
                rs = head('https://www.google.com/', proxies={'https': proxy}, timeout=20)
                print(rs.status_code, '\n httpproxy', proxy, "Waktu berlalu: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('http/https://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Waktu berlalu: %s" % (time.time() - start))
            try:
                rs = head('https://www.google.com/', proxies={'https': 'socks5://' + proxy}, timeout=20)
                print(rs.status_code, '\n socks5proxy', proxy, "Waktu berlalu: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('socks5://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Waktu berlalu: %s" % (time.time() - start))
            try:
                rs = head('https://www.google.com/', proxies={'https': 'socks4://' + proxy}, timeout=20)
                print(rs.status_code, '\n socks4proxy', proxy, "Waktu berlalu: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('socks4://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Waktu berlalu: %s" % (time.time() - start))

    start = time.time()
    threadlist = []

    try:
        os.remove('VALID PROXIES.txt')
    except Exception:
        pass

    with open(raw_input('[!] ENTER YOUR PROXIES PATH: '), 'r') as file:
        for proxy in file:
            proxy = proxy.strip()
            t = Thread(target=tryproxies, args=(proxy,))
            t.start()
            threadlist.append(t)

# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

if __name__ == '__main__':
    main()