<p align="center">
 <img src="https://github.com/Xeonrx/Resprayd/blob/main/img/fronticon.png">
 </p>

The Klyda project has been created to aid in quick credential based attacks against online web applications.<br />
Klyda supports the use from simple password sprays, to large multithreaded dictionary attacks.

Klyda is a new project, and I am looking for any contributions; including wordlists contributions. Any help is very appreciated.
The script works by injecting given credentials into requests, and narrowing down successful results via blacklists of strings, status codes, or content lenghts.

Klyda offers simple, easy to remember usage; however, still offers configurability for your needs:
- Mulithreaded tasks
- Combine wordlists for larger scale attacks
- Blacklisting data to narrow down results
- Limit thread speed for sneaky purposes
- Alter requests, such as useragent, timeout, & headers
- File output

# Installation & Usage
**1)** Clone the Git repo to your machine, `git clone https://github.com/Xeonrx/Klydaa/edit/main/README.md`<br />
**2)** Cd into the Klyda directory, `cd Klyda`<br />
**3)** Install the neccessary modules via Pip, `pip install requests, beautifulsoup4`<br />
**4)** Display the Klyda help prompt for usage, `python3 klyda.py -h`

>Klyda has been tested on Windows & Linux, but should work on any machine capable of running Python.
