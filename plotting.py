import matplotlib.pyplot
import math

### functions ###

def domain(init, end, step):
    x = list()
    for i in range(int(init), int(end*(1/step))+1):
        x.append(i*step)
    return x

def image(dom, f):
    y = list()
    for i in range(len(dom)):
        y.append(f(dom[i]))
    return y


def myPlot(x,y):
    yMax = max(y)
    yMin = min(y)

    xMax = max(x)
    xMin = min(x)

    matplotlib.pyplot.plot([xMax, xMin], [0,0], '#000000') #black color
    matplotlib.pyplot.plot([0,0], [yMax, yMin], '#000000')

    matplotlib.pyplot.plot(x,y)
    #matplotlib.pyplot.show()                 
##########################################################

def rms(v):
    accumulator = 0
    for i in range(len(v)):
        accumulator = accumulator + v[i]*v[i]
    accumulator = math.sqrt(accumulator)
    return accumulator

def u(t):
    if t > 0:
        return 1
    return 0

def delta(t):
    if t == 0:
        return 1
    return 0


def frequencyDomain(t):
    result = list()
    for i in range(len(t)):
        if t[i] == 0:
            result.append(float('inf'))
        else:
            result.append(1/t[i])
    return result


def fourierTransform(t, xt ,w):
    integralReal = 0
    integralImaginary = 0
    result = list()
    for i in range(len(t)):
##        print("cos("+str(t[i])+") = "+str((math.cos(w*t[i]))))
##        print("i = "+str(i))
##        if t[i] == 0:
##            print("cos("+str(t[i])+") = "+str((math.cos(w*t[i]))))
##        if t[i] >= 1.4 and t[i] <= 1.6:
##            print("cos("+str(t[i])+") = "+str((math.cos(w*t[i]))))
        integralReal = integralReal + xt[i]*(math.cos(w*t[i]))
        integralImaginary = integralImaginary - xt[i]*(math.sin(w*t[i]))
    result.append(integralReal)
    result.append(integralImaginary)
    return result #[0] = real part and [1] = imaginary part

def numericIntegral(x, y):
    accumulator = 0
    for i in range(1,len(x)):
        accumulator = accumulator + (y(x[i]))*(x[i] - x[i-1])
    return accumulator



t = domain(0,100,0.1)
xt = image(t, u)
w = domain(0,20,0.1)

##xw = list()
##for i in range(len(w)):
##    res = fourierTransform(t,xt,w[i])
##    mag = math.sqrt((res[0]*res[0])+(res[1]*res[1]))
##    xw.append(mag)
##
##myPlot(w,xw)
##
##
##matplotlib.pyplot.show()

a = fourierTransform(t,xt,1)
print(a)
print(rms(a))



def f(x):
    return x*x

x = domain(0,5,0.1)

print(numericIntegral(x,f))
