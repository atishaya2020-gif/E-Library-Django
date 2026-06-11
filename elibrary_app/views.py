from django.shortcuts import redirect, render, get_object_or_404

from elibrary_app.forms import EBooksForm
from elibrary_app.models import EBook

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def Registers(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['first--name']
        lastName = request.POST['last--name']


        if User.objects.filter(username=email).exists():

            messages.info(
                request,
                'User already exists'
            )

            return render(request, 'register.html')


        else:

            User.objects.create_user(
                username=email,
                password=password,
                first_name=firstName,
                last_name=lastName
            )


            messages.success(
                request,
                "Account created successfully 🎉"
            )


            return redirect('login')


    return render(request, 'register.html')







def Login(request):

    if request.method == 'POST':

        email = request.POST['email']

        password = request.POST['password']



        user = auth.authenticate(

            username=email,

            password=password

        )



        if user is not None:


            auth.login(request,user)


            messages.success(
                request,
                "Welcome back 📚"
            )


            return redirect('home')



        else:


            messages.info(
                request,
                'Invalid Credentials'
            )



    return render(request,'login.html')








def logout(request):

    auth.logout(request)


    messages.success(
        request,
        "Logged out successfully"
    )


    return redirect('home')









def home(request):

    return render(
        request,
        'home.html'
    )










def explore(request):


    books = EBook.objects.all()


    search = request.GET.get('search')

    category = request.GET.get('category')




    if search:


        books = books.filter(
            title__icontains=search
        ) | books.filter(
            summary__icontains=search
        )





    if category and category != "All":


        books = books.filter(
            category=category
        )




    return render(

        request,

        'explore.html',

        {

            'books':books,

            'search':search,

            'category':category

        }

    )









@login_required
def addBook(request):


    if request.method == "POST":


        form = EBooksForm(
            request.POST,
            request.FILES
        )



        if form.is_valid():


            book = form.save(commit=False)


            book.author = request.user


            book.save()



            messages.success(
                request,
                "Book uploaded successfully 📚"
            )



            return redirect("explore")




    else:


        form = EBooksForm()




    return render(

        request,

        "addBook.html",

        {

            "form":form

        }

    )









@login_required
def contri(request):


    books = EBook.objects.filter(

        author=request.user

    )


    return render(

        request,

        'contri.html',

        {

            'books':books

        }

    )









@login_required
def deleteBook(request,book_id):


    book = get_object_or_404(

        EBook,

        id=book_id,

        author=request.user

    )




    if request.method == "POST":


        book.delete()



        messages.success(
            request,
            "Book deleted successfully 🗑"
        )



        return redirect('contri')





    return render(

        request,

        'deleteBook.html',

        {

            'book':book

        }

    )










@login_required
def editBook(request,book_id):


    book = get_object_or_404(

        EBook,

        id=book_id,

        author=request.user

    )




    if request.method=="POST":



        form = EBooksForm(

            request.POST,

            request.FILES,

            instance=book

        )




        if form.is_valid():


            form.save()



            messages.success(
                request,
                "Book updated successfully ✨"
            )



            return redirect('contri')




    else:


        form = EBooksForm(instance=book)





    return render(

        request,

        'editBook.html',

        {

            'form':form,

            'book':book

        }

    )










def viewBook(request,book_id):


    book = get_object_or_404(

        EBook,

        id=book_id

    )



    return render(

        request,

        'viewBook.html',

        {

            'book':book

        }

    )