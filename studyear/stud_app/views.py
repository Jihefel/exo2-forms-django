from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

# Create your views here.
def home(request):
       members = Member.objects.all()
       students = {
           'all_members': members,
           'female_members': members.filter(gender='femme'),
           'male_members': members.filter(gender='homme')
       }
       return render(request, 'stud_app/home.html', students)

def add_member(request):
       if request.method == 'POST':
           form = MemberForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('home')
       else:
           form = MemberForm()
       return render(request, 'stud_app/add_member.html', {'form': form})
