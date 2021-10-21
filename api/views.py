from datetime import timezone
from rest_framework.response import Response 
from rest_framework.generics import get_object_or_404
from .models import Poll, Question, Option, UserAnswer
from .serializers import PollSerializer, QuestionSerializer, OptionSerializer, UserAnswerSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, api_view


# login
@csrf_exempt
@api_view(['GET'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please enter username and password!'},
        status=400)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'User not found'}, status=404)
        
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=200)

# poll
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def poll_view(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response({"polls": serializer.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,)) 
def poll_create(request):
    poll = request.data
    serializer = PollSerializer(data=poll, context={'request': request})
    if serializer.is_valid(raise_exseption=True):
        poll_saved = serializer.save()
    return Response({"success": f"Poll {poll_saved.title} saved!"})


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))   
def poll_update_delete(request, pk):
    saved_poll = get_object_or_404(Poll.objects.all(), pk=pk)
    if request.method == 'PATCH':
        data = request.data
        serializer = PollSerializer(instance=saved_poll, data=data, partial=True)

        if serializer.is_valid(raise_exseption=True):
            poll_saved =serializer.save()
        
        return Response({
            "success": f"Poll {poll_saved.title} updated"
        })
    elif request.method == 'DELETE':
        saved_poll.delete()
        return Response({
            "message": f"Poll with id '{pk}'' was deleted"
        }, status=204)

# question
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,)) 
def question_create(request):
    question = request.data

    serializer = QuestionSerializer(data=question, context={'request': request})
    if serializer.is_valid(raise_exseption=True):
        question_saved = serializer.save()
    return Response({"success": f"Question {question_saved.question_text} saved!"})


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))   
def question_update_delete(request, pk):
    saved_question = get_object_or_404(Question.objects.all(), pk=pk)
    if request.method == 'PATCH':
        data = request.data
        serializer = QuestionSerializer(instance=saved_question, data=data, partial=True)

        if serializer.is_valid(raise_exseption=True):
            saved_question =serializer.save()
        
        return Response({
            "success": f"Question {saved_question.title} updated"
        })
    elif request.method == 'DELETE':
        saved_question.delete()
        return Response({
            "message": f"Question with id '{pk}'' was deleted"
        }, status=204)

# question
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,)) 
def option_create(request):
    option = request.data

    serializer = OptionSerializer(data=option, context={'request': request})
    if serializer.is_valid(raise_exseption=True):
        option_saved = serializer.save()
    return Response({"success": f"Option {option_saved.option_text} saved!"})


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))   
def option_update_delete(request, pk):
    saved_option = get_object_or_404(Option.objects.all(), pk=pk)
    if request.method == 'PATCH':
        data = request.data
        serializer = OptionSerializer(instance=saved_option, data=data, partial=True)

        if serializer.is_valid(raise_exseption=True):
            saved_option =serializer.save()
        
        return Response({
            "success": f"Option {saved_option.option_text} updated"
        })
    elif request.method == 'DELETE':
        saved_option.delete()
        return Response({
            "message": f"Option with id '{pk}'' was deleted"
        }, status=204)

# user answer
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_answe_view(request):
    answer = UserAnswer.objects.all()
    serializer = UserAnswerSerializer(answer, many=True)
    return Response({"answer": serializer.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,)) 
def user_answer_create(request):
    serializer = UserAnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exseption=True):
        answer = serializer.save()
    return Response({"success": f"Answer {answer.option_text} saved!"})


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))   
def user_answer_update_delete(request, pk):
    saved_answer = get_object_or_404(UserAnswer.objects.all(), pk=pk)
    if request.method == 'PATCH':
        data = request.data
        serializer = UserAnswerSerializer(instance=saved_answer, data=data, partial=True)

        if serializer.is_valid(raise_exseption=True):
            saved_answer =serializer.save()
        
        return Response({
            "success": f"User Answer {saved_answer.option_text} updated"
        })
    elif request.method == 'DELETE':
        saved_answer.delete()
        return Response({
            "message": f"User Answer with id '{pk}'' was deleted"
        }, status=204)


@api_view(['GET'])
@permission_classes((IsAuthenticated,)) 
def poll_active_view(request):
    survey = Poll.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now())
    serializer = PollSerializer(survey, many=True)
    return Response(serializer.data)