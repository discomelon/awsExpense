from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
	return render(request, 'index.html')


def display_Farhan(request):
	items = Farhan.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		items = items.filter(Image__icontains=search_term)
	context = {
	'items': items,
	'search_term': search_term, 
	'header': 'Farhan'
	}
	return render(request, 'index.html',context)


def display_Nadia(request):
	items = Nadia.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		items = items.filter(Title__icontains=search_term)
	context = {
	'items': items,
	'search_term': search_term, 
	'header': 'Nadia'
	}
	return render(request, 'index.html',context)


def display_FarhanFamily(request):
	items = FarhanFamily.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		items = items.filter(Title__icontains=search_term)
	context = {
	'items': items,
	'search_term': search_term, 
	'header': 'FarhanFamily'
	}
	return render(request, 'index.html',context)


def display_Ongie(request):
	items = Ongie.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		items = items.filter(Title__icontains=search_term)
	context = {
	'items': items,
	'search_term': search_term, 
	'header': 'Ongie'
	}
	return render(request, 'index.html',context)

def display_Orange(request):
	items = Orange.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		items = items.filter(Title__icontains=search_term)
	context = {
	'items': items,
	'search_term': search_term, 
	'header': 'Orange'
	}
	return render(request, 'index.html',context)


def add_Farhan(request):
	if request.method == "POST":
		form = FarhanForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display_Farhan')

	else:
		form = FarhanForm()
		return render(request, 'add_new.html', {'form' : form})

def add_Nadia(request):
	if request.method == "POST":
		form = NadiaForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display_Nadia')

	else:
		form = NadiaForm()
		return render(request, 'add_new.html', {'form' : form})


def add_FarhanFamily(request):
	if request.method == "POST":
		form = FarhanFamilyForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display_FarhanFamily')

	else:
		form = FarhanFamilyForm()
		return render(request, 'add_new.html', {'form' : form})


def add_Ongie(request):
	if request.method == "POST":
		form = OngieForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display_Ongie')

	else:
		form = OngieForm()
		return render(request, 'add_new.html', {'form' : form})


def add_Orange(request):
	if request.method == "POST":
		form = OrangeForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display_Orange')

	else:
		form = OrangeForm()
		return render(request, 'add_new.html', {'form' : form})


def edit_Farhan(request, pk):
	item = get_object_or_404(Farhan, pk=pk)

	if request.method == "POST":
		form = FarhanForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_Farhan')
	else:
		form = FarhanForm(instance=item)

		return render(request, 'edit_item.html', {'form' : form})


def edit_Nadia(request, pk):
	item = get_object_or_404(Nadia, pk=pk)

	if request.method == "POST":
		form = NadiaForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_Nadia')
	else:
		form = NadiaForm(instance=item)

		return render(request, 'edit_item.html', {'form' : form})


def edit_FarhanFamily(request, pk):
	item = get_object_or_404(FarhanFamily, pk=pk)

	if request.method == "POST":
		form = FarhanFamilyForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_FarhanFamily')
	else:
		form = FarhanFamilyForm(instance=item)

		return render(request, 'edit_item.html', {'form' : form})


def edit_Ongie(request, pk):
	item = get_object_or_404(Ongie, pk=pk)

	if request.method == "POST":
		form = OngieForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_Ongie')
	else:
		form = OngieForm(instance=item)

		return render(request, 'edit_item.html', {'form' : form})

def edit_Orange(request, pk):
	item = get_object_or_404(Orange, pk=pk)

	if request.method == "POST":
		form = OrangeForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_Orange')
	else:
		form = OrangeForm(instance=item)

		return render(request, 'edit_item.html', {'form' : form})


def delete_Farhan(request, pk):

	Farhan.objects.filter(id=pk).delete()

	items = Farhan.objects.all()

	context = {
	'items' : items
	}

	return render(request, 'index.html', context)


def delete_Nadia(request, pk):

	Nadia.objects.filter(id=pk).delete()

	items = Nadia.objects.all()

	context = {
	'items' : items
	}

	return render(request, 'index.html', context)


def delete_FarhanFamily(request, pk):

	FarhanFamily.objects.filter(id=pk).delete()

	items = FarhanFamily.objects.all()

	context = {
	'items' : items
	}

	return render(request, 'index.html', context)


def delete_Ongie(request, pk):

	Ongie.objects.filter(id=pk).delete()

	items = Ongie.objects.all()

	context = {
	'items' : items
	}

	return render(request, 'index.html', context)


def delete_Orange(request, pk):

	Orange.objects.filter(id=pk).delete()

	items = Orange.objects.all()

	context = {
	'items' : items
	}

	return render(request, 'index.html', context)

