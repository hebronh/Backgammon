from cs1graphics import *

size = int(input('Pixels per grid cell: ')) #think 500 hypothetically
paper = Canvas(size,size)
paper.setBackgroundColor('burlywood4')

Backagammon = Layer()

##Gameboards

leftboard = Rectangle(size/15*0.55, size/13, Point(0.265*size,0.51*size))
leftboard.setFillColor('navajowhite')
leftboard.setBorderColor('navajowhite')
leftboard.scale(10.5)

rightboard = Rectangle(size/15*0.55, size/13, Point(0.734*size,0.51*size))
rightboard.setFillColor('navajowhite')
rightboard.setBorderColor('navajowhite')
rightboard.scale(10.5)

Backagammon.add(leftboard)
Backagammon.add(rightboard)


for x in range(1, 7):
#Bottom-Left
        tri = Polygon(Point(x/15*paper.getWidth(), 12/13*paper.getHeight()),
                      Point((x+1)/15*paper.getWidth(), 12/13*paper.getHeight()),
                      Point((x+0.5)/15*paper.getWidth(), 7/13*paper.getHeight()))
        if x % 2 == 1:
            tri.setFillColor('darkorange3')
        else:
            tri.setFillColor('tan')
        tri.setBorderColor('black')
        Backagammon.add(tri)

#Top-Left
        tri = Polygon(Point(x/15*paper.getWidth(), 1.245/13*paper.getHeight()),
                      Point((x+1)/15*paper.getWidth(), 1.245/13*paper.getHeight()),
                      Point((x+0.5)/15*paper.getWidth(), 6/13*paper.getHeight()))
        if x % 2 == 1:
            tri.setFillColor('tan')
        else:
            tri.setFillColor('darkorange3')
        tri.setBorderColor('black')
        Backagammon.add(tri)

#Top-Right
        tri = Polygon(Point((x+7)/15*paper.getWidth(), 1.245/13*paper.getHeight()),
               Point((x+7+1)/15*paper.getWidth(), 1.245/13*paper.getHeight()),
               Point((x+7+0.5)/15*paper.getWidth(), 6/13*paper.getHeight()))
        if x % 2 == 1:
            tri.setFillColor('tan')
        else:
            tri.setFillColor('darkorange3')
        tri.setBorderColor('black')
        Backagammon.add(tri)


#Bottom-Right
        tri = Polygon(Point((x+7)/15*paper.getWidth(), 12/13*paper.getHeight()),
                      Point((x+7+1)/15*paper.getWidth(), 12/13*paper.getHeight()),
                      Point((x+7+0.5)/15*paper.getWidth(), 7/13*paper.getHeight()))
        if x % 2 == 1:
            tri.setFillColor('darkorange3')
        else:
            tri.setFillColor('tan')
        tri.setBorderColor('black')
        Backagammon.add(tri)

#Checkers:
        
