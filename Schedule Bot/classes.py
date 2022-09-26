import time


class Time:
    def __init__(self, day, hours, minutes):
        self.day = day
        self.hours = hours
        self.minutes = minutes


class Task:
    def __init__(self, name, day, hours, minutes):
        self.name = name
        self.curTime = Time(day, hours, minutes)

    def retMin(self):
        diff = 0
        diff += self.curTime.day * 24
        diff += self.curTime.hours
        diff *= 60
        diff += self.curTime.minutes
        return diff


def cmp(task):
    return task.curTime.day, task.curTime.hours, task.curTime.minutes


class Schedule:
    def __init__(self):
        self.remind = 0
        self.taskList = []

    def addTask(self, newTask):
        self.taskList.append(newTask)
        self.taskList.sort(key=cmp)

    def deleteTask(self, index):
        index -= 1
        if index >= 0 and index < len(self.taskList):
            self.taskList.pop(index)
            return True
        return False

    def rescheduleTask(self, index, newTask):
        index -= 1
        if not self.deleteTask(index):
            return False
        else:
            self.addTask(newTask)
            return True

