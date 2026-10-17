from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Task
from .forms import StudentRegistrationForm, TaskForm


def home(request):
    return render(request, 'tasks/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                'Your account has been created successfully!'
            )

            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()

    return render(request, 'tasks/register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }

    return render(request, 'tasks/dashboard.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, 'Task added successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'page_title': 'Add New Task',
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'page_title': 'Edit Task',
    })


@login_required
def delete_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        task.delete()

        messages.success(request, 'Task deleted successfully!')
        return redirect('dashboard')

    return render(
        request,
        'tasks/task_confirm_delete.html',
        {'task': task}
    )

@login_required
@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    task.completed = not task.completed
    task.save(update_fields=['completed'])

    if task.completed:
        messages.success(request, 'Task marked as completed!')
    else:
        messages.info(request, 'Task marked as pending!')

    return redirect('dashboard')

@login_required
@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')