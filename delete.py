## Deletes a finger from sensor

from pyfingerprint.pyfingerprint import PyFingerprint

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/serial0', 9600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)


def delete_template_finger_image(x):
    positionNumber=x
    ## Gets some sensor information
    #print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
    #current= str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())
    ## Tries to delete the template of the finger
    try:
        #positionNumber = raw_input('Please enter the template position you want to delete: ')
        positionNumber = int(positionNumber)

        if ( f.deleteTemplate(positionNumber) == True ):
            #print('Template deleted!')
            current= 'Template deleted!'+'Currently used templates:'+str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())
            return current

    except Exception as e:
        m='  '+'Operation failed! '+str(e)+'  '
        #print('Operation failed!')
        #print('Exception message: ' + str(e))
        #exit(1)
        return m

    

'''
while True:
    delete_template_finger_image()
'''
    
#print delete_template_finger_image(2)
