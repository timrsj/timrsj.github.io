import subprocess as cmd 

message = 'update '
cp = cmd.run("git add *.*", check=True, shell=True)
print(cp)
cp = cmd.run(f"git commit -m {message}", check=True, shell=True)
print(cp)

cp = cmd.run("git push -u origin master -f", check=True, shell=True)
print(cp)

