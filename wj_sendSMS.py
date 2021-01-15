import urllib.parse
import http.client
import json

def main():
    host = "106.ihuyi.com"
    sms_uri = "/webservice/sms.php?method=Submit"
    params = urllib.parse.urlencode({'account': 'C65108052', 'password': '28c6031229a54e415b4ac1b51b9a6534', 'content': '您的验证码是：1234。请不要把验证码泄露给其他人。', 'mobile': '18974978372', 'format': 'json'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept' : 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonStr = response_str.decode('utf-8')
    print(json.loads(jsonStr))
    conn.close()

if __name__ == '__main__':
    main()