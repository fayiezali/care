# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
# ___________________________________________
# List all categories
def function__read_category_all(request):
    variable__category_all = \
        Categories.objects.all()
    return render(
            request
            , 'categories/category_list.html'
            ,{'variable__category_all'
            : variable__category_all})
# ___________________________________________
# View details of a specific category
def function__read_category_detail(
    request
    ,parameter__category_id):
    variable__category_detail = \
        Categories.read(parameter__category_id)
    return render(
            request
            ,'categories/category_detail.html'
            ,{
            'variable__category_detail'
            :variable__category_detail
            }
                )
# The `# ___________________________________________` in the code is acting as a visual separator or
# divider between different sections of the code. It helps to improve readability and organization by
# visually breaking up the code into distinct parts or functions. It serves as a clear marker to
# indicate the beginning or end of a specific section, making it easier for developers to navigate and
# understand the code structure.
# The `# ___________________________________________` in the code is acting as a visual separator or
# divider between different sections of the code. It helps to improve readability and organization by
# visually breaking up the code into distinct parts or functions. It serves as a clear marker to
# indicate the beginning or end of a specific section, making it easier for developers to navigate and
# understand the codebase.
# ___________________________________________


# Create a new category
# def category_create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST.get('description', '')
#         category = Categories.create(name=name, description=description)
#         return redirect('category_detail', category_id=category.id)
#     return render(request, 'categories/category_form.html')
# def category_create(request):
#     if request.method == 'POST':
#         new_category=None
#         name        = request.POST['name']
#         description = request.POST.get('description', '')
#         new_category= Categories.create(name=name, description=description)
#         return redirect('category_detail', category_id=new_category.id)
#     return render(request, 'categories/category_form.html')

# # category_detail=category_read and category_read=category_detail
# # Read an existing category
# def category_read__(request, category_id):
#     category = None
#     category = get_object_or_404(
#                 Categories
#                 , id=category_id)
#     category = Categories.read(category_id=1)
#     if category:
#         print(category.name)
#         return redirect(
#                 'category_detail'
#                 , category_id=category.id)
#     else:
#         print("Category not found")
#     return render(
#                 request
#                 , 'categories/category_form.html'
#                 , {'category': category})

# # Update an existing category
# def category_update(request, category_id):
#     category = None
#     category = get_object_or_404(
#                 Categories
#                 , id=category_id)
#     if request.method == 'POST':
#         name        = request.POST['name']
#         description = request.POST.get('description', '')
#         category    = Categories.update(
#                         category_id
#                         , name=name
#                         , description=description)
#         return redirect(
#                 'category_detail'
#                 , category_id=category.id)
#     return render(
#                 request
#                 , 'categories/category_form.html'
#                 , {'category': category})


# # Delete a category
# def category_delete(request, category_id):
#     if Categories.delete(category_id=1):
#         print("Category deleted")
#     else:
#         print("Category not found")








# # views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import *
# from django.http import HttpResponse

# # List all categories
# def category_list(request):
#     categories = Categories.objects.all()
#     return render(request, 'categories/category_list.html', {'categories': categories})

# # View details of a specific category
# def category_detail(request, category_id):
#     category = get_object_or_404(Categories, id=category_id)
#     return render(request, 'categories/category_detail.html', {'category': category})

# # Create a new category
# def category_create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST.get('description', '')
#         category = Categories.create(name=name, description=description)
#         return redirect('category_detail', category_id=category.id)
#     return render(request, 'categories/category_form.html')

# # Update an existing category
# def category_update(request, category_id):
#     category = get_object_or_404(Categories, id=category_id)
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST.get('description', '')
#         category = Categories.update(category_id, name=name, description=description)
#         return redirect('category_detail', category_id=category.id)
#     return render(request, 'categories/category_form.html', {'category': category})

# # Delete a category
# def category_delete(request, category_id):
#     category = get_object_or_404(Categories, id=category_id)
#     if request.method == 'POST':
#         Categories.delete(category_id)
#         return redirect('category_list')
#     return render(request, 'categories/category_confirm_delete.html', {'category': category})
