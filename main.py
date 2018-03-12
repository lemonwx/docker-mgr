import sh
cmd = "images"
ret = sh.docker()
print(ret.__str__())

