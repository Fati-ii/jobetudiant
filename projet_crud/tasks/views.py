from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.
# liste des taches
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
# creer la tache
#def create_task(request):
 #   form = TaskForm()
  #  return render(request, 'tasks/create_task.html', {'form': form})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirige vers la vue qui affiche les tâches
    else:
        form = TaskForm()
    
    return render(request, 'tasks/create_task.html', {'form': form})



# mise à jour
def task_update(request,pk):
    task=get_object_or_404(Task, pk=pk)
    form=TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_list.html',{'form':form})
 # supprimer
def task_delete(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        task.delete()
        return redirect(task_list)
    return render(request,'tasks/task_confirm_delete.html',{'task':task})



