
#edit test
#class 테스트

class character():
    
    #init은 class가 생성될때마다 등장합니다
    def __init__(self, name = "No", health = 100, money = 100):
        self.name = name
        self.money = money
        self.health = health
        print(f"{self.name} spawned with ${self.money}")

    def checkmoney(self):
        return self.money

    def checkhealth(self):
        return self.health

    def __del__(self):
        print(f"{self.name}이 사망하였습니다")

print("Character Spawn Module")

nameofplr = input("스폰하고싶은 캐릭터 이름?: ")

player = character(nameofplr)

while True:
    question = input("하고싶은활동\n모르겠으면 'help'을 입력해주세요\n:")

    if question.lower() == "help":
        print("checkmoney, checkhealth, suicide")
        continue
    elif question.lower() == "checkmoney":
        print(player.checkmoney())
        continue
    elif question.lower() == "checkhealth":
        print(player.checkhealth())
        continue
    elif question.lower() == "suicide":
        del player
        break
print("게임 오버")