from gpio import *
from time import *

def main():
    pinMode(0,INPUT)
    pinMode(1,OUT)
    print("Fire Alarm System");
    while True:
        fire = digitalRead(0);
        print(fire);
        if(fire==1023):
            customWrite(1,'1');
            customWrite(2, HIGH);
        else:
            customWrite(1,'0');
            customWrite(2, LOW);
if __name__ =="__main__":
    main()