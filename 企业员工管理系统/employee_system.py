from employee import Employee
import os

class EmployeeManagerSystem(object):


    def __init__(self):
        # 存放员工数据的文件
        self.employee_data_file = 'employee.data'

        #上次保存前的员工备份文件，而且只备份一个
        self.employee_data_file_backup = 'employee.data.backup'

        self.employee_list = [] #从文件中加载之后的员工列表

        self.save_flag = True #已经保存员工数据
    def main(self):
        """员工管理系统的入口"""
    # 1,加载和读取员工数据文件
        self.load_employee()
        while True:
            # 2,显示欢迎界面
            self.show_hello()

            #由用户输入指定的功能数字
            menu_number = int(input('请输入你需要的功能编号:'))

            if menu_number ==7:
                self.go_out()
                break
            elif menu_number ==1:
                self.add_employee()
            elif menu_number ==2:
                self.del_employee()
            elif menu_number ==3:
                self.update_employee()
            elif menu_number ==4:
                self.search_employee()
            elif menu_number ==5:
                self.show_all_employee()
            elif menu_number ==6:
                self.save_employee()

    def go_out(self):
        """
        退出程序的需求：如果，员工进行了添加，修改，删除。那么必须要保存到文件中
        1，如果没有保存，则在退出之前要自动保存
        2,怎么样：确定有没有保存？
        :return:
        """
        if not self.save_flag:# 员工数据没有保存
            self.save_employee()
        print('谢谢!程序退出！')


    def save_employee(self):
        """
        保存的需求和步骤：
        1，先把原来的数据文件备份(如果已经存在备份文件，则把备份文件删除)
        2，创建新文件
        3，写入数据
        4，关闭文件流
        :return:
        """
        if os.path.exists(self.employee_data_file_backup):
            os.remove(self.employee_data_file_backup) #删除备份文件
        #1,备份
        os.rename(self.employee_data_file,self.employee_data_file_backup)
        #2,打开文件流
        with open(self.employee_data_file,'w',encoding='utf-8') as f:
            #3，写入数据
            new_list = []
            for emp in self.employee_list: #原来的列表中是一个个的emp对象
                new_list.append(emp.__dict__)
            #new_list :[{'name':'zs'},{},{} ]
            f.write(str(new_list))
        self.save_flag = True #刚刚已经保存过了











    def show_all_employee(self):
        """展示所有的员工信息"""
        print('姓名\t年龄\t性别\t手机号码\t是否离职')
        for emp in self.employee_list:
            print(emp)

    def search_employee(self):
        """根据姓名查找员工信息"""
        # 1,输入员工姓名
        search_name = input('请输入要查询的员工姓名:')
        # 遍历员工列表，判断是否存在，存在则修改
        for emp in self.employee_list:
            if emp.name == search_name:
                print(emp)
                break
        else:
            print(f'没有找到名字叫{search_name}的员工')


    def update_employee(self):
        """
        修改员工:首先需要输入被修改的员工新名，然后再依次修改该员工的属性
        :return:
        """
        #1,输入员工姓名
        update_name = input('请输入要被修改的员工姓名:')
        # 遍历员工列表，判断是否存在，存在则删除
        for emp in self.employee_list:
            self.save_flag = False #你完成了一次修改，必须要保存数据
            if emp.name ==update_name: #员工存在
                #3，修改员工其他属性
                new_name = input('请输入新的姓名（不修改直接回车):'.strip())
                emp.name = new_name if new_name else emp.name

                new_sex = input('请输入新的性别（不修改直接回车):'.strip())
                emp.gender = new_sex if new_sex else emp.gender

                new_age = input('请输入新的年龄（不修改直接回车):'.strip())
                emp.age = int(new_age) if new_age else emp.age

                new_number = input('请输入新的手机号码（不修改直接回车):'.strip())
                emp.mobile_number = new_number if new_number else emp.mobile_number

                new_leave = input('请输入是否离职,1表示离职，0表示在职（不修改直接回车):'.strip())
                if new_leave:
                    emp.is_leave = True if int(new_leave) ==1 else False

                print('员工信息已修改：')
                print(emp)
                break
        else: #循环正常结束
            print(f'没有找到名字叫{update_name}的员工')


    def del_employee(self):
       """
       删除员工的需求:首先输入一个被删除的员工姓名
       :param self:
       :return:
       """
       # 1，输入被删除的员工姓名
       del_name = input('请输入要被删除的员工姓名:')
       # 遍历员工列表，判断是否存在，存在则删除
       for emp in self.employee_list:
           if emp.name == del_name:
               self.save_flag = False  # 你完成了一次修改，必须要保存数据
               self.employee_list.remove(emp)
               print(f'名字叫:{del_name}的员工已经删除')
               break
       else:
           print(f'没有找到名字叫{del_name}的员工')

    def add_employee(self):
        """添加员工信息"""
        #1,由用户输入你需要添加员工信息
        name = input('请输入员工的姓名:')
        gender = input('请输入员工的性别:')
        age = int(input('请输入员工的年龄:'))
        mobile_number = input('请输入员工的电话号码:')
        is_leave = int(input('请输入员工是否离职,1表示离职，0表示在职:'))
        #2，创建一个员工对象
        emp = Employee(name,gender,age,mobile_number,is_leave)
        self.save_flag = False  # 你完成了一次修改，必须要保存数据
        #把新加入的员工添加到列表中
        self.employee_list.append(emp)
        #4，把刚刚添加的员工信息，输出
        print(emp)



    @staticmethod
    def show_hello():
        """显示系统的欢迎界面"""
        print('欢迎进入企业员工管理系统')
        print('-'*60)
        print('1:添加员工') #复制快捷键 ctrl + d
        print('2:删除员工')
        print('3:修改员工')
        print('4:查询员工')
        print('5:展示所有员工')
        print('6:保存员工数据')
        print('7:退出系统')
        print('-'*60)




    def load_employee(self):
        """
        读取员工数据文件,把所有的员工信息都放在一个列表
        :return:
        """
        try:
            f = open(self.employee_data_file,'r',encoding='utf-8')
        except Exception as err:
            #如果报错，很可能第一次启动程序。这个文件还不存在。需要创建一下
            f = open(self.employee_data_file,'w',encoding='utf-8')
        else: #没有报错，意味着文件存在
            #读取文件中的数据
            data = f.read()
            if data:
                lst = eval(data)  # 把文件中的内容（字符串），当成Python表达式解析。
                for dict1 in lst:
                    self.employee_list.append(
                        Employee(dict1['name'], dict1['gender'], dict1['age'], dict1['mobile_number'],
                                 dict1['is_leave']))


        finally:
            if f:
                f.close()

if __name__ == '__main__':
    s = EmployeeManagerSystem()
    s.main()
