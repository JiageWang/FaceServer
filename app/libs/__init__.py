import json
from app import create_app
from app.models import Embedding
from .arcface.arcface import Arcface
from .mtcnn.mtcnn import MTCNN
import numpy as np


class FaceModel(object):
    def __init__(self):
        self.mtcnn = MTCNN()
        self.arcface = Arcface()
        self.threshold = 0.8
        self.facebank = None
        self.ids = None
        self.update_facebank()

    def update_facebank(self):
        with create_app().app_context():
            embeddings = Embedding.query.all()
            # print(embeddings[0].emd)
            facebank = [np.array(json.loads(embedding.emd.decode('utf-8'))) for embedding in embeddings]
            self.ids = [embedding.sid for embedding in embeddings]
            self.facebank = np.concatenate(facebank, 0) if len(facebank) > 0 else np.array([])

    def get_embedding(self, img):
        bbox, face = self.mtcnn.get_align_face(img)
        if face:
            return self.arcface(face)
        return None

    def compare(self, face):
        if self.facebank is None:
            print('请先初始化facebank')
            return None
        emd = self.get_embedding(face)
        if emd is not None:
            diff = emd - self.facebank
            dist = np.sum(np.square(diff), axis=1)
            min_idx = np.argmin(dist)
            print(dist[min_idx])
            if dist[min_idx] < self.threshold:
                return self.ids[min_idx]
        return None

    # def infer(self, img):
    #     bboxes, faces = self.mtcnn.get_align_face(img)
    #     if faces:
    #         name = self.get_most_similar(faces)
    #         return name
    #     else:
    #         return None
    #
    # def get_most_similar(self, faces):
    #     indexes, scores = self.arcface.infer(faces)
    #     return self.names[indexes[np.argmin(scores)]+1]

    # def get_name(self, img):
    #     bboxes, faces = self.get_bboxes_faces(img)
    #     if len(faces)>0:
    #         names, scores = self.get_most_similar(faces)
    #         return names, scores
    #     return [],[]

    # def defect_faces(self, img):
    #     bboxes, faces = self.mtcnn.get_align_faces(img)
    #     if len(bboxes)>0:
    #         bboxes = bboxes[:, :-1]  # shape:[10,4],only keep 10 highest possibiity faces
    #         bboxes = bboxes.astype(int)
    #         bboxes = bboxes + [-1, -1, 1, 1]  # personal choice
    #     return bboxes, faces

    # def get_result_frame(self, img):
    #     bboxes, faces = self.get_bboxes_faces(img)
    #     if len(faces)>0:
    #         names, scores = self.get_most_similar(faces)
    #         for idx,bbox in enumerate(bboxes):
    #             img = self.__draw_box_name(bbox, self.arcface.names[names[idx] + 1], img)
    #     return img

    # def __draw_box_name(self, bbox, name, img):
    #     img = cv2.rectangle(img,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,0,255),6)
    #     img = self.__put_chinese(img, name, (bbox[0],bbox[1]))
    #     return img
    #
    # @staticmethod
    # def __put_chinese(img, str, position):
    #     # 图像从OpenCV格式转换成PIL格式
    #     img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #     font = ImageFont.truetype('simhei.ttf', 40)
    #     # 需要先把输出的中文字符转换成Unicode编码形式
    #     # str = str.encode('utf8')
    #     draw = ImageDraw.Draw(img)
    #     draw.text(position, str, font=font, fill=(255, 0, 0))
    #     img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    #     return img


face_model = FaceModel()
