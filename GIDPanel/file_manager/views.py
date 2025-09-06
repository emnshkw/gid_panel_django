# downloads/views.py
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import File

def download_file(request, file_id):
    obj = get_object_or_404(File, id=file_id)
    try:
        response = FileResponse(obj.file.open("rb"), as_attachment=True, filename=obj.name)
        return response
    except FileNotFoundError:
        raise Http404("Файл не найден")
