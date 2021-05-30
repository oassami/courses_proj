from django.db import models

class CourseManager(models.Manager):
    def addCourseValidation(self, post_data):
        errors = {}
        if len(post_data['c_name']) < 5:
            errors['c_name'] = 'Course name must be at least 5 characters'
        if len(post_data['c_desc']) < 15:
            errors['c_desc'] = 'Description must be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
