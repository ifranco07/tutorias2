# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InitialInterviewForm
from .models import InitialInterview

@login_required
def fill_initial_interview(request):
    student = request.user.student
    interview_exists = InitialInterview.objects.filter(student=student).exists()
    
    if request.method == 'POST' and not interview_exists:
        form = InitialInterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.student = student
            interview.save()
            return redirect('student_dashboard')
    else:
        form = InitialInterviewForm()
    
    return render(request, 'interview/initial_interview_form.html', {'form': form, 'interview_exists': interview_exists})

