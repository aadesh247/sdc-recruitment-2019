from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import ToDoItem
from .forms import ToDoForm


def index(request):
	items = ToDoItem.objects.all()

	form = ToDoForm()
	context = {'all_items': items, 'form':form}
	return render(request, 'index.html',context) 

@require_POST
def addItem(request):
	form = ToDoForm(request.POST)
	if form.is_valid():
		new_todo = ToDoItem(content=request.POST['content'])
		new_todo.save()

	return redirect('index')


def deleteItem(request, item_id):
	item = ToDoItem.objects.get(pk=item_id)
	item.delete()
	return redirect('index')

# def addItem(request):
# 	new_item = ToDoItem(content = request.POST['task'])
# 	new_item.save()
# 	return HttpResponseRedirect('index.html')

# def deleteItem(request, item_id):
# 	temp = ToDoItem.objects.get(id = item_id)
# 	temp.delete()
# 	return HttpResponseRedirect('index.html')

