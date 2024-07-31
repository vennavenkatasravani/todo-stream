from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo, Note
from .forms import NoteForm

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)
    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    todo.isCompleted = True if isCompleted == 'on' else False
    todo.save()
    return redirect('todos:index')

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    notes = todo.notes.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.todo = todo
            note.save()
            return redirect('todos:todo_detail', todo_id=todo_id)
    else:
        form = NoteForm()
    return render(request, 'todos/todo_detail.html', {'todo': todo, 'notes': notes, 'form': form})
