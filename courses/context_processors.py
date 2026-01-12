from .models import AdditionalInfo

def additional_info_processor(request):
    """
    সব template-এ 'additional_info' automatically পাঠাবে
    """
    if request.user.is_authenticated:
        additional_info, _ = AdditionalInfo.objects.get_or_create(user=request.user)
        return {'additional_info': additional_info}
    return {}
