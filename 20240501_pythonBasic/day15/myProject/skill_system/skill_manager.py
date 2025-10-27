from skill_system.skill_dep import SkillDep


class SkillManager:
    def fun2(self):
        print("我是SkillManager的fun2")


dep = SkillDep()
dep.fun1()

# 在main.py中调用SkillManager实例的方法
# 在SkillManager.py中调用SkillDep实例的方法
# 在SkillDep.py中调用Helper实例的方法
