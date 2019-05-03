from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField('date published')
    user_id = serializers.IntegerField(default=0) 

class ChoiceSerializer(serializers.Serializer):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id = serializers.IntegerField()
    choice_text = serializers.CharField(max_length=200)
    votes = serializers.IntegerField(default=0)