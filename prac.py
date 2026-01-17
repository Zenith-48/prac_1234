import sys
if len(sys.argv)==2:
    script_name=sys.argv[0]
    a=sys.argv[1]
    b=sys.argv[2]
else:
    script_name=sys.argv[0]
    a="6"
    b="2"
    x,y=int(a),int(b)
    while y:
        x,y=y,x%y
        hcf=x
        lcm=int(a*b)/hcf
print("HCF is:",hcf)
print("LCM is:",lcm)
