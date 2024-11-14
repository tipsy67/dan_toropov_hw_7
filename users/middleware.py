# from django.utils import timezone
#
# class UpdateLastLoginMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print(1)
#         if request.user.isauthenticated():
#             print(11)
#             request.user.last_login = timezone.now()
#             request.user.save(update_fields=['last_login'])
#         response = self.get_response(request)
#         return response
