# 1.建立 BMI class(類別)
class BMI:
# 2.init(建構子)，建立屬性(name,gender,age,height,weight)
    def __init__(self, name, gender, age, height, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
# 3.def(方法)
# 建立方法 BMI(回傳MBI值，BMI公式，身高平方/體重)
    def BMI(self):
        BMI = self.weight/(self.height/100)**2
        return BMI

# 建立方法 Body_type(根據BMI，回傳體位信息)
    def Body_type(self):
        bmi = self.BMI()
        if bmi < 18.5:
            return "體重過輕"
        elif bmi < 24:
            return "正常範圍"
        elif bmi < 27:
            return "過重"
        elif bmi < 30:
            return "輕度肥胖"
        elif bmi < 35:
            return "中度肥胖"
        else: 
            return "過度肥胖"
        
# 建立方法 Show(秀出該Class中的所有信息，MBI小數後兩位)
    def Show(self):
        print(f"姓名:{self.name}")
        print(f"姓別:{self.gender}")
        print(f"年齡:{self.age}")
        print(f"身高:{self.height}")
        print(f"體重:{self.weight}")
        print(f"BMI:{self.BMI():.2f}{self.Body_type()}")

# 5.def(方法)進階練習
# 建立方法def Set_age(改變年齡，並顯示宿改前後數值)
    def Set_age(self, Age):
        self.age = Age
# 建立方法def Set_height (改變身高，並顯示宿改前後數值)
    def Set_height(self, Height):
        self.height = Height
# 建立方法def Set_weight(改變體重，並顯示宿改前後數值)
    def Set_weight(self, Weight):
        self.weight = Weight

# 4.信息資料And 建立Object(物件)

Datalist=[["Nephi","男",22,171,45],["巧克力","女",8/12,150,39],["香草","女",8/12,148,35],["楓","女",2,157,42]]
classlist=[] #存放不同的 BMI class
# a=BMI("Nephi","男",22,171,45)
# a.Show()
# a.Set_age(33)
# a.Set_weight(100)
# a.Set_height(199)
# a.Show()
for i in range(len(Datalist)):
    # 利用Datalist資料 導入 BMI class中，提示: i 的右邊建立 Object 物件
    i = BMI(Datalist[i][0], Datalist[i][1], Datalist[i][2],Datalist[i][3], Datalist[i][4])
    i.Show()
    classlist.append(i)
print(classlist)
print(Datalist)
# 6.進階練習
print("\n✾ ✾ ✾ 進階題 ✾ ✾ ✾\n")
# 將Datalist中 巧克力年齡改為9/12，體重改為40，身高改為153，並展示。
print("-"*60)
chocolate = BMI(Datalist[1][0], Datalist[1][1], Datalist[1][2],Datalist[1][3], Datalist[1][4])
chocolate.Set_age(12)
chocolate.Set_weight(40)
chocolate.Set_height(153)
chocolate.Show()
print(chocolate) #chotolate是一個物件
# 將Datalist中 香草年齡改為9/12，體重改為37，身高改為149，並展示。
print("-"*60)
classlist[2].Set_age(9)
classlist[2].Set_weight(37)
classlist[2].Set_height(149)
classlist[2].Show()

