
#EXERCISE 1

def YUVfromRGB(R, G, B ):
    Y=0.257*R + 0.504*G + 0.098*B+16
    U = -0.148*R - 0.291*G + 0.439*B + 128
    V = 0.439*R - 0.368*G - 0.071*B + 128
    return (Y,U,V)

def RGBfromYUV(Y,U,V):
    B=1.164*(Y-16)+2.018*(U-128)
    G=1.164*(Y-16)-0.813*(V-128)-0.391*(U-128)
    R=1.164*(Y-16)+1.596*(V-128)
    return(R,G,B)

what = int(input("Do you want to convert RGB to YUV (1) , or YUV to RGB (2)?: "))
while what>2 or what<1 :
    print("Try again bro")
    what = int(input("Do you want to convert RGB to YUV (1) , or YUV to RGB (2)?: "))

if what ==1:

    R = int(input("The Red value is: "))
    G=int(input("The Green value is: "))
    B=int(input("The Blue value is: "))

    y,u,v = YUVfromRGB(R, G, B )
    print("The conversion from RGB to YUV is", y, u, v)

elif what ==2:
    Y = int(input("The Y value is: "))
    U = int(input("The U value is: "))
    V = int(input("The V value is: "))

    r, g, b = RGBfromYUV(Y, U, V)
    print("The conversion from YUV to RGB is", round(r, 2), round(g, 2),
          round(b, 2))


