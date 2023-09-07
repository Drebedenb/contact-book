from rest_framework.permissions import IsAuthenticated

from .filters import ContactFilter
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_class = ContactFilter
    permission_classes = [IsAuthenticated]
