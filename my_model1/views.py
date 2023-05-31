from rest_framework.response import Response
from rest_framework.views import APIView
from keras.models import load_model
import numpy as np

class ScaraPredict(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = load_model('my_model1\\my_best_model_BO.h5')

    def post(self, request):
        coord = request.data.get("coord")
        angles = self.model.predict(np.array([coord]))[0]
        return Response({"angles": angles.tolist()})
