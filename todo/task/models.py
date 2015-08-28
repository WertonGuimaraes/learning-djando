from django.db import models

class Task(models.Model):	
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def get_title(self):
        return self.title
		
    def to_string(self):
        return "Titulo = %s\nCompleto = %s" %(self.title, self.completed)
        
    def get_pk(self):
        return self.pk
		
    def set_pk(self, pk):
        self.pk = pk
