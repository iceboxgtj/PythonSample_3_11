input_num1 = int(input("첫번채 숫자를 입력하세요:"))
input_num2 = int(input("두번채 숫자를 입력하세요:"))
input_op = input("어떤 연산(+,-,*,/) :")

if input_op == "+":
    print(f"{input_num1} + {input_num2} = {input_num1+input_num2}")
elif input_op == "-":
    print(f"{input_num1} - {input_num2} = {input_num1-input_num2}")
elif input_op == "*":
    print(f"{input_num1} * {input_num2} = {input_num1*input_num2}")
elif input_num2 == 0:
    print("0으로 나눌수는 없지")    
elif input_op == "/":
    print(f"{input_num1} / {input_num2} = {input_num1/input_num2}")    
else:
    print(f"연산에 뭘 입력한거지 {input_op}")
        