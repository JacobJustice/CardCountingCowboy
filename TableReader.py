# Import necessary packages
import cv2
import numpy as np
import time
import os
from card_detector import Cards
from card_detector import VideoStream

class TableReader():
    def __init__(self):
        ### ---- INITIALIZATION ---- ###
        # Define constants and initialize variables

        ## Camera settings
        self.IM_WIDTH = 1280
        self.IM_HEIGHT = 720 
        self.FRAME_RATE = 10

        ## Initialize calculated frame rate because it's calculated AFTER the first time it's displayed
        self.frame_rate_calc = 1
        self.freq = cv2.getTickFrequency()

        ## Define font to use
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        # Initialize camera object and video feed from the camera. The video stream is set up
        # as a seperate thread that constantly grabs frames from the camera feed. 
        # See VideoStream.py for VideoStream class definition
        ## IF USING USB CAMERA INSTEAD OF PICAMERA,
        ## CHANGE THE THIRD ARGUMENT FROM 1 TO 2 IN THE FOLLOWING LINE:
        self.videostream = VideoStream.VideoStream((self.IM_WIDTH,self.IM_HEIGHT),self.FRAME_RATE,2,0).start()
        time.sleep(1) # Give the camera time to warm up
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.train_ranks = Cards.load_ranks( self.path + '/card_detector/Card_Imgs/')
        self.train_suits = Cards.load_suits( self.path + '/card_detector/Card_Imgs/')
        #print(train_ranks,train_suits)

    def get_table_state(self):
        cards = []
        # Grab frame from video stream
        image = self.videostream.read()

        # Start timer (for calculating frame rate)
        t1 = cv2.getTickCount()

        # Pre-process camera image (gray, blur, and threshold it)
        pre_proc = Cards.preprocess_image(image)
        #cv2.imshow("preprocessimage",pre_proc)
    	
        # Find and sort the contours of all cards in the image (query cards)
        cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

        # If there are no contours, do nothing
        if len(cnts_sort) != 0:

            # Initialize a new "cards" list to assign the card objects.
            # k indexes the newly made array of cards.
            k = 0

            # For each contour detected:
            for i in range(len(cnts_sort)):
                if (cnt_is_card[i] == 1):

                    # Create a card object from the contour and append it to the list of cards.
                    # preprocess_card function takes the card contour and contour and
                    # determines the cards properties (corner points, etc). It generates a
                    # flattened 200x300 image of the card, and isolates the card's
                    # suit and rank from the image.
                    cards.append(Cards.preprocess_card(cnts_sort[i],image))

                    # Find the best rank and suit match for the card.
                    cards[k].best_rank_match,cards[k].best_suit_match,cards[k].rank_diff,cards[k].suit_diff = Cards.match_card(cards[k],self.train_ranks,self.train_suits)
                    

                    # Draw center point and match result on the image.
                    image = Cards.draw_results(image, cards[k])
                    k = k + 1
                    # Draw card contours on image (have to do contours all at once or # they do not show up properly for some reason)
                    if (len(cards) != 0):
                        #print(cards)
                        temp_cnts = []
                        for i in range(len(cards)):
                            temp_cnts.append(cards[i].contour)
                            cv2.drawContours(image,temp_cnts, -1, (255,0,0), 2)

        cv2.drawContours(image,cnts_sort, -1, (255,0,0), 2)
        # Draw framerate in the corner of the image. Framerate is calculated at the end of the main loop,
        # so the first time this runs, framerate will be shown as 0.
        #cv2.putText(image,"FPS: "+str(int(frame_rate_calc)),(10,26),font,0.7,(255,0,255),2,cv2.LINE_AA)

        # Finally, display the image with the identified cards!
        #cv2.imshow("Card Detector",image)

        # Calculate framerate
#        t2 = cv2.getTickCount()
#        time1 = (t2-t1)/self.freq
#        frame_rate_calc = 1/time1

        key = cv2.waitKey(1) & 0xFF

        return cards

    def stop_video_stream(self):
        self.videostream.stop()

if __name__=='__main__':
    table_reader = TableReader()
    while True:
        cards = table_reader.get_table_state()
    #    for k in range(len(cards)):
    #        print(cards[k].best_rank_match,cards[k].best_suit_match, cards[k].center)
        print([(k.best_rank_match, k.center) for k in cards])
        time.sleep(.1)

#    table_reader.stop_video_stream()
