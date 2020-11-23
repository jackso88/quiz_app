from django.db import models

# Create your models here.
class Test(models.Model):
	text = models.CharField(max_length=200)
	def __str__(self):
		return self.text
	
class Question(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	text = models.TextField()
	class Meta:
		verbose_name_plural = 'questions'
	def __str__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.TextField()
	correct = models.BooleanField(default=False)
	class Meta:
		verbose_name_plural = 'answers'
	def __str__(self):
		return self.text

class Cache(models.Model):
	res = models.IntegerField(default = 0)
	ind = models.IntegerField(default = 0)
