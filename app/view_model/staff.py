from app.models.staff import Staff
from app.models import db


class StaffViewModel:
    def __init__(self, staff):
        self.id = staff.id
        self.name = staff.name
        self.number = staff.number
        self.duty = staff.duty
        self.branch = staff.branch

    def __get_dict(self):
        staff_dict = {
            'id': self.id,
            'number': self.number,
            'name': self.name,
            'duty': self.duty,
            'branch': self.branch
        }
        return staff_dict

    @property
    def info(self):
        return self.__get_dict()


class StaffCollection:
    def __init__(self):
        self.staffs = []
        self.total = 0

    def fill(self, staffs):
        self.total = len(staffs)
        self.staffs = [StaffViewModel(staff).info for staff in staffs]
        return self


# class _StaffViewModel:
#     def __init__(self, staffs):
#         self.staffs = []
#         self.num = 0
#
#     @staticmethod
#     def __staff2dict(staff):
#         staff_dict = {
#             'id': staff.id,
#             'number': staff.number,
#             'name': staff.name,
#             'duty': staff.duty,
#             'branch': staff.branch
#         }
#         return staff_dict
#
#     def query(self, **condition):
#         self.staffs = [self.__staff2dict(staff) for staff in Staff.query.filter_by(**condition).all()]
#         self.num = len(self.staffs)
#         return self
#
#     @property
#     def first(self):
#         return self.staffs[0] if self.num > 0 else None
#
#     def add(self, staff_info):
#         try:
#             staff = Staff(number=staff_info['number'],
#                           name=staff_info['name'],
#                           branch=staff_info['branch'],
#                           duty=staff_info['duty'])
#             db.session.add(staff)
#             db.session.commit()
#             return True
#         except Exception as e:
#             print('添加数据失败', e)
#             return False


if __name__ == "__main__":
    from app import create_app
    with create_app().app_context():
        svm = StaffViewModel()
        print(svm.add({'name': '王佳铖', 'branch': '东华大学', 'duty': '学生', 'number': '2180702'}))
