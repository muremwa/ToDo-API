from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response

from django.shortcuts import get_object_or_404

from .serializers import TodoSerializer, Todo


class Index(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoActions(APIView):
    @staticmethod
    def mark_as_done_or_undone(todo):
        answer = None
        if todo.done == True:
            todo.done = False
            answer = "Now not Done"
        else:
            todo.done = True
            answer = "Now done"
        todo.save()
        return answer

    @staticmethod
    def delete_todo(todo):
        todo.delete()
        return "Todo deleted"
        
    def post(self, *args, **kwargs):
        response = dict()
        todo = get_object_or_404(Todo, pk=kwargs['todo_id'])
        if kwargs['type'] == "done":
            response['result'] = self.mark_as_done_or_undone(todo)
        elif kwargs['type'] == "delete":
            response['result'] = self.delete_todo(todo)
        else:
            response['result'] = "{} not supported".format(kwargs['type'])

        return Response(response)
