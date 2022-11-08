import bruter, etc, networking
from parsing import args, helpme
from threading import Thread

def Klyda():
    if args.help:# if -h
        exit(print(helpme()))
    print(etc.banner)

    usernames, passwords, threads, formdata = [],[],[],{}
    if not args.url:
        exit("(ABORT) No target URL has been specified? Use -h for Klyda usage.\n")
    if not args.username and not args.usernamefile:
        exit("(ABORT) No usernames have been specified? Use -h for Klyda usage.\n")
    if not args.password and not args.passwordfile:
        exit("(ABORT) No passwords have been specified? Use -h for Klyda usage.\n")
    if not args.formdata:
        exit("(ABORT) No formdata has been specified? Use -h for Klyda usage.\n")
  
    for i in args.formdata:
        key, value = i.split(":");formdata[key] = value

    if args.username:
        for i in args.username:
            usernames.append(i)
    if args.usernamefile:
        for i in args.usernamefile:
            try:
                with open(i,"r", encoding = "ISO-8859-1") as f:
                    for a in f.readlines():
                        usernames.append(a.replace("\n",""))
            except:
                exit("(ABORT) Klyda couldn't locate file, " + i)
    if args.password:
        for i in args.password:
            passwords.append(i)
    if args.passwordfile:
        for i in args.passwordfile:
            try:
                with open(i,"r", encoding = "ISO-8859-1") as f:
                    for a in f.readlines():
                        passwords.append(a.replace("\n",""))
            except:
                exit("(ABORT) Klyda couldn't locate file, " + i)

    usernames, passwords, biggerlist = bruter.splitlist(usernames,passwords)
    if networking.validate() == False:
       exit("(ABORT) Couldn't reach the target URL? It may of gone offline...\n")

    print(f"+-[{etc.current()}:REQUEST LOG]".ljust(args.border,"-") + "+" + "\n" + "|".ljust(args.border," ") + "|")
    if biggerlist == True:
        try:
            for i in usernames:
                t = Thread(target=bruter.attacker, args=(i,passwords,formdata,))
                threads.append(t)
                t.start()
                for t in threads:
                    t.join()
        except KeyboardInterrupt:
            etc.summary()
    else:
        try:
            for i in passwords:
                t = Thread(target=bruter.attacker, args=(usernames,i,formdata,))
                threads.append(t)
                t.start()
                for t in threads:
                    t.join()
        except KeyboardInterrupt:
            etc.summary()
    etc.summary()