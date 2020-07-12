out = open('data/out.txt', 'w')

for line in open('data/seashell.log', encoding="utf8").readlines():
    if "compileAndRunProject" in line:
        dt_str = line.split("]")[0][1:-5]
        out.write(dt_str)
        out.write("\n")
out.close()
