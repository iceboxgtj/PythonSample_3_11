def main() -> None:
    
    add_a = 10 + 20
    sub_b = 20 - 10
    mul_c = 10 * 2
    div_d = 10 / 2
    mod_e = 10 % 3

    print(f"변수타입은 {type(add_a)} 결과는 {add_a}")
    print(f"변수타입은 {type(sub_b)} 결과는 {sub_b}")
    print(f"변수타입은 {type(mul_c)} 결과는 {mul_c}")
    print(f"변수타입은 {type(div_d)} 결과는 {div_d:.2f}")
    print(f"변수타입은 {type(mod_e)} 결과는 {mod_e}")

    a = 123
    b = 7

    print("a =", a)
    print("b =", b)

    print("a / b =", a / b)
    print("a // b =", a // b)
    print("a % b =", a % b)



if __name__ == "__main__":
    main()