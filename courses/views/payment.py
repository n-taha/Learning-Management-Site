from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from courses.models.manual_payment import ManualPayment
from courses.models.course import Course
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def submit_manual_payment(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id')
        payer_number = request.POST.get('payer_number')

        # save to ManualPayment model
        ManualPayment.objects.create(
            user=request.user,
            course=course,
            payment_method=payment_method,
            transaction_id=transaction_id,
            payer_number=payer_number
        )

        messages.success(
            request,
            f"পেমেন্ট সফলভাবে জমা দেওয়া হয়েছে! \nপেমেন্ট মাধ্যম: {payment_method}, ট্রানজেকশন আইডি: {transaction_id}\n\nআমরা সবকিছু যাচাই করে আগামী ৬ ঘণ্টার মধ্যে আপনাকে কোর্সে প্রবেশাধিকার দিয়ে দেব।\nযেকোনো সমস্যার জন্য কল করতে পারেন: ০১৭XXXXXXXX"
            )

        return redirect('checkout', slug=slug)

    return redirect('checkout', slug=slug)
