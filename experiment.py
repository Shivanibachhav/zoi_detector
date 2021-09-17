import cv2
import numpy as np
import csv
import os
import glob
import shutil
import math

class Measure:

    def start(self,Image,crop_flag=True):
        try:
            img_name=Image.split('.')[0].split('/')[-1]
            print(img_name)
            #check whether the .csv file is already present
            header_flag=os.path.exists('Record.xlsx')
            img = cv2.imread(Image, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (512, 1111))
            img_=img
            # Convert to grayscale.
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Blur using 3 * 3 kernel.
            gray_blurred = cv2.blur(gray, (5, 3))

            # Apply Hough transform on the blurred image.
            detected_circles = cv2.HoughCircles(gray_blurred,
                                                cv2.HOUGH_GRADIENT, 1, 10, param1=300,
                                                param2=17, minRadius=1, maxRadius=15)
            # detected_circles_b is for big circle
            detected_circles_b = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20,
                                                  param1=100, param2=100, minRadius=30, maxRadius=240)
            # detected_circles_s is for big circle
            detected_circles_s = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 10,
                                                  param1=100, param2=30, minRadius=1, maxRadius=15)

            #########################################################################
            ## Outer and Inner Circle detection code
            # Draw circles that are detected.
            if detected_circles_b is not None:

                # Convert the circle parameters a, b and r to integers.
                detected_circles_b = np.uint16(np.around(detected_circles_b))
                # print(detected_circles_b[0,0:7])
                for pt in detected_circles_b[0, 0:1]:
                    a, b, r = pt[0], pt[1], pt[2]

                    # Draw the circumference of the circle.
                    cv2.circle(img, (a, b), r, (0, 255, 0), 4)

                    # Draw a small circle (of radius 1) to show the center.
                    cv2.circle(img, (a, b), 1, (0, 0, 255), 2)
            i = 0
            label = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
            chk=False
            header=["Patient's Sample Number",'x1(Px)','x1(mm)','Comment', 'x2(Px)','x2(mm)','Comment', 'x3(Px)', 'x3(mm)',
                    'Comment', 'x4(Px)', 'x4(mm)','Comment', 'x5(Px)', 'x5(mm)','Comment', 'x6(Px)', 'x6(mm)',
                    'Comment', 'x7(Px)', 'x7(mm)','Comment', 'x8(Px)', 'x8(mm)','Comment']
            if detected_circles_s is not None:
                test=detected_circles_s
                chk=True

                # Convert the circle parameters a, b and r to integers.
                detected_circles_s1 = np.uint16(np.around(detected_circles_s))
                mm = detected_circles_s1
                mm_=[]
                for pt in mm[0, 0:10]:
                    a, b = pt[0], pt[1]
                    r = 13
                    cv2.circle(img, (a, b), r, (0, 255, 0), 4)

                    #cv2.putText(img, label[i], (a - 15, b + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                    #i += 1
                    #cv2.circle(img, (a, b), 1, (0, 0, 255), 2)
                    mm_.append([a,b,r])
                    # cv2.imshow("Detected Circle small", img)
                    # cv2.waitKey(0)
            # s_sti = detected_circles_s

            # print(s_sti)
            # print(type(s_sti))

            #########################################################################
            ## Zone Detection code
            # block_size = 511
            # constant = 2
            # #th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
            # th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size,
            #                             constant)
            # # cv2.imshow('gaus',th2)
            # # cv2.waitKey(0)

            # img=th2
            data_out = []
            #if detected_circles is not None:
            if detected_circles is not None:
                detected_circles = np.uint16(np.around(detected_circles))
                #detected_circles = np.uint16(np.around(detected_circles))
                for pt in detected_circles[0, :]:
                    x, y, r = pt
                    h = 10

                    while h < 160:

                        #                 print('radius -', h)
                        try:
                            crop_img = img[y - h:y + h, x - h:x + h]
                            gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
                            gray_blurred = cv2.blur(gray, (5, 3))
                            ret, thresh = cv2.threshold(gray_blurred, 100, 255, cv2.THRESH_OTSU)
                            # ret, thresh = cv2.threshold(gray_blurred, 100, 255, 1)
                            edges = gray_blurred  # cv2.Canny(gray_blurred,50,20)
                            kernel = np.ones((5, 5), np.uint8)
                            img_dilation = cv2.dilate(thresh, kernel, iterations=1)
                            img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
                            # if h>60:
                            #     cv2.imshow('test',img_dilation)
                            #     cv2.waitKey(0)

                            detected_circles_1 = cv2.HoughCircles(img_erosion, cv2.HOUGH_GRADIENT, 30, 40,
                                                                  param1=60, param2=1, minRadius=16, maxRadius=60)

                            show2 = crop_img
                            try:
                                if len(detected_circles_1) == 1:

                                    a, b, r_ = detected_circles_1[0, 0]
                                    if h - 5 < a < h + 5 and h - 5 < b < h + 5:
                                        #
                                        cv2.circle(show2, (a, b), r_, (255, 0, 0), 3)
                                        cv2.circle(show2, (a, b), 1, (255, 0, 0), 3)
                                        # cv2.putText(crop_img, 'Gradient - {}'.format(10), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                        #             0.5,
                                        #             (255, 0, 0), 2)
                                        data_out.append([x, y, r_])
                                        break
                                else:
                                    #cv2.imshow("Detected Circle", show2)
                                    #waitKey(0)
                                    pass
                            except:
                                pass
                        except Exception as e:
                            pass
                        h += 5
                i = 0
                res_dict={}
                xx = []
                xx.append(img_name)
                if data_out:
                    j=0
                    print(len(data_out))
                    print(len(mm_))

                    for p in range(len(mm[0])):
                        for q in range(len(mm_)):
                            try:
                                sum1=sum(data_out[p][:2])
                                sum2=sum(mm_[q][:2])
                                print(sum1,sum2)
                                if sum1==sum2 or sum2-3<=sum1<=sum2+3 or sum1-3<=sum2<=sum1+3:
                                    mm_.pop(q)
                                    break
                            except:
                                pass
                    data_out.extend(mm_)
                    for t in data_out:

                        a1, b1, r1 = t
                        #print('Diameter of', label[i], '=', 2 * r1)
                        # print(r1)
                        img=img_
                        cv2.circle(img, (a1, b1), r1, (255, 0, 0), 2)
                        cv2.circle(img, (a1, b1), 1, (255, 0, 0), 3)
                        cv2.line(img, (a1 - r1, b1), (a1, b1), (0, 0, 0), 3)
                        cv2.line(img, (a1 + r1, b1), (a1, b1), (0, 0, 0), 3)
                        # cv2.putText(img, '{}'.format(2 * r1), (a1 - 15, b1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        cv2.putText(img, label[i], (a1 - 15, b1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                        float_value = float(r1)
                        round_value = round(float_value)
                        dia_value = int(round_value) * 2

                        mm_value = math.sqrt(math.pi * dia_value)

                        if mm_value <= 10:

                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Resistant')
                            res_dict[label[i]] = r1

                        elif  10<= mm_value <= 14:

                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Intermediate')
                            res_dict[label[i]] = r1

                        else:

                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Susceptible')
                            res_dict[label[i]] = r1


                        # print(xx)
                        i += 1
                        j+=1

                    #cv2.imshow("Detected Circle", img)
                    #cv2.waitKey(0)



                    #===== If Writing .csv file for first time write headers otherwise write the data into file that is already present
                    if not header_flag:
                        self.write_to_csv(header)
                    self.write_to_csv(xx)
                return [res_dict, img]

                # print(xx)

            elif detected_circles_s is not None:

                detected_circles = np.uint16(np.around(detected_circles_s))
                for pt in detected_circles[0, :]:
                    x, y, r = pt
                    h = 10

                    while h < 160:

                        #                 print('radius -', h)
                        try:
                            crop_img = img[y - h:y + h, x - h:x + h]
                            gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
                            gray_blurred = cv2.blur(gray, (5, 3))
                            ret, thresh = cv2.threshold(gray_blurred, 100, 255, cv2.THRESH_OTSU)
                            # ret, thresh = cv2.threshold(gray_blurred, 100, 255, 1)
                            edges = gray_blurred  # cv2.Canny(gray_blurred,50,20)
                            kernel = np.ones((5, 5), np.uint8)
                            img_dilation = cv2.dilate(thresh, kernel, iterations=1)
                            img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
                            detected_circles_1 = cv2.HoughCircles(img_erosion, cv2.HOUGH_GRADIENT, 30, 40,
                                                                  param1=60, param2=1, minRadius=16, maxRadius=60)

                            show2 = crop_img
                            try:
                                if len(detected_circles_1) == 1:

                                    a, b, r_ = detected_circles_1[0, 0]
                                    if h - 5 < a < h + 5 and h - 5 < b < h + 5:
                                        #
                                        cv2.circle(show2, (a, b), r_, (255, 0, 0), 3)
                                        cv2.circle(show2, (a, b), 1, (255, 0, 0), 3)
                                        # cv2.putText(crop_img, 'Gradient - {}'.format(10), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                        #             0.5,
                                        #             (255, 0, 0), 2)
                                        data_out.append([x, y, r_])
                                        break
                                else:
                                    #cv2.imshow("Detected Circle", show2)
                                    #cv2.waitKey(0)
                                    pass
                            except:
                                pass
                        except:
                            pass
                        h += 5
                i = 0
                res_dict = {}
                xx = []
                xx.append(img_name)
                if data_out:
                    j = 0
                    print(len(data_out))
                    print(len(mm_))

                    for p in range(len(mm[0])):
                        for q in range(len(mm_)):
                            try:
                                sum1 = sum(data_out[p][:2])
                                sum2 = sum(mm_[q][:2])
                                print(sum1, sum2)
                                if sum1 == sum2 or sum2 - 3 <= sum1 <= sum2 + 3 or sum1 - 3 <= sum2 <= sum1 + 3:
                                    mm_.pop(q)
                                    break
                            except:
                                pass
                    data_out.extend(mm_)
                    for t in data_out:

                        a1, b1, r1 = t
                        # print('Diameter of', label[i], '=', 2 * r1)
                        # print(r1)
                        cv2.circle(img, (a1, b1), r1, (255, 0, 0), 2)
                        cv2.circle(img, (a1, b1), 1, (255, 0, 0), 3)
                        cv2.line(img, (a1 - r1, b1), (a1, b1), (0, 0, 0), 3)
                        cv2.line(img, (a1 + r1, b1), (a1, b1), (0, 0, 0), 3)
                        # cv2.putText(img, '{}'.format(2 * r1), (a1 - 15, b1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        cv2.putText(img, label[i], (a1 - 15, b1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                        float_value = float(r1)
                        round_value = round(float_value)
                        dia_value = int(round_value) * 2

                        mm_value = math.sqrt(math.pi * dia_value)

                        if mm_value <= 10:

                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Resistant')
                            res_dict[label[i]] = r1
                        #elif 14 >= mm_value <= 10:

                            #xx.append(2 * r1)
                            #xx.append(round(mm_value))
                            #xx.append('Intermediate')
                            #res_dict[label[i]] = r1

                        elif 10<= mm_value <= 14:

                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Intermediate')
                            res_dict[label[i]] = r1
                        else:
                            xx.append(2 * r1)
                            xx.append(round(mm_value))
                            xx.append('Susceptible')
                            res_dict[label[i]] = r1

                        i += 1
                        j += 1

                    #cv2.imshow("Detected Circle", img)
                    #cv2.waitKey(0)

                    # ===== If Writing .csv file for first time write headers otherwise write the data into file that is already present
                    if not header_flag:
                        self.write_to_csv(header)
                    self.write_to_csv(xx)
                return [res_dict, img]

                # print(xx)


            else:
                # cv2.imshow("Detected Circle", img)
                # cv2.waitKey(0)

                print("########### No Circles detected in given image ############")
        except Exception as e:
            print(e)

    ##Write Data to CSV file(Append Mode)
    def write_to_csv(self,row):
        with open('Record.xlsx', 'a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)


    #########################################################################
    ## Give Input Image File
    # det("Image1.jpg")
# a=Measure()
# a.start(r'C:\Users\Osiya\Desktop\Dessertion\final\images\x_55.jpg')

