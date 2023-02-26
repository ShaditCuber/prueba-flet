
from flet import *
import cv2
  
VID=None
MORIR=False


def main(page:Page):
    def cerrar(e):
        global MORIR
        
        MORIR=True
        # After the loop release the cap object
        
        
        page.clean()
        btn_rp=FilledButton(text="Generar Registro Presencial",width=300,height=45,on_click=btn_click)
        btn_id=FilledButton(text="Generar Informe y Diplomas",width=300,height=45)
        
        # login=TextField(label="Nombre Usuario",hint_text="user")
        # password=TextField(label="Contraseña",hint_text="pass",password=True,can_reveal_password=True)
        
        page.appbar=AppBar(title=Text("Izied"),bgcolor="#6ec63b",center_title=True)
        page.add(
            Container(
                content=Column([
                img,
                btn_rp,
                btn_id
                ],spacing=40)
            )
            )
        
    def btn_click(e):
        global MORIR
        page.clean()
        VID = cv2.VideoCapture(0)
        
        btn_rp=FilledButton(text="X",width=45,height=45,on_click=cerrar)
        
        
        page.add(
        Container(
            content=Column([
                btn_rp
            ],spacing=40)
        )
        )
        # define a video capture object
        MORIR=False
        while(True):
            
            # Capture the video frame
            # by frame
            ret, frame = VID.read()

            
            
            # Display the resulting frame
            cv2.imshow('frame', frame)
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            key=cv2.waitKey(1)
            if  key==ord("q") or MORIR:
                break
        
        VID.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
  
        
    
    page.window_width=300.00
    page.window_height=720.00
    img=Image(
        src=f"izi.ico",
        fit="contain",
        width=300,
        height=100
    )
    btn_rp=FilledButton(text="Generar Registro Presencial",width=300,height=45,on_click=btn_click)
    btn_id=FilledButton(text="Generar Informe y Diplomas",width=300,height=45)
    
    # login=TextField(label="Nombre Usuario",hint_text="user")
    # password=TextField(label="Contraseña",hint_text="pass",password=True,can_reveal_password=True)
    
    page.appbar=AppBar(title=Text("Izied"),bgcolor="#6ec63b",center_title=True)
    page.add(
        Container(
            content=Column([
            img,
            btn_rp,
            btn_id
            ],spacing=40)
        )
        )


app(target=main)
# app(target=main,port=8000,view=WEB_BROWSER)
