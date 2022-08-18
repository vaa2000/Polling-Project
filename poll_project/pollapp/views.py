from django.shortcuts import render, redirect
from .models import PollModel
from .forms import PollForm

def home(request):
	data = PollModel.objects.all()
	return render(request,"home.html", {"data":data})

def create(request):
	if request.method == "POST":
		data = PollForm(request.POST)
		if data.is_valid():
			data.save()
			fm = PollForm
			return render(request, "create.html", {"fm":fm, "msg":"added"})
		else:
			fm = PollForm()
			return render(request, "create.html",{"fm":fm, "msg":"check errors"})
	else:
		fm = PollForm()
		return render(request, "create.html",{"fm":fm, "msg":"check errors"})

def vote(request, id):
	data = PollModel.objects.get(id=id)
	if request.method == "POST":
		op = request.POST.get("r1")
		if op == "op1":
			data.op1c += 1
		elif op == "op2":
			data.op2c += 1
		else:
			data.op3c += 1
		data.save()
		return redirect("home")
	else:
		return render(request, "vote.html" ,{"data":data})

def results(request, id):
	data = PollModel.objects.get(id=id)
	return render(request, "results.html",{"data":data})
	