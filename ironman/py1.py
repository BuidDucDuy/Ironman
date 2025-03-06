
import pyttsx3 as py
import datetime
import speech_recognition as sr 
import webbrowser as wb 

khoi_tao_giong_noi = py.init()
luu_tru_giong_noi = khoi_tao_giong_noi.getProperty("voices")
khoi_tao_giong_noi.setProperty("voice" , luu_tru_giong_noi[1].id)

def giong_noi(noi) :
    khoi_tao_giong_noi.say(noi)
    khoi_tao_giong_noi.runAndWait()
    

def thoi_gian():
    thoi_gian_hien_tai = datetime.datetime.now().strftime("%I:%M:%p")
    print("now time : " + thoi_gian_hien_tai)
    giong_noi("Now time" + thoi_gian_hien_tai)
def season():
    gio = datetime.datetime.now().hour
    if(gio > 6 and gio <12):
        giong_noi("good morning" + name)
        print("good morning" + name)
    elif(gio > 12 and gio < 18):
        giong_noi("good afternoon" + name)
        print("afternoon" + name)
    else :
        giong_noi("good night" + name)
        print("good night "+name)
def nhan_dang_giong_noi() :
    print("listening ----")
    nhan_dang = sr.Recognizer() 
    with sr.Microphone() as mc :
        nhan_dang.pause_threshold = 2 
        nhan_dang.adjust_for_ambient_noise(mc)
        thu_am_giong_noi = nhan_dang.listen(mc)
    try:
        print("Dang thu nhap hiong noi")
        query = nhan_dang.recognize_google(thu_am_giong_noi , language = "en") 
    except sr.UnknownValueError:
        print("pleas repeat ")
        query = str(input("Your order : "))
    return query
def tim_kiem(query) :
    giong_noi("your order website ")
    wb_search = str(input("Your order wrbsite: ")).lower() 
    search = query #str(input("Your order : "))
    if wb_search in ["google" , "youtube" , "facebook"]:
        url = f"https://www.{wb_search}.com/search?q={search}"  
        wb.open(url)
        
    else :
        giong_noi("error")
        print("eroor")
 
if __name__ == "__main__":
    name = input("Moi ban nhap ten : ")
    giong_noi("hello" + name)
    giong_noi("can i help you")
    
    query  = nhan_dang_giong_noi()
    while True :
        if query :
            tim_kiem(query)

    # thoi_gian()
# import pyttsx3 
# import datetime as dt
# import webbrowser as wb
# import speech_recognition as sr
# khoi_tao_giong_noi = pyttsx3.init()
# luu_tru_giong_noi = khoi_tao_giong_noi.getProperty("voices")
# khoi_tao_giong_noi.setProperty("voice" , luu_tru_giong_noi[1].id)

# def giong_noi(noi):
#     khoi_tao_giong_noi.say(noi)
#     khoi_tao_giong_noi.runAndWait()
    
# def thoi_gian():
#     thoi_gian_hien_tai = dt.datetime.now().strftime("%I:%M:%p")
#     giong_noi(thoi_gian_hien_tai)
#     print("Now time : " + thoi_gian_hien_tai)
    
# def season():         
#     season = dt.datetime.now().hour
#     if(6 < season < 12):
#         giong_noi("Good morning : " + name)
#         print("Good morning : " + name)
#     elif( 12 < season < 18) :
#         giong_noi("Good afternoon " + name )
#         print("Good afternoon " + name )
#     else :
#         giong_noi("Good night" + name)               
#         print("Good night" + name)         

# def nhan_dang_giong_noi():
#     nhan_dang = sr.Recognizer()
#     print("Dang nghe")
#     with sr.Microphone() as mc :
#         nhan_dang.pause_threshold = 0.5
#         nhan_dang.adjust_for_ambient_noise(mc)
#         thu_am_giong_noi = nhan_dang.listen(mc)
#     try :
#         print("dang xu li giong noi")
#         query = nhan_dang.recognize_google(thu_am_giong_noi , language= 'en')
#     except sr.UnknownValueError :
#         query = str(input("nhap van ban"))
#     return query   
# def search_wb(query) :
#     searchwb = "youtube"
#     search = query
#     url = f'https://www.{searchwb}.com/search?q={search}'
#     if searchwb in ["facebook" , "google" , "yotube"]:
#         wb.open(url)
    
# if (__name__) == "__main__" :
#     name = str(input("Moi nhap ten cua ban : "))
#     giong_noi("hello " + name )
#     print("hello " + name)
    
#     thoi_gian()
    
#     season()
    
#     query = nhan_dang_giong_noi()
#     search_wb(query)
        
#     # nhan_dang_giong_noi()