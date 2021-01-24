from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Project,User,Profile,Comment
import datetime as dt

class ProjectTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='deborah')
        self.user1.save()


        self.image=Project(title='leaves',description='beautiful',user=self.user1,likes="1",post="image")
        self.image.save_image()


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_image()
        images=Project.objects.all()
        self.assertTrue(len(images)>0)


    def test_delete_method(self):
        '''
        test of delete image
        '''

        Project.objects.all().delete()



    def test_filter_by_name(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_name(self.image.title)
        image=Project.objects.filter(title=self.image.title)
        self.assertTrue(img,image)

class CommentTestClass(TestCase):

    def setUp(self):

        self.user1 = User(username='deborah')
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()

        self.ingabire=Project(2,title='Ingabire',description='beautiful',user=self.user1,likes="1",post="image")
        self.ingabire.save_image()

        self.com=Comment(comment='leaves',comment_image=self.ingabire,posted_by=self.nature,)
        self.com.save_com()


    def test_instance(self):

        self.assertTrue(isinstance(self.com,Comment))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.com.save_com()
        comm=Comment.objects.all()
        self.assertTrue(len(comm)>0)
    def test_delete_method(self):
        '''
        test of delete image
        '''

        Comment.objects.all().delete()

class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user1 = User(username='deborah')
        self.user1.save()
        # self.image=Profile(name='leaves',description='beautiful',user=self.user1,likes="1",post="image")
        # self.image.save_image()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()


    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Profile))


    def test_save_method(self):
        '''
        test image by save
        '''
        self.nature.save_prof()
        comm=Profile.objects.all()
        self.assertTrue(len(comm)>0)

    def test_delete_method(self):
        '''
        test of delete image
        '''

        Profile.objects.all().delete()
