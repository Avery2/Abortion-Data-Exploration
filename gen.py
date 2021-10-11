import os
from os import listdir
from os.path import isfile, join

mypath = "./img/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlypng = [f for f in onlyfiles if f.split('.')[1] == "png"]
# os.system("ls *.png")

imgs = []
grp = []
for p in onlypng:
    gp, img = p.split("_", 1)
    imgs.append((gp, img))
    grp.append(gp)

grp = list(set(grp))

#   <img width="45%" alt="" src="">

container = """
<div align="center">
  [IMG_HOOK]

  <p>Words go here.</p>
</div>
"""

# print(f"imgs {imgs}")
# print(f"grp {grp}")
groups = {g: [] for g in grp}

for i in imgs:
    groups[i[0]].append(i[1])

# print(groups)
# for g, i in groups.items():
#     print(f"{g}: {i}")

# group will be lists with group name at index 0

for g, l in groups.items():
    img_s = []
    for i in l:
        src = mypath+g+"_"+i
        s = f"<img width=\"45%\" alt=\"{g+i}\" src=\"{src}\">"
        img_s.append(s)
        # print(s)
    section = container.replace("[IMG_HOOK]", '\n'.join(img_s))
    print(section)
