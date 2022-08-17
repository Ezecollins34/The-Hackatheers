'DIRS': ['mac/templates'],

from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='Home'),
                  path('blog/', include("blog.urls")),
                  path('shop/', include("shop.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <title>Welcome To My Awesome Cart</title>
  </head>
  <body>
    <div class="jumbotron">
  <h1 class="display-4">Welcome To My Awesome Cart</h1>
  <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <a class="btn btn-primary btn-lg" href="/shop" role="button">Go To Shop</a>
  <a class="btn btn-primary btn-lg" href="/blog" role="button">GO To Blog</a>
</div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."

update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
update.save()

{ % extends
'shop/basic.html' %}
{ % block
title %} My
Awesome
Cart
Tracker
{ % endblock %}
{ % block
body %}
< div


class ="container" >

< div


class ="col my-4" >

< h2 > Enter
Your
Order
Id and Email
address
to
track
your
order < / h2 > 4

< form
method = "post"
action = "/shop/checkout/" > { % csrf_token %}
< div


class ="form-row" >

< div


class ="form-group col-md-6" >

< label
for ="inputname" > Order Id < / label >
< input
type = "text"


class ="form-control" id="orderId" name="orderId" placeholder="Orer Id" >

< / div >
< div


class ="form-group col-md-6" >

< label
for ="inputEmail4" > Email < / label >
< input
type = "email"


class ="form-control" id="email" name="email" placeholder="Email" >

< / div >
< button
type = "submit"


class ="btn btn-primary" > Track Order < / button >

< / div >
< / div >
< div


class ="col my-4" >

< h2 > Your
Order
Status: < / h2 >
< div


class ="my-4" >

< ul


class ="list-group" id="items" >

< / ul >
< / div >

< / div >
< / div >
{ % endblock %}
{ % block
js %}
< script >
if (localStorage.getItem('cart') == null) {
var cart = {};
} else {
cart = JSON.parse(localStorage.getItem('cart'));
}
console.log(cart);
var
sum = 0;
if ($.isEmptyObject(cart)) {
// If object is empty
mystr = "<p>Your cart is empty, please add some items before checking out ! </p>"
$('#items').append(mystr);
}

for (item in cart) {

    let name = cart[item][1];
let qty = cart[item][0];
sum = sum + qty;
mystr = ` < li


class ="list-group-item d-flex justify-content-between align-items-center" >

${name}
< span


class ="badge badge-primary badge-pill" > ${qty} < / span >

< / li > `
$('#items').append(mystr);
}
document.getElementById('cart').innerHTML = sum;
$('#itemsJson').val(JSON.stringify(cart));
{ % if thank %}
alert("Thanks for ordering with us. Your order id is {{id}}. Use it to track your order using our order tracker")
localStorage.clear();
document.location = "/shop";
{ % endif %}
< / script >
    { % endblock %}


