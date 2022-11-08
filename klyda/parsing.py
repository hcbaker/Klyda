import argparse
def options(): # avaible options/usage for Klyda
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h","--help",action="store_true",help="Display help and usage")
    parser.add_argument("--url",type=str,help="Target url")
    parser.add_argument("-d","--formdata",type=str,nargs="+",help="Formdata to foward requests. format as (key:value)")
    parser.add_argument("-u","--username",type=str,nargs="+",help="Targeted username(s)")
    parser.add_argument("-U","--usernamefile",type=str,nargs="+",help="Targeted file of usernames")
    parser.add_argument("-p","--password",type=str,nargs="+",help="Given password(s)")
    parser.add_argument("-P","--passwordfile",type=str,nargs="+",help="Given list of passwords")
    parser.add_argument("-t","--threads",type=int,default=1,help="Given amount of threads to spawn (deafult 1)")
    parser.add_argument("-b","--border",type=int,default=75,help="Adjust length of border (default 75 characters)")

    parser.add_argument("--bstr",type=str,nargs="+",default=[],help="Blacklist given strings from output")
    parser.add_argument("--bcde",type=int,nargs="+",default=[],help="Blacklist given request codes from output")
    parser.add_argument("--blen",type=int,nargs="+",default=[],help="Blacklist given content lengths from output")

    parser.add_argument("--rate",type=int,nargs=2,default=[100,0],help="Rate of requests per minute, format as (requests minutes)")
    parser.add_argument("-tm","--timeout",type=int,default=4,help="Seconds for request timeout (deafult 4s)")

    return parser.parse_args()

def helpme(name=None): # klyda help prompt
    return """
 █▄        ▄█
 ████████████ Klyda  : version 1.1
 ██  ████  ██ Author : https://github.com/Xeonrx
 ████████████ Source : https://github.com/Xeonrx/Klyda
 ████████████
 ████████████
                Klyda is a Python project designed to simplify
                the use of dictionary/spray attacks on web applications, 
                  
                Klyda is meant for security/testing purposes, and proper
                permission MUST be given before an attack. This script
                doesn't exist for the intention of malicious purpose, and
                no one is repsonsible for any legal precussions but yourself!
                
      > If any malfunctions/bugs are apparent, please submit an issue request here: 
      (https://github.com/Xeonrx/Klyda/issues)
      
      > I encourge anyone to contibute to the Klyda project. Please do so here:
      (https://github.com/Xeonrx/Klyda/pulls)
      
      > Klyda is still a work in progress. Check GitHub for future updates & plans.


      [KLYDA USAGE]:
      -h / --help (Display help prompt for klyda usage)
      
      --url (Targeted URL for Klyda to attack) ex.   --url http://127.0.0.1
      -d / --data (Needed data to send requests through. Format as key:value) ex.   -d username:xuser password:xpass login:login
      -t / --threads (Number of processes used to run the attack, default is 1) ex.   -t 2
      -b / --border (Adjust the border size of Klyda output, default is 77 characters) ex.   -b 45
      -tm / --timeout (Adjust the seconds for a request timeout, default is 4 seconds) ex.   -tm 2

      -u / --username (Username(s) to target in attack, can range from 1 to whatever) ex.   -u admin guest user
      -U / --usernamefile (File of usernames to target in attack, can range from 1 to whatever. Can be combined with -u) ex.   -U users.txt list.txt
      -p / --password (Passwords(s) to use in attack, can range from 1 to whatever) ex.   -p password 1234 letmein
      -P / --passwordfile (File of passwords to use in attack, can range from 1 to whatever. Can be combined with -p) ex.   -P common.txt pass.txt

      --rate (Control each thread by number of requests per given minutes, for quiet purporses) ex.   --rate 10 1 (10 requets per 1 minute)
      --bstr (Block given strings from output, to narrow down results, can range from 1 to whatever) ex.   --bstr "Login failed" "Try again"
      --bcde (Block given request codes from output, to narrow down results, can range from 1 to whatever) ex.   --bcde 404 403
      --blen (Block given request lengths from output, to narrow down results, can range from 1 to whatever) ex.   --blen 6 9

      [KLYDA EXAMPLES]: (examples are based off of the Damn Vulnerable Web App & Mutillidae, which are purpously designed vulnerable servers)
      python3 klyda.py --url http://127.0.0.1/dvwa/login.php -u user guest admin -p 1234 password admin -d username:xuser password:xpass Login:Login --bstr "Login failed"
      python3 klyda.py --url http://127.0.0.1/mutillidae/index.php?page=login.php -u root -P passwords.txt -d username:xuser password:xpass login-php-submit-button:Login --bstr "Authentication Error"
      """

args = options()