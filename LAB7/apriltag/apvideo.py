# seenlist = []
# vid = cv2.VideoCapture(0)

# while(True):
#     seenlist = tags
#     ret,frame = vid.read()
#     cv2.imshow('frame',frame)
#     im=frame.copy()

#     procv = multiprocessing.Process(target=apscan,args=(im,))
#     procv.start()
#     procv.join(timeout=0.2)
#     procv.terminate()

#     if proc.exitcode is None :
#         print("No april on the image")
#     elif tags != seenlist:
#         print(tags)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# cv2.destroyAllWindows()
