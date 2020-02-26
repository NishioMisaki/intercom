from head import *
def cam():
  #camraモジュールの準備
  cam = pc.PiCamera()
  cam.resolution = (1200,800)
  
  cam.start_preview()
  print("人が訪ねて来ました。")
  time.sleep(2)
  cam.capture("./sample.jpg")
  cam.stop_preview()
  print("家主は現在外出中です。")
  print("家主へ報告のメールを送信します。")
  