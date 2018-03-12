import sh


def which(cmd):
    ret = sh.docker("help")
    print(ret)

which("images")
