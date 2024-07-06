from django.shortcuts import render, redirect,get_object_or_404
from .forms import TodoForm
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'home.html', {"todos": todos,'form': form})


def edit(request, pk):
    instance_to_be_edited = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=instance_to_be_edited)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=instance_to_be_edited)
    return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    todo_to_delete = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo_to_delete.delete()
        return redirect('home')
    return render(request, 'delete.html', {'Todo': todo_to_delete})