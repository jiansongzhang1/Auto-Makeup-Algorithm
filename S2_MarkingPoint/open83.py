import requests  
import json
from json import JSONDecoder  
import cv2  
import os  
import itertools
import numpy as np
from matplotlib import pyplot as plt

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
#cat_no_unicode = opt_no_unicode.replace(unicode('utf-8：'), '')

filename = 'E:\MyProject\S2_MarkingPoint_done\Json2point'  
filename2 = 'Adele_B_0.jpg'
filepath = os.path.join(filename, filename2)

with open(filepath+".json",'r') as load_f:
    req_dict = json.load(load_f)
    
#print ("face number =",len(req_dict[u'faces']))  
face_num = len(req_dict[u'faces'])  
frame = cv2.imread(filepath)

lx=[0,0,0,0,0,0,0,0,0,0] #×óÁ³
ly=[0,0,0,0,0,0,0,0,0,0]
rx=[0,0,0,0,0,0,0,0,0,0] #ÓÒÁ³
ry=[0,0,0,0,0,0,0,0,0,0]
lmx=[0,0,0,0,0,0,0,0,0,0] #×ó×ì
lmy=[0,0,0,0,0,0,0,0,0,0]
rmx=[0,0,0,0,0,0,0,0,0,0] #ÓÒ×ì
rmy=[0,0,0,0,0,0,0,0,0,0]
nx=[0,0,0,0,0,0,0,0,0,0,0] #±Ç×Ó
ny=[0,0,0,0,0,0,0,0,0,0,0]
lex=[0,0,0,0,0,0,0,0,0,0,0] #×óÑÛ
ley=[0,0,0,0,0,0,0,0,0,0,0]
rex=[0,0,0,0,0,0,0,0,0,0,0] #ÓÒÑÛ
rey=[0,0,0,0,0,0,0,0,0,0,0]
lbx=[0,0,0,0,0,0,0,0,0] #×óÃ¼
lby=[0,0,0,0,0,0,0,0,0]
rbx=[0,0,0,0,0,0,0,0,0] #ÓÒÃ¼
rby=[0,0,0,0,0,0,0,0,0]

