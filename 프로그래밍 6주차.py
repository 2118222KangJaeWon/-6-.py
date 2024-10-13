# Quiz 1
class User:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.contact} 입니다.")

if __name__ == "__main__":
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    contact = input("연락처를 입력하세요 (형식: 000-0000-0000): ")

    user = User(name, age, contact)
    user.info()

# Quiz 2
def check_length_of_message(message):
    length = len(message)
    if length <= 20:
        return 50  # 요금 50원
    else:
        return 100  # 요금 100원

if __name__ == "__main__":
    message = input("문자 메시지를 입력하세요: ")
    fee = check_length_of_message(message)
    print(f"문자 메시지 요금은 {fee}원입니다.")