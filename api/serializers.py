from rest_framework import serializers
from .models import Poll, Question, Option, UserAnswer


class DefaultUser(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id
    
    def __call__(self):
        return self.user_id


class UserAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=DefaultUser())
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    option = serializers.SlugRelatedField(queryset=Option.objects.all(), slug_field='id', allow_null=True)
    option_text = serializers.CharField(max_length=250, allow_null=True, required=False)

    class Meta:
        model = UserAnswer
        fields = '__all__'
    
    def create(self, validated_data):
        return UserAnswer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class OptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    option_text = serializers.CharField(max_length=250)

    class Meta:
        model = Option
        fields = '__all__'
    
    def create(self, validated_data):
        return Option.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def validate(self, attrs):
        try:
            obj = Option.objects.get(question=attrs['question'].id, option_text=attrs['option_text'])
        except Option.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError("Option is already exixst")


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=250)
    question_type = serializers.CharField(max_length=250)
    option = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
    
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def validate(self, attrs):
        question_type =attrs['question_type']
        if question_type == 'TEXT' or question_type == 'ONEOPTION' or question_type == 'MANYOPTION':
            return attrs
        raise serializers.ValidationError('Type must be text, one option or many option')


class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=128)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=400)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
    
    def create(self, validated_data):
        return Poll.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'start_date': 'You can"t change it!'})
        
        instance.title = validated_data.get('title', instance.title)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
    
        instance.save()
        return instance

