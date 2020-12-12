def SayHi(name: ste, age: int) -> str:  # 화살표는 return 값의 데이터 타입을 명시
    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert SayHi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert SayHi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print("Done. Time to Check.")