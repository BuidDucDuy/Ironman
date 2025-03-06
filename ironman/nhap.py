# import webbrowser as wb 
# def tim_kiem(trang_web) :
#     search = str(input("Nhap lua chon can tim :").lower())
#     url = f"https://www.{trang_web}.com/search?q= {search}"
#     wb.get().open(url.lower())
# # def tim_kiem_you() :
# #     searchy = str(input("Nhap lua chon can tim :"))
# #     url = f"https://www.{searchy}.com/search?q= {searchy}"
# #     wb.get().open(url)
# if __name__ == "__main__" :
#     trang_wb = str(input("nhap trang web : ")).lower()
#     if(trang_wb == "google" or trang_wb == "youtube" or trang_wb == "facebook"):
#         tim_kiem(trang_wb)

# with open("nhap.txt" , "w") as file :
#     file.write("HELLO")
# import speech_recognition as sr 
# def tim_kiem_giong_noi ():
#     nhan_dang = sr.Recognizer
#     with sr.Microphone as mc :
#        nhan_dang.adjust_for_ambient_noise()
# try :
#     x = 10/0
# except Exception as l :
#     print("loi" , l)
# if(10 / 0 == 0):
#     print("khong loi")
# else :
#     print("loi")
# import speech_recognition as sr 
# def nhan_dien_giong_noi():
#     nhan_dang = sr.Recognizer()
#     with sr.Microphone as mc :
#         nhan_dang.adjust_for_ambient_noise(mc)