for num, pt, whiteOnTop in [(2,1, True),(5,6,False),(3,8,False),(5,12,True)]:
          for c in range(num-1):
            cx = (0.099 * size)
            cx2 = (0.634 * size)
            cx3 = (0.90 * size)
            cy = (0.895*size) 
            cy2 = (0.835*size) 
            cy3 = (2.38/13*size)
            cy4 = (1.60/13*size)
            cy5 = (3.15/13*size)
            cy6 = (10.05/13*size) 
            cy7 = (10.80/13*size) 
            cy8 = (11.60/13*size) 
            cy9 = (10.05/13*size) 
            cy10 = (9.25/13*size)
            cy11 = (8.45/13*size)
            checker = Circle(size * 0.09/3,Point(cx,cy))
            checker2 = Circle(size * 0.09/3,Point(cx,cy2))
            checker3 = Circle(size * 0.09/3, Point(cx2,cy2))
            checker4 = Circle(size * 0.09/3, Point(cx2,cy))
            checker5 = Circle(size*0.09/3, Point(cx2,cy3))
            checker6 = Circle(size*0.09/3, Point(cx2,cy4))
            checker11 = Circle(size*0.09/3, Point(cx2, cy5))
            checker12 = Circle(size*0.09/3, Point(cx2,cy6))
            checker13 = Circle(size * 0.09/3,Point(cx3,cy7))
            checker14 = Circle(size * 0.09/3,Point(cx3,cy8))
            checker15 = Circle(size * 0.09/3,Point(cx3,cy9))
            checker16 = Circle(size * 0.09/3,Point(cx3,cy10))
            checker17 = Circle(size * 0.09/3, Point(cx3,cy11))
            checker18 = Circle(size * 0.09/3, Point(cx3,cy5))
            checker19 =  Circle(size * 0.09/3, Point(cx3,cy4))
            checker20 = Circle(size * 0.09/3, Point(cx3,cy3))
          if pt>6:
            cx += size
          if whiteOnTop == True:
            checker.setFillColor('white')
            checker2.setFillColor('white')
            checker3.setFillColor('black')
            checker4.setFillColor('black')
            checker5.setFillColor('black')
            checker6.setFillColor('black')
            checker11.setFillColor('white')
            checker12.setFillColor('black')
            checker13.setFillColor('white')
            checker14.setFillColor('white')
            checker15.setFillColor('white')
            checker16.setFillColor('white')
            checker17.setFillColor('white')
            checker18.setFillColor('black')
            checker19.setFillColor('black')
            checker20.setFillColor('black')
          else:
            checker.setFillColor('black')
            checker2.setFillColor('black')
            checker3.setFillColor('white')
            checker4.setFillColor('white')
            checker5.setFillColor('black')
            checker6.setFillColor('black')
            checker11.setFillColor('black')
            checker12.setFillColor('white')
            checker13.setFillColor('black')
            checker14.setFillColor('black')
            checker15.setFillColor('black')
            checker16.setFillColor('black')
            checker17.setFillColor('black')
            checker18.setFillColor('white')
            checker19.setFillColor('white')
            checker20.setFillColor('white')
            Backagammon.add(checker)
            Backagammon.add(checker2)
            Backagammon.add(checker3)
            Backagammon.add(checker4) 
            Backagammon.add(checker5)
            Backagammon.add(checker6)
            Backagammon.add(checker11)
            Backagammon.add(checker12)
            Backagammon.add(checker13)
            Backagammon.add(checker14)
            Backagammon.add(checker15)
            Backagammon.add(checker16)
            Backagammon.add(checker17)
            Backagammon.add(checker18)
            Backagammon.add(checker19)
            Backagammon.add(checker20)


for c in range(num+2):
            cx = (0.100*size)
            cy = (1.60/13*size)
            cy2 = (2.38/13*size)
            checker = Circle(size * 0.09/3,Point(cx,cy))
            checker2 = Circle(size * 0.09/3,Point(cx,cy2))
if pt<6:
            cx += size
if whiteOnTop == False:
            checker.setFillColor('black')
            checker2.setFillColor('black')
else:
            checker.setFillColor('white')
            checker2.setFillColor('white')
            Backagammon.add(checker)
            Backagammon.add(checker2)

for c in range(num+2):
            cx = (0.435*size)
            cy = (1.60/13*size) 
            cy13 = (3.94/13*size)
            cy14 = (4.72/13*size)
            cy2 = (0.835*size)
            cy4 = (0.774*size)
            cy12 = (0.713*size)
            cy6 = (0.650*size)
            checker = Circle(size * 0.09/3,Point(cx,cy))
            checker2 = Circle(size * 0.09/3,Point(cx,cy3))
            checker3 = Circle(size * 0.09/3,Point(cx,cy5))
            checker4 = Circle(size * 0.09/3,Point(cx,cy13))
            checker5 = Circle(size * 0.09/3,Point(cx,cy14))
            checker6 = Circle(size * 0.09/3,Point(cx,cy8))
            checker7 = Circle(size * 0.09/3,Point(cx,cy2))
            checker8 = Circle(size * 0.09/3,Point(cx,cy4))
            checker9 = Circle(size * 0.09/3,Point(cx,cy12))
            checker10 = Circle(size * 0.09/3,Point(cx,cy6))
            
if pt<6:
            cx += size
if whiteOnTop == False:
            checker.setFillColor('white')
            checker2.setFillColor('white')
            checker3.setFillColor('white')
            checker4.setFillColor('white')
            checker5.setFillColor('white')
            checker6.setFillColor('black')
            checker7.setFillColor('black')
            checker8.setFillColor('black')
            checker9.setFillColor('black')
            checker10.setFillColor('black')
            checker11.setFillColor('white')
