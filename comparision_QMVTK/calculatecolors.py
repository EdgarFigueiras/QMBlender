import math

def calculate_color_by_amplitude(amplitude, min, max):
    #Colors array, from dark blue (Lowest probability) to dark red (Highest probability)
    color = [0,0,0]
    
    colorArray = [
                  [0,0,130],
                  [0,0,200],
                  [0,0,255],
                  [0,40,255],
                  [0,90,255],
                  [0,153,255],
                  [1,212,255],
                  [38,255,210],
                  [96,255,150],
                  [134,255,115],
                  [177,255,71],
                  [228,255,20],
                  [255,211,0],
                  [255,163,0],
                  [255,100,0],
                  [255,60,0],
                  [245,10,0],
                  [200,0,0],
                  [155,0,0],
                  [131,0,0]
                  ];
        
    #Calculate the step to use the full range of colours between min and max psi values
    #Calculate the amplitude to adjust the new steps.
    #Amplitude_in_order_0-1 = (Amplitude - minPsi)/(maxPsi-minPsi)
    
    #print("x_ampl = ", amplitude, "-", min, "/(", max , "-", min, ")" )
    x_ampl = (amplitude - min)/(max-min);
    
    #20 steps of colours, amplitude from 0.0 to 1.0
    indexOfColor = math.floor(x_ampl / 0.05);
    
    if (indexOfColor > 19):
        indexOfColor = 19
    
    #print("indexOfColor = ", indexOfColor)
    
                  
    color[0] = colorArray[indexOfColor][0];
    color[1] = colorArray[indexOfColor][1];
    color[2] = colorArray[indexOfColor][2];
                  
    return color