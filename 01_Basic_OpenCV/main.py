import cv2
import sys

def start_video_stream(source):
    #hàm kết nối và hiển thị lường từ camera hoặc file.
    print(f"đang kết nối tới nguồn : {source}")
    
    #khởi tạo một đối tượng VideoCapture
    cap = cv2.VideoCapture(source)
    
    #kiểm tra xem có mở được luồng camera không 
    if not cap.isOpened():
        print("Lỗi: không thể mở được video stream hoặc luồng camera")
        sys.exit()
        
    print("Kết nối thành công!")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            #đọc từng khung hình 
            # ret: luận lý logic True nếu đọc thành công, ngược lại false nếu không thể kết nối 
            # frame: ma trận điểm ảnh (hình ảnh thực tế)
            print("Không thể nhận khung hình (Stream kết thúc hoặc mất kết nối )")
            break
        # tùy chọn: giảm kích thước khung hình cho vừa kích thước màn hình 
        # giảm kích thước giúp thuật toán AI chạy nhanh hơn ở các giai đoạn sau
        frame_resized = cv2.resize(frame, (1024,576))
        
        # hiển thị khung hình lên cửa sổ 
        cv2.imshow('Traffic camera VMS - Giai doan 1', frame_resized)
        
        #chờ 1ms và kiểm tra xem người dùng có nhấn phím 'q' không để thoát
        # dùng cv2.waitkey(1) cho live stream (RTSP)
        # nếu dùng file m4p có thể tăng waitkey(25) để video chiếu đúng tốc độ thực 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("đã nhận lệnh thoát từ người dùng")
            break
        
if __name__ == "__main__":
    # các biến thể có thể điều chỉnh
    VIDEO_SOURCE = "http://192.168.120.128:8080/video"
    start_video_stream(VIDEO_SOURCE)