# creating a variable to represent everything after the = and putting triple quotes to allow for a multi line string
old_str = """ORIGIN
    1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy
lvcgergffy tpktrreaed
    61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic 
slyqlenycn
//"""
#creating a variable (unwanted_chars) to equal all the things I want to take out of the old_str "ORIGIN", "1", "6", "//", " ", "\n"]
unwanted_chars = ["ORIGIN", "1", "6", "//", " "
, "\n"]

# for this variable(i) in unwanted_chars replace(.replace(varible, "something here")) the unwanted characters(unwnated_chars) with ""(nothing)  
for i in unwanted_chars:
    old_str = old_str.replace(i, "")
#print the old_str with the unwanted characters removed
print(old_str)

#print to screen the length in thclear old_str (like wc in BASH)
print(len(old_str))

# setting insulin_i to equal the first 24 characters in old_str
insulin_i = old_str[0 : 24]
print(insulin_i)
print(len(insulin_i))
