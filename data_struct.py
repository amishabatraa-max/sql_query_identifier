#String operators in detail 
given_str = "+49 (172) 123-4567" # output: 00491721234567
new_output = given_str.replace("+","00").replace(" ","").\
    replace("(","").replace(")","").replace("-","")
print(f"performed string operations on: {given_str} and changed it to: {new_output}")
print(f"The length comparison:{len(given_str)-len(new_output)}")

given_str_2 = "Adma-24-Dubai 14:30"
x1 = given_str_2.split(" ")
print(x1)
x2 = [x1.split("-") for x1 in x1]
print(x2)
for x in x2:
    for y in range(len(x)):
        print(x[y])

given_query = " 968-Maria , (D@t@ Engineering ) ;; 27y "
answer_query = given_query.strip().replace(";;",",").\
    replace("@","a").replace("y","").replace("968-","").replace("(","").\
    replace(")","").split(",")
for i in answer_query:
    i.lower().strip()
print(answer_query)
print(f"name: {answer_query[0].lower().strip()} | role: {answer_query[1].lower().strip()} | age: {answer_query[2].lower().strip()}")