else:
            checker.setFillColor('black')
            checker2.setFillColor('black')
            checker3.setFillColor('black')
            checker4.setFillColor('black')
            checker5.setFillColor('black')
            checker6.setFillColor('white')
            checker7.setFillColor('white')
            checker8.setFillColor('white')
            checker9.setFillColor('white')
            checker10.setFillColor('white')
            checker11.setFillColor('black')
            Backagammon.add(checker)
            Backagammon.add(checker2)
            Backagammon.add(checker3)
            Backagammon.add(checker4)
            Backagammon.add(checker5)
            Backagammon.add(checker6)
            Backagammon.add(checker7)
            Backagammon.add(checker8)
            Backagammon.add(checker9)
            Backagammon.add(checker10)


            
centerbar = Path(Point(0.500*size, 0*size),Point(0.500*size,size))
centerbar.setBorderWidth(3)
Backagammon.add(centerbar)


num1 = Text('1',12)
num1.setFontColor('black')
num1.move(0.10*size,0.945*size)

num2 = Text('2',12)
num2.setFontColor('black')
num2.move(0.17*size,0.945*size)

num3 = Text('3',12)
num3.setFontColor('black')
num3.move(0.235*size,0.945*size)

num4 = Text('4',12)
num4.setFontColor('black')
num4.move(0.299*size,0.945*size)

num5 = Text('5',12)
num5.setFontColor('black')
num5.move(0.370*size,0.945*size)


num6 = Text('6',12)
num6.setFontColor('black')
num6.move(0.440*size,0.945*size)


num7 = Text('7',12)
num7.setFontColor('black')
num7.move(0.570*size,0.945*size)

num8 = Text('8',12)
num8.setFontColor('black')
num8.move(0.635*size,0.945*size)

num9 = Text('9',12)
num9.setFontColor('black')
num9.move(0.698*size, 0.945*size)


num10 = Text('10',12)
num10.setFontColor('black')
num10.move(0.765*size,0.945*size)

num11 = Text('11',12)
num11.setFontColor('black')
num11.move(0.835*size,0.945*size)

num12 = Text('12',12)
num12.setFontColor('black')
num12.move(0.895*size,0.945*size)

num13 = Text('13',12)
num13.setFontColor('black')
num13.move(0.895*size,1.05/13*size)

num14 = Text('14',12)
num14.setFontColor('black')
num14.move(0.835*size, 1.05/13*size)

num15 = Text('15',12)
num15.setFontColor('black')
num15.move(0.770*size, 1.05/13*size)

num16 = Text('16',12)
num16.setFontColor('black')
num16.move(0.700*size, 1.05/13*size)

num17 = Text('17',12)
num17.setFontColor('black')
num17.move(0.635*size, 1.05/13*size)

num18 = Text('18',12)
num18.setFontColor('black')
num18.move(0.570*size, 1.05/13*size)


num19 = Text('19',12)
num19.setFontColor('black')
num19.move(0.435*size, 1.05/13*size)

num20 = Text('20',12)
num20.setFontColor('black')
num20.move(0.365*size, 1.05/13*size)

num21 = Text('21',12)
num21.setFontColor('black')
num21.move(0.301*size, 1.05/13*size)

num22 = Text('22',12)
num22.setFontColor('black')
num22.move(0.235*size,1.05/13*size)

num23 = Text('23',12)
num23.setFontColor('black')
num23.move(0.170*size,1.05/13*size)

num24 = Text('24',12)
num24.setFontColor('black')
num24.move(0.100*size,1.05/13*size)


Backagammon.add(num1)
Backagammon.add(num2)
Backagammon.add(num3)
Backagammon.add(num4)
Backagammon.add(num5)
Backagammon.add(num6)
Backagammon.add(num7)
Backagammon.add(num8)
Backagammon.add(num9)
Backagammon.add(num10)
Backagammon.add(num11)
Backagammon.add(num12)
Backagammon.add(num13)
Backagammon.add(num14)
Backagammon.add(num15) 
Backagammon.add(num16) 
Backagammon.add(num17)
Backagammon.add(num18)
Backagammon.add(num19)
Backagammon.add(num20)
Backagammon.add(num21)
Backagammon.add(num22)
Backagammon.add(num23)
Backagammon.add(num24)

    
paper.add(Backagammon)
