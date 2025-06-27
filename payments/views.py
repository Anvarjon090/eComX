from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Test tovar',
                        },
                        'unit_amount': 1500,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/payments/success/',
                cancel_url='http://localhost:8000/payments/cancel/',
            )
            return JsonResponse({'checkout_url': session.url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponse("Faqat POST so'rovi yuboring.", status=405)
    
    