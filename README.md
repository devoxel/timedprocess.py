#timedprocess.py
===============

##What is it?
---------------
A simple command line tool to run a program for a specified duration. 

##\Features?
---------------
usage: timedprocess <options> <duration> <path>

Duration:
\tA string containing a time, for example:
```
"5h"
"5h25m"
"25m40s4h"
```

Options:
\t--hide-time-remaining \t\t flags to hide the time remaining.
\t-help, -h, --help \t\t Show this message and exit.

##How do I install it?
---------------
The project uses Python's automatic script creation, so if everything goes well, after the project is installed you should be able to run it straight away from terminal the same way you would run pip for instance.

I recommend using pip to install:
`pip install timedprocess.py

If you prefer you can try use easy_install on the setup.py, although I haven't tested this yet.