import time

import cv2
import mediapipe as mp
import math
import numpy as np



def imprimir(direccion):
    print(direccion)
##############

#---------- video capturaa
cap = cv2.VideoCapture(0)
cap.set(3,1280)   #ancho
cap.set(4,720)    #alto

#--------- funcion de dibujo
mpDibujo = mp.solutions.drawing_utils
confDibu = mpDibujo.DrawingSpec(thickness=1,circle_radius=1)


#---------
mpMallaFacial = mp.solutions.face_mesh
MallaFacial = mpMallaFacial.FaceMesh(max_num_faces=1)  # solo un rostro



#-------funcionalidad principal
def a():
    while True:
        ret,frame = cap.read()

        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #------ OBSERVAR RESULTADOS

        resultados = MallaFacial.process(frameRGB)

        #------- listas para almacenar datos

        px = []
        py = []
        lista = []
        r = 5
        t = 3
        img_h, img_w, img_c = frameRGB.shape
        face_3d = []
        face_2d = []

        if resultados.multi_face_landmarks:   # si llega a detectar un rostro

            for rostros in resultados.multi_face_landmarks:
                mpDibujo.draw_landmarks(frame,rostros,mpMallaFacial.FACEMESH_TESSELATION,confDibu,confDibu)

                for id,puntos in enumerate(rostros.landmark):
                    if id == 33 or id == 263 or id == 1 or id == 61 or id == 291 or id == 199:
                        if id == 1:
                            nose_2d = (puntos.x * img_w, puntos.y * img_h)
                            nose_3d = (puntos.x * img_w, puntos.y * img_h, puntos.z * 8000)

                        x, y = int(puntos.x * img_w), int(puntos.y * img_h)

                        # Get the 2D Coordinates
                        face_2d.append([x, y])

                        # Get the 3D Coordinates
                        face_3d.append([x, y, puntos.z])

                    altura,ancho,c = frame.shape
                    x,y = int(puntos.x*ancho),int(puntos.y*altura)
                    px.append(x)
                    py.append(y)
                    lista.append([id,x,y])
                    if len(lista) == 468:

                        # cejasssssss

                        x1_cejas,y1_cejas = lista[65][1:]
                        x2_cejas,y2_cejas = lista[158][1:]
                        cx_cejas,cy_cejas = (x1_cejas+x2_cejas)//2,(y1_cejas+y2_cejas)//2
                        longitud_cejas = math.hypot(x2_cejas-x1_cejas,y2_cejas-y1_cejas) #vector con orgen en las coordenadas indicadas
                        #print(longitud_cejas)



                        #bocaaaaa
                        x1_boca, y1_boca = lista[13][1:]
                        x2_boca, y2_boca = lista[14][1:]
                        cx_boca, cy_boca = (x1_boca + x2_boca) // 2, (y1_boca + y2_boca) // 2
                        #cv2.line(frame,(x1_boca,y1_boca),(x2_boca,y2_boca),(0,0,0),t)
                        #cv2.circle(frame,(x1_boca,y1_boca),r,(0,0,0),cv2.FILLED)
                        #cv2.circle(frame, (x2_boca, y2_boca), r, (0, 0, 0), cv2.FILLED)
                        # cv2.circle(frame, (cx_boca, cy_boca), r, (0, 0, 0), cv2.FILLED)
                        longitud_boca = math.hypot(x2_boca - x1_boca, y2_boca - y1_boca)  # vector con orgen en las coordenadas indicadas
                        #print(longitud_boca)



                        x1_cb, y1_cb = lista[78][1:]
                        x2_cb, y2_cb = lista[308][1:]
                        cx_cb, cy_cb = (x1_cb + x2_cb) // 2, (y1_cb + y2_cb) // 2
                        #cv2.line(frame,(x1_cb,y1_cb),(x2_cb,y2_cb),(0,0,0),t)
                        #cv2.circle(frame,(x1_cb,y1_cb),r,(0,0,0),cv2.FILLED)
                        #cv2.circle(frame, (x2_cb, y2_cb), r, (0, 0, 0), cv2.FILLED)
                        #cv2.circle(frame, (cx_cb, cy_cb), r, (0, 0, 0), cv2.FILLED)
                        longitud_cb = math.hypot(x2_cb - x1_cb,
                                                   y2_cb - y1_cb)  # vector con orgen en las coordenadas indicadas
                        #print(longitud_cb)


                        # movimientos

                        face_2d = np.array(face_2d, dtype=np.float64)

                        # Convert it to the NumPy array
                        face_3d = np.array(face_3d, dtype=np.float64)

                        # The camera matrix
                        focal_length = 1 * img_w

                        cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                               [0, focal_length, img_w / 2],
                                               [0, 0, 1]])

                        # The Distance Matrix
                        dist_matrix = np.zeros((4, 1), dtype=np.float64)

                        # Solve PnP
                        success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                        # Get rotational matrix
                        rmat, jac = cv2.Rodrigues(rot_vec)

                        # Get angles
                        angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                        # Get the y rotation degree
                        x_principal = angles[0] * 360
                        y_principal = angles[1] * 360

                        if y_principal < -10:
                            text = "derecha"
                            return text

                        elif y_principal > 10:
                            text = "izq"
                            return text

                        elif x_principal < -5:
                            text = "abajo"
                            return text

                        elif x_principal > 10:
                            text = "arriba"
                            return text

                        elif longitud_boca > 60:
                            text = "boca"
                            return text


                        elif longitud_cejas > 40:
                            text = "cejas"
                            return text

                        elif longitud_cb > 110:
                            text = "cbbbbb"
                            return text

                        else:
                            text = "centro"

                        cv2.putText(frame, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



        cv2.imshow("juego :)",frame)
        t = cv2.waitKey(1)


    cap.relase()
    cv2.destroyAllWindows()



while True:
    print("su turno")
    print(a())