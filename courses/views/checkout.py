from django.shortcuts import get_object_or_404, render
from ..models import Course

def checkout(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/check_out.html', {'course': course})