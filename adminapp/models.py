from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE , related_name='teachers')
    kafedra_id = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name="kafedra")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Groups(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subjects, related_name='groups')

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=255, null= False, blank= False)
    last_name = models.CharField(max_length=255, null=False , blank=False)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="students")
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"

