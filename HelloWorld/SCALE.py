weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    conKL = float(weight) * 2.2
    print("Weight in LB: " + str(conKL))
elif unit.upper() == "L":
    conLK = float(weight) // 2.2
    print("weight in KG: " + str(conLK))
