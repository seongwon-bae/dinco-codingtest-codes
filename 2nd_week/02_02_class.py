class Person:
    # 클래스를 만들때 호출되는 생성자 함수
    # self 는 객체 자기 자신이라는 뜻
    def __init__(self, name_param):
        self.name = name_param # self의 name에 값 저장
        print('hihi i am created', self, self.name)

    # Method - 클래스 내부 함수
    def talk(self):
        print('안녕하세요 저는',self.name,'입니다')

person_1 = Person('유재석')
person_1.talk()
person_2 = Person('박명수')
person_2.talk()