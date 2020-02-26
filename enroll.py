import time
from pyfingerprint.pyfingerprint import PyFingerprint


## Enrolls new finger

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/serial0', 9600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

def Enroll_New_Finger():
    ## Gets some sensor information
    #print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to enroll new finger
    try:
        #print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            #print('Template already exists at position #' + str(positionNumber))
            exist = '   '+'     '+'Template already exists at position:'+str('%03d'%positionNumber)+'     '+'         '+'        '+'          '+'       '
            return(exist)
            #exit(0)

        #print('Remove finger...')
        #time.sleep(2)

        #print('Waiting for same finger again...')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers and creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        #print('Finger enrolled successfully!')
        #print('New template position #' + str(positionNumber))

        data = 'Enrolled successfully!'+'New template position:'+str('%03d'%positionNumber)+' | '+'Currently used templates:'+str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())
        return data

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

'''
while True:
    Enroll_New_Finger()
'''
#Enroll_New_Finger()
