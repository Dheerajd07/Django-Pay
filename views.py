import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def donation(request):
    if request.method == 'POST':
        # Get the donation amount from the form submission
        amount = request.POST['amount']

        # Create a new Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'Donation',
                'amount': int(float(amount) * 100),
                'currency': 'inr',
                'quantity': 1,
            }],
            success_url=request.build_absolute_uri(reverse('donation_success')),
            cancel_url=request.build_absolute_uri(reverse('donation_cancel')),
        )

        # Redirect the user to the Stripe checkout page
        return redirect(checkout_session.url)

    # Render the donation page template
    return render(request, 'donation.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

@csrf_exempt
def donation_success(request):
    # Render the donation success page template
    return render(request, 'donation_success.html')

@csrf_exempt
def donation_cancel(request):
    # Render the donation cancel page template
    return render(request, 'donation_cancel.html')
