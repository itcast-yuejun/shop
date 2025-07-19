class Employee(object):
    """员工表"""
    # is_leave=0 表示在职，1表示离职
    def __init__(self,name,gender,age,mobile_number,is_leave=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.is_leave = is_leave #is_leave=True表示离职，否则表示在职

    def __str__(self):
        msg = '离职' if self.is_leave else '在职'
        return f'{self.name}\t{self.age}\t{self.gender}\t{self.mobile_number}\t{msg}'

if __name__ == '__main__':
    e = Employee('张三','女',23,'123456')
    print(e.__dict__)#把python对象转换成字典
    print(vars(e)) #也是可以把python对象转换成字典
    print(e)