from PIL import Image, ImageDraw , ImageFont

def generate_bars(bars):
    
    main_width = 600
    
    bar_color = "#b2ffff"
    height_of_one_bar = 30
    space_between_bar = 10
    
    font_size = 16
    
    fnt = ImageFont.truetype('fonts/RedHat/RedHatDisplay-Bold.ttf', font_size)

    if len(bars) == 1: 
        w, h = main_width, height_of_one_bar
        shape = [(0 , 0), (w , h)] 

        img = Image.new('RGBA', (main_width, height_of_one_bar), (0,0,0,0))
        hex_img = ImageDraw.Draw(img)  
        hex_img.rounded_rectangle(shape, fill=bar_color,radius=3)  
        
    else:
        total = sum(bars)
        
        final_height = len(bars)*height_of_one_bar + (len(bars) - 1)*space_between_bar
        
        img = Image.new('RGBA', (main_width, final_height), (0,0,0,0))
        
        for i in range(len(bars)):
            rec_img = Image.new('RGBA', (main_width, height_of_one_bar), (0,0,0,0))               
            
            width = (bars[i]/total)*main_width
            
            percantage = f"{round((bars[i]/total)*100,1)}%"
            
            height_pixel = i*(height_of_one_bar + space_between_bar)

            w, h = width, height_of_one_bar
            shape = [(0 , 0), (w , h)]     
            
            hex_img = ImageDraw.Draw(rec_img)  
            hex_img.rounded_rectangle(shape, fill=bar_color,radius=3)
            
            hex_width = width + 10
            hex_height = int((height_of_one_bar/2) - (font_size/2))
                
            hex_img.text((hex_width , hex_height), percantage, fill=(255,255,255), font=fnt)
            
            img.paste(rec_img, (0, height_pixel), mask=rec_img)
             
    img.show()

generate_bars([1,2,3,4,5])