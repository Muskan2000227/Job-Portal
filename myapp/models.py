from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class register_user(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField()
    passw=models.CharField(max_length=40)
    cpassw=models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.id} - {self.email}"
    
class register_emp(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField()
    passw=models.CharField(max_length=40)
    cpassw=models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.id} - {self.email}"    

class Jobs(models.Model):
    title = models.CharField(max_length=255)  
    description = RichTextField(max_length=5000)
    budget_salary = models.CharField(max_length=255)
    education_req = models.CharField(max_length=255, blank=True, null=True)
    experience_req = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  # Storing category as a string
    location = models.CharField(max_length=255)  # Storing location as a string
    jobtag = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255)
    vacancies = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, default='available')
    employer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.location} | {self.category}"
    

class Experience(models.Model):
    user = models.ForeignKey(register_user, on_delete=models.CASCADE)  # Linked to UserProfile
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Can be null for current jobs
    responsibility = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company_name}"  

class Education(models.Model):
    user = models.ForeignKey(register_user, on_delete=models.CASCADE)  # Linked to UserProfile
    title= models.CharField(max_length=255)
    college= models.CharField(max_length=255)
    stream= models.CharField(max_length=255)
    result= models.CharField(max_length=255)
    startingperiod= models.DateField()
    endingperiod= models.DateField()
    
    def __str__(self):
        return f'{self.title}'  

class Skills(models.Model):
    skills=models.CharField(max_length=255)
    user = models.ForeignKey(register_user, on_delete=models.CASCADE)  # Linked to UserProfile
    def __str__(self):
        return f'{self.skills}'

class Resume(models.Model):
    resume=models.FileField(upload_to="resumes/",blank=True,null=True)
    user = models.ForeignKey(register_user, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.user}' 

class Saved(models.Model):
    job= models.ForeignKey(Jobs,on_delete=models.CASCADE,default=1)
    seeker= models.ForeignKey(register_user,on_delete=models.CASCADE,default=1)
    status= models.CharField(max_length=255,blank=True,null=True,default="Saved")
    def __str__(self):
        return f'{self.job}'              
   
# for resume


from ckeditor.fields import RichTextField

class ResumeBuilder(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)  # Rich text field for projects
    certifications=models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name

   