from django import forms
from .models import Member,User


class MemberForm (forms.Form):
    id = forms.IntegerField()
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    joined_date = forms.DateField()
    phone = forms.CharField(max_length=20)
    married = forms.BooleanField()
    slug = forms.SlugField()


class CreateMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname','lastname','joined_date','phone','married','slug']
        def __init__(self,*args,**kwargs):
            super(CreateMember,self).__init__(*args, **kwargs)



class UpdateMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname','lastname','joined_date','phone','married','slug']
        def __init__(self,*args,**kwargs):
            super(UpdateMember, self).__init__(*args, **kwargs)

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','username', 'password','firstname','lastname','email','address','phone']
        def __init__(self,*args,**kwargs):
            super(UpdateUser, self).__init__(*args, **kwargs)

class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','username', 'password','firstname','lastname','email','address','phone']
        def __init__(self,*args,**kwargs):
            super(CreateUser, self).__init__(*args, **kwargs)