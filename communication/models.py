from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название школы')
    address = models.CharField(max_length=200, verbose_name='Адрес школы')
    established = models.DateField(verbose_name='Дата основания школы')
    type = models.CharField(max_length=100, verbose_name='Тип школы')
    website = models.URLField(verbose_name='Веб сайт школы')

    def __str__(self) :
        return f'{self.name}'

class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя директора')
    age = models.IntegerField(verbose_name='Возраст директора')
    experience = models.IntegerField(verbose_name='Опыт работы директора')
    qualification = models.CharField(max_length=200, verbose_name='Квалификация директора')
    school = models.OneToOneField(School, on_delete=models.CASCADE, verbose_name='Школа которой руководит')

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'

class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя учителя')
    age = models.IntegerField(verbose_name='Возраст учителя')
    subject = models.CharField(max_length=100, verbose_name='Предмет который преподает')
    experience = models.IntegerField(verbose_name='Опыт работы')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'

class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название предмета')
    code = models.CharField(max_length=10, verbose_name='Дод предмета')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='taught_subjects')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='offered_subjects')

    def __str__(self) -> str:
        return f'{self.name}, {self.code}'

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата урока')
    start_time = models.TimeField(verbose_name='Начало урока')
    end_time = models.TimeField(verbose_name='Конец урока')
    classroom = models.CharField(max_length=50, verbose_name='Аудитория')

    def __str__(self) -> str:
        return f'{self.subject}, {self.date}'

class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя студента')
    age = models.IntegerField(verbose_name='Возраст студента')
    grade = models.IntegerField(verbose_name='Класс в котором учится')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'

class Schedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата урока')

    def __str__(self) -> str:
        return f'{self.student}, {self.lesson}, {self.date}'

class Classroom(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер аудитории')
    capacity = models.IntegerField(verbose_name='Вместимость')
    floor = models.IntegerField(verbose_name='Этаж')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.number}, {self.capacity}, {self.floor}'