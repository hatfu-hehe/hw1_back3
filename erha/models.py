from django.db import models


class Fragments(models.Model):
    title = models.CharField(max_length=200, verbose_name="Enter chapter's title")
    passage = models.TextField(verbose_name="Enter content")
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}-{self.created_at}"
    
    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'
    


class CharsErha(models.Model):
    photo = models.ImageField(upload_to='mitban_nvl/', verbose_name="insert character's photo")
    name = models.CharField(max_length=30, verbose_name="enter character's name")
    age = models.PositiveBigIntegerField(verbose_name="enter character's sge", default=26)
    ORGANIZATIONS = (
        ('Sisheng Peak', 'Sisheng Peak'), 
        ('Wubei Temple', 'Wubei Temple'),
        ('Shangqing Pavillion', 'Shangqing Pavillion'),
        ('Guyueye Sect', 'Guyueye Sect'),
        ('Taobao Mountain', 'Taobao Mountain'),
        ('Unknown', 'Unknown')
    )
    organization = models.CharField(max_length=100, choices=ORGANIZATIONS, default='Unknown',
                                    verbose_name="Enter character's sect/organization")
    description = models.TextField(verbose_name="Enter character's background")
    weapon = models.CharField(max_length=100, verbose_name="Enter character's weapon")
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)
    
    class Meta:
        verbose_name = "character"
        verbose_name_plural = "characters"
    
    def __str__(self):
        return self.name
