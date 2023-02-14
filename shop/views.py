from django.shortcuts import render,redirect,HttpResponse
from . models import Product
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def index(request):
    product_objects=Product.objects.all()
    item =request.GET.get('item')
    if item!=0 and  item is not None:
        product_objects=product_objects.filter(name__icontains=item)
   
     
    return render(request,'index.html',{'product_objects':product_objects})
def detail_page(request,id):
    product_details=Product.objects.get(id=id)
    return render(request,'detail.html',{'product_details':product_details})

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username is taken.')
                return redirect("/signup")
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email is already exist.')
                return redirect("/signup")
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            messages.success(request, 'user is created.')
            return redirect("/log_in")
            

           

        else:
            # messages.success(request, 'password is not matching.')
            print("password is not matching")
            return redirect("/signup")

        
 
        

    

    return render(request,'signup.html')


def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
          
        else:
            messages.success(request,"invalid credentail")
            return redirect("/log_in")
    else:

        return render(request,"log_in.html")
    
def log_out(request):
    auth.logout(request)
    return redirect("/")


def forgot(request):
    if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']
         if User.objects.filter(username=username).exists():
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()
            return redirect("/log_in")
         else:
            messages.success(request,"username is not exist")
    
    else:
        return render(request,"forgot.html")

@login_required(login_url="/log_in")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/log_in")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/log_in")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/log_in")
def item_decrement(request, id):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("cart_detail")
    except:
       return redirect("cart_detail")
    


@login_required(login_url="/log_in")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/log_in")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')