for i in range(face_num):  
    #print ("person:", face_num)
    point = req_dict[u'faces'][i][u'landmark'] 
    #print(point)  
    cx=point[u'contour_chin'][u'x'] #ÏÂ°Í
    cy=point[u'contour_chin'][u'y']
    
    lx[1]=point[u'contour_left1'][u'x'] #×óÁ³
    lx[2]=point[u'contour_left2'][u'x']
    lx[3]=point[u'contour_left3'][u'x']
    lx[4]=point[u'contour_left4'][u'x']
    lx[5]=point[u'contour_left5'][u'x']
    lx[6]=point[u'contour_left6'][u'x']
    lx[7]=point[u'contour_left7'][u'x']
    lx[8]=point[u'contour_left8'][u'x']
    lx[9]=point[u'contour_left9'][u'x']
    
    ly[1]=point[u'contour_left1'][u'y'] 
    ly[2]=point[u'contour_left2'][u'y']
    ly[3]=point[u'contour_left3'][u'y']
    ly[4]=point[u'contour_left4'][u'y']
    ly[5]=point[u'contour_left5'][u'y']
    ly[6]=point[u'contour_left6'][u'y']
    ly[7]=point[u'contour_left7'][u'y']
    ly[8]=point[u'contour_left8'][u'y']
    ly[9]=point[u'contour_left9'][u'y']
    
    rx[1]=point[u'contour_right1'][u'x'] #ÓÒÁ³
    rx[2]=point[u'contour_right2'][u'x']
    rx[3]=point[u'contour_right3'][u'x']
    rx[4]=point[u'contour_right4'][u'x']
    rx[5]=point[u'contour_right5'][u'x']
    rx[6]=point[u'contour_right6'][u'x']
    rx[7]=point[u'contour_right7'][u'x']
    rx[8]=point[u'contour_right8'][u'x']
    rx[9]=point[u'contour_right9'][u'x']
    
    ry[1]=point[u'contour_right1'][u'y']
    ry[2]=point[u'contour_right2'][u'y']
    ry[3]=point[u'contour_right3'][u'y']
    ry[4]=point[u'contour_right4'][u'y']
    ry[5]=point[u'contour_right5'][u'y']
    ry[6]=point[u'contour_right6'][u'y']
    ry[7]=point[u'contour_right7'][u'y']
    ry[8]=point[u'contour_right8'][u'y']
    ry[9]=point[u'contour_right9'][u'y']
    
    lmx[1]=point[u'mouth_left_corner'][u'x'] #×ó×ì
    lmx[2]=point[u'mouth_lower_lip_bottom'][u'x']
    lmx[3]=point[u'mouth_lower_lip_left_contour1'][u'x']
    lmx[4]=point[u'mouth_lower_lip_left_contour2'][u'x']
    lmx[5]=point[u'mouth_lower_lip_left_contour3'][u'x']
    lmx[6]=point[u'mouth_lower_lip_right_contour1'][u'x']
    lmx[7]=point[u'mouth_lower_lip_right_contour2'][u'x']
    lmx[8]=point[u'mouth_lower_lip_right_contour3'][u'x']
    lmx[9]=point[u'mouth_lower_lip_top'][u'x']
    
       
    lmy[1]=point[u'mouth_left_corner'][u'y'] 
    lmy[2]=point[u'mouth_lower_lip_bottom'][u'y']
    lmy[3]=point[u'mouth_lower_lip_left_contour1'][u'y']
    lmy[4]=point[u'mouth_lower_lip_left_contour2'][u'y']
    lmy[5]=point[u'mouth_lower_lip_left_contour3'][u'y']
    lmy[6]=point[u'mouth_lower_lip_right_contour1'][u'y']
    lmy[7]=point[u'mouth_lower_lip_right_contour2'][u'y']
    lmy[8]=point[u'mouth_lower_lip_right_contour3'][u'y']
    lmy[9]=point[u'mouth_lower_lip_top'][u'y']
    
    rmx[1]=point[u'mouth_right_corner'][u'x'] #ÓÒ×ì
    rmx[2]=point[u'mouth_upper_lip_bottom'][u'x']
    rmx[3]=point[u'mouth_upper_lip_left_contour1'][u'x']
    rmx[4]=point[u'mouth_upper_lip_left_contour2'][u'x']
    rmx[5]=point[u'mouth_upper_lip_left_contour3'][u'x']
    rmx[6]=point[u'mouth_upper_lip_right_contour1'][u'x']
    rmx[7]=point[u'mouth_upper_lip_right_contour2'][u'x']
    rmx[8]=point[u'mouth_upper_lip_right_contour3'][u'x']
    rmx[9]=point[u'mouth_upper_lip_top'][u'x']
    
    rmy[1]=point[u'mouth_right_corner'][u'y'] 
    rmy[2]=point[u'mouth_upper_lip_bottom'][u'y']
    rmy[3]=point[u'mouth_upper_lip_left_contour1'][u'y']
    rmy[4]=point[u'mouth_upper_lip_left_contour2'][u'y']
    rmy[5]=point[u'mouth_upper_lip_left_contour3'][u'y']
    rmy[6]=point[u'mouth_upper_lip_right_contour1'][u'y']
    rmy[7]=point[u'mouth_upper_lip_right_contour2'][u'y']
    rmy[8]=point[u'mouth_upper_lip_right_contour3'][u'y']
    rmy[9]=point[u'mouth_upper_lip_top'][u'y']
    
     
    nx[1]=point[u'nose_contour_left1'][u'x'] #±Ç×Ó
    nx[2]=point[u'nose_contour_left2'][u'x'] 
    nx[3]=point[u'nose_contour_left3'][u'x'] 
    nx[4]=point[u'nose_contour_lower_middle'][u'x'] 
    nx[5]=point[u'nose_contour_right1'][u'x'] 
    nx[6]=point[u'nose_contour_right2'][u'x'] 
    nx[7]=point[u'nose_contour_right3'][u'x'] 
    nx[8]=point[u'nose_left'][u'x'] 
    nx[9]=point[u'nose_right'][u'x'] 
    nx[10]=point[u'nose_tip'][u'x'] 
    
    ny[1]=point[u'nose_contour_left1'][u'y'] #±Ç×Ó
    ny[2]=point[u'nose_contour_left2'][u'y'] 
    ny[3]=point[u'nose_contour_left3'][u'y'] 
    ny[4]=point[u'nose_contour_lower_middle'][u'y'] 
    ny[5]=point[u'nose_contour_right1'][u'y'] 
    ny[6]=point[u'nose_contour_right2'][u'y'] 
    ny[7]=point[u'nose_contour_right3'][u'y'] 
    ny[8]=point[u'nose_left'][u'y'] 
    ny[9]=point[u'nose_right'][u'y'] 
    ny[10]=point[u'nose_tip'][u'y']
    
    lex[1]=point[u'left_eye_bottom'][u'x'] #×óÑÛ
    lex[2]=point[u'left_eye_center'][u'x']
    lex[3]=point[u'left_eye_left_corner'][u'x']
    lex[4]=point[u'left_eye_lower_left_quarter'][u'x']
    lex[5]=point[u'left_eye_lower_right_quarter'][u'x']
    lex[6]=point[u'left_eye_pupil'][u'x']
    lex[7]=point[u'left_eye_right_corner'][u'x']
    lex[8]=point[u'left_eye_top'][u'x']
    lex[9]=point[u'left_eye_upper_left_quarter'][u'x']
    lex[10]=point[u'left_eye_upper_right_quarter'][u'x']
    
    ley[1]=point[u'left_eye_bottom'][u'y'] 
    ley[2]=point[u'left_eye_center'][u'y']
    ley[3]=point[u'left_eye_left_corner'][u'y']
    ley[4]=point[u'left_eye_lower_left_quarter'][u'y']
    ley[5]=point[u'left_eye_lower_right_quarter'][u'y']
    ley[6]=point[u'left_eye_pupil'][u'y']
    ley[7]=point[u'left_eye_right_corner'][u'y']
    ley[8]=point[u'left_eye_top'][u'y']
    ley[9]=point[u'left_eye_upper_left_quarter'][u'y']
    ley[10]=point[u'left_eye_upper_right_quarter'][u'y']
    
    rex[1]=point[u'right_eye_bottom'][u'x'] #ÓÒÑÛ
    rex[2]=point[u'right_eye_center'][u'x']
    rex[3]=point[u'right_eye_left_corner'][u'x']
    rex[4]=point[u'right_eye_lower_left_quarter'][u'x']
    rex[5]=point[u'right_eye_lower_right_quarter'][u'x']
    rex[6]=point[u'right_eye_pupil'][u'x']
    rex[7]=point[u'right_eye_right_corner'][u'x']
    rex[8]=point[u'right_eye_top'][u'x']
    rex[9]=point[u'right_eye_upper_left_quarter'][u'x']
    rex[10]=point[u'right_eye_upper_right_quarter'][u'x']
    
    rey[1]=point[u'right_eye_bottom'][u'y'] 
    rey[2]=point[u'right_eye_center'][u'y']
    rey[3]=point[u'right_eye_left_corner'][u'y']
    rey[4]=point[u'right_eye_lower_left_quarter'][u'y']
    rey[5]=point[u'right_eye_lower_right_quarter'][u'y']
    rey[6]=point[u'right_eye_pupil'][u'y']
    rey[7]=point[u'right_eye_right_corner'][u'y']
    rey[8]=point[u'right_eye_top'][u'y']
    rey[9]=point[u'right_eye_upper_left_quarter'][u'y']
    rey[10]=point[u'right_eye_upper_right_quarter'][u'y']
      
    lbx[1]=point[u'left_eyebrow_left_corner'][u'x'] #×óÃ¼
    lbx[2]=point[u'left_eyebrow_lower_left_quarter'][u'x']
    lbx[3]=point[u'left_eyebrow_lower_middle'][u'x']
    lbx[4]=point[u'left_eyebrow_lower_right_quarter'][u'x']
    lbx[5]=point[u'left_eyebrow_right_corner'][u'x']
    lbx[6]=point[u'left_eyebrow_upper_left_quarter'][u'x']
    lbx[7]=point[u'left_eyebrow_upper_middle'][u'x']
    lbx[8]=point[u'left_eyebrow_upper_right_quarter'][u'x']
    
    lby[1]=point[u'left_eyebrow_left_corner'][u'y'] 
    lby[2]=point[u'left_eyebrow_lower_left_quarter'][u'y']
    lby[3]=point[u'left_eyebrow_lower_middle'][u'y']
    lby[4]=point[u'left_eyebrow_lower_right_quarter'][u'y']
    lby[5]=point[u'left_eyebrow_right_corner'][u'y']
    lby[6]=point[u'left_eyebrow_upper_left_quarter'][u'y']
    lby[7]=point[u'left_eyebrow_upper_middle'][u'y']
    lby[8]=point[u'left_eyebrow_upper_right_quarter'][u'y']
    
    rbx[1]=point[u'right_eyebrow_left_corner'][u'x'] #ÓÒÃ¼
    rbx[2]=point[u'right_eyebrow_lower_left_quarter'][u'x']
    rbx[3]=point[u'right_eyebrow_lower_middle'][u'x']
    rbx[4]=point[u'right_eyebrow_lower_right_quarter'][u'x']
    rbx[5]=point[u'right_eyebrow_right_corner'][u'x']
    rbx[6]=point[u'right_eyebrow_upper_left_quarter'][u'x']
    rbx[7]=point[u'right_eyebrow_upper_middle'][u'x']
    rbx[8]=point[u'right_eyebrow_upper_right_quarter'][u'x']
    
    rby[1]=point[u'right_eyebrow_left_corner'][u'y'] 
    rby[2]=point[u'right_eyebrow_lower_left_quarter'][u'y']
    rby[3]=point[u'right_eyebrow_lower_middle'][u'y']
    rby[4]=point[u'right_eyebrow_lower_right_quarter'][u'y']
    rby[5]=point[u'right_eyebrow_right_corner'][u'y']
    rby[6]=point[u'right_eyebrow_upper_left_quarter'][u'y']
    rby[7]=point[u'right_eyebrow_upper_middle'][u'y']
    rby[8]=point[u'right_eyebrow_upper_right_quarter'][u'y']
    
    #×ø±ê
    '''
    print "chin:"
    print 'cx =',cx,'cy =',cy
    print "left face:"
    for j in range (9):
        print 'lx[',j+1,'] =',lx[j+1],'ly[',j+1,'] =',ly[j+1]
    print "right face:"
    for j in range (9):
        print 'rx[',j+1,'] =',rx[j+1],'ry[',j+1,'] =',ry[j+1]
    print "left mouse:"
    for j in range (9):
        print 'lmx[',j+1,'] =',lmx[j+1],'lmy[',j+1,'] =',lmy[j+1]
    print "right mouse:"
    for j in range (9):
        print 'rmx[',j+1,'] =',rmx[j+1],'rmy[',j+1,'] =',rmy[j+1]
    print "nose:"
    for j in range (10):
        print 'nx[',j+1,'] =',nx[j+1],'ny[',j+1,'] =',ny[j+1]
    print "left eye:"
    for j in range (10):
        print 'lex[',j+1,'] =',lex[j+1],'ley[',j+1,'] =',ley[j+1]
    print "right eye:"
    for j in range (10):
        print 'rex[',j+1,'] =',rex[j+1],'rey[',j+1,'] =',rey[j+1]
    print "left eyebrow:"
    for j in range (8):
        print 'lbx[',j+1,'] =',lbx[j+1],'lby[',j+1,'] =',lby[j+1]
    print "right eyebrow:"
    for j in range (8):
        print 'rbx[',j+1,'] =',rbx[j+1],'rby[',j+1,'] =',rby[j+1]
    '''
    #»æÍ¼
    cv2.circle(frame,(cx,cy),1,(0,255,0),-1)
    for j in range (9):
        cv2.circle(frame,(lx[j+1],ly[j+1]),1,(0,255,0),-1)
        cv2.circle(frame,(rx[j+1],ry[j+1]),1,(0,255,0),-1)
    for j in range (9):    
        cv2.circle(frame,(lmx[j+1],lmy[j+1]),1,(0,255,0),-1)
        cv2.circle(frame,(rmx[j+1],rmy[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(nx[j+1],ny[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(lex[j+1],ley[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(rex[j+1],rey[j+1]),1,(0,255,0),-1)
    for j in range (8):    
        cv2.circle(frame,(lbx[j+1],lby[j+1]),1,(0,255,0),-1)
    for j in range (8):    
        cv2.circle(frame,(rbx[j+1],rby[j+1]),1,(0,255,0),-1)


lx.remove(0);rx.remove(0);lmx.remove(0);rmx.remove(0);nx.remove(0);lex.remove(0);rex.remove(0);lbx.remove(0);rbx.remove(0)
ly.remove(0);ry.remove(0);lmy.remove(0);rmy.remove(0);ny.remove(0);ley.remove(0);rey.remove(0);lby.remove(0);rby.remove(0)
pointsx=itertools.chain([cx],lx,rx,lmx,rmx,nx,lex,rex,lbx,rbx)
pointsy=itertools.chain([cy],ly,ry,lmy,rmy,ny,ley,rey,lby,rby)
pointsx1=list(pointsx)
pointsy1=list(pointsy)
#print (pointsx1,'\n',pointsy1)
#print (len(pointsx1))

#np.savetxt(filename2, (pointsx1, pointsy1))

 #plt.imshow(frame,"faceDetecion")

cv2.imwrite("point_"+filename2,frame) 
#cv2.imshow("faceDetecion", frame)          
#c = cv2.waitKey(0)     
#cv2.destroyAllWindows()   