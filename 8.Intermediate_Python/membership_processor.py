name_box = "Alice Bentall"
age_box = "20"
uni_box = " "
subs_box = "1.99"
mkt_box = "0"

name_entered = bool(name_box)
if name_entered:
    name = name_box
else:
    name = "unknown"

age = int(age_box)
student = bool(uni_box)
subscription = float(subs_box)
marketing = bool(int(mkt_box))

profile = name +', ' + str(age)
print(profile)