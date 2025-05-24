import os
import re
import sys
import json
import base64
import requests
from datetime import datetime

dumpdata = []
class Login:

    def __init__(self):
        self.headers = {
            'x-bloks-version-id': 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd',
            'x-ig-www-claim': '0',
            'x-debug-www-claim-source': 'handleLogin3',
            'x-bloks-prism-button-version': 'CONTROL',
            'x-ig-capabilities': '3brTv10=',
            'x-ig-app-id': '567067343352427',
            'priority': 'u=3',
            'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
            'accept-language': 'id-ID, en-US',
        }

    def idbear(self, cokie):
        try:
            self.id = re.search(r'ds_user_id=(\d+);',str(cokie)).group(1)
            self.sn = re.search(r'sessionid=(.*?);',str(cokie)).group(1)
            self.br = base64.b64encode(json.dumps({'ds_user_id': self.id, 'sessionid': self.sn}).encode()).decode()
            return self.id, self.br
        except AttributeError:
            exit('\nInvalid cokie')

    def Session(self, cokie):
        try:
            self.uid,self.bearer = self.idbear(cokie)
            self.headers.update({
                    'authorization': f'Bearer IGT:2:{self.bearer}',
            })
            self.respon = requests.get(f'https://i.instagram.com/api/v1/users/{self.uid}/info/',headers=self.headers).json()['user']['full_name']
            return self.respon
        except:
            return False

    def Cookie(self):
        os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
        cok = input('Login with cookie > ')
        ses = self.Session(cok)
        while(ses == False):
            cok = input('Login with cookie > ')
            ses = self.Session(cok)
            if ses:break
        open('.tumbal','w').write(cok)
        self.menu()
    
    def Files(self):
        now = datetime.now()
        file = f'/sdcard/dump_uid-{now.day}-{now.month}-{now.year}.txt'
        return file

    def menu(self):
        if os.path.isfile('.tumbal') is False:self.Cookie()
        ses = self.Session(open('.tumbal','r').read())
        if ses == False:self.Cookie()
        os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
        print('Login as',ses)
        uidList = []
        users = input('Masukan username pisahan dengan koma > ').split(',')
        for self.xyz in users:
            self.uuid = convert().usernametoid(self.xyz)
            if self.uuid:uidList.append(self.uuid)
        if len(uidList) == 0:
            exit('\nCoba ganti username')
        dumps_type = input('\n1) Dump followers\n2) Dump following\n> ')
        print('\n')
        for self.ah in uidList:
            if dumps_type == '1':
                dump().followers(self.ah,'',self.Files())
            else:
                dump().following(self.ah,'',self.Files())
        exit('\nDone')
        
class convert:
    def __init__(self):
        self.cokie = open('.tumbal','r').read()

    def usernametoid(self, username):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'viewport-width': '673'
                })
                self.req = self.r.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}").json()['data']['user']['id']
                return self.req
            except:return None


class dump:
    def __init__(self):
        self.cokie = open('.tumbal','r').read()

    def followers(self,userid,next_pae,files_):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'viewport-width': '673'
                })
                self.data = {"query_hash": "c76146de99bb02f6415203be841dd25a","variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                self.req = self.r.get('https://www.instagram.com/graphql/query/',params=self.data).json()
                for self.users in self.req['data']['user']['edge_followed_by']['edges']:
                    self.udata = self.users['node']['id']
                    if self.udata not in dumpdata:
                        dumpdata.append(self.udata)
                        open(files_,'a').write(f'{self.udata}\n')
                    print(f' Success dump {len(dumpdata)}',end='\r'),sys.stdout.flush()
                if(self.req['data']['user']['edge_followed_by']['page_info']['has_next_page']==True):
                    self.followers(userid, self.req['data']['user']['edge_followed_by']['page_info']['end_cursor'],files_)
                else: return
            except:return
    
    def following(self,userid,next_pae,files_):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'viewport-width': '673'
                })
                self.data = {"query_hash": "d04b0a864b4b54837c0d870b0e77e076","variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                self.req = self.r.get('https://www.instagram.com/graphql/query/',params=self.data).json()
                for self.users in self.req['data']['user']['edge_follow']['edges']:
                    self.udata = self.users['node']['id']
                    if self.udata not in dumpdata:
                        dumpdata.append(self.udata)
                        open(files_,'a').write(f'{self.udata}\n')
                    print(f' Success dump {len(dumpdata)}',end='\r'),sys.stdout.flush()
                if(self.req['data']['user']['edge_follow']['page_info']['has_next_page']==True):
                    self.following(userid, self.req['data']['user']['edge_follow']['page_info']['end_cursor'],files_)
            except:return
    
Login().menu()

