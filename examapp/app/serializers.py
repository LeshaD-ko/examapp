from collections import OrderedDict
from operator import itemgetter

from rest_framework.serializers import ModelSerializer
from app.models import Question, Answer_variants, Result, TestedUser, QuestionType, Answer, Correct_answers


class QuestionsTypeSerializer(ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('name',)


class AnswerVariantsSerializer(ModelSerializer):
    class Meta:
        model = Answer_variants
        fields = ('variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6', )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # filter the null values and creates a new dictionary
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret


class Correct_answersSerializer(ModelSerializer):
    class Meta:
        model = Correct_answers
        fields = ('correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5',)


class TestedUserSerializer(ModelSerializer):
    class Meta:
        model = TestedUser
        fields = ('first_name', 'last_name', 'email', )


# used
class QuestionsSerializer(ModelSerializer):
    answer_variants = AnswerVariantsSerializer()

    class Meta:
        model = Question
        fields = ['id', 'question_type', 'question_text', 'question_image', 'answer_variants']


class ResultSerializer(ModelSerializer):
    # user = TestedUserSerializer()

    class Meta:
        model = Result
        fields = ('user_id', 'test', 'points', 'percent')


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = ('user_id', 'question_id', 'answer', 'answer_time')

