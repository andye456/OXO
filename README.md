# MLOXO
_n_-dimentional Noughts and Crosses
## References
Higher-Dimensional Tic-Tac-Toe | Infinite Series

https://www.youtube.com/watch?v=FwJZa-helig


## Strategy
#### 2D Board
    (x,y)
    0,0 | 0,1 | 0,2
    ---------------
    1,0 | 1,1 | 1,2
    ---------------
    2,0 | 2,1 | 2,2

###
    [0,0],[0,1],[0,2] = WIN
    [0,0],[1,1],[2,2] = WIN
    [0,0],[1,0],[2,0] = WIN
    [0,0],[1,1],[2,0] = not WIN
###
    if (x1=x2=x3 and y2=y1+1 and y3=y1+2)
        WIN
    elif (y1=y2=y3 and x2=x1+1 and x3=x1+2)
        WIN
    elif (x2=x1+1 and x3=x1+2 and y2=y1+1 and y3=y1+2)
        WIN
    elif (x2=x1+1 and x3=x1+2 and y2=y1-1 and y3=y1-2
        WIN
    
* A winning row has all x coords the same 
* A winning col has all y coords the same
* A winning diagonal has all x and y incrementing by 1 or decrementing by 1
* So either one set of coords is the same or both are different.
#### 3D Board
    (x,y,z)
    1,1,1 | 1,2,1 | 1,3,1
    ---------------------
    2,1,1 | 2,2,1 | 2,3,1
    ---------------------
    3,1,1 | 3,2,1 | 3,3,1
    
    1,1,2 | 1,2,2 | 1,3,2
    ---------------------
    2,1,2 | 2,2,2 | 2,3,2
    ---------------------
    3,1,2 | 3,2,2 | 3,3,2
    
    1,1,3 | 1,2,3 | 1,3,3
    ---------------------
    2,1,3 | 2,2,3 | 2,3,3
    ---------------------
    3,1,3 | 3,2,3 | 3,3,3

###

    [1,1,1],[2,2,1],[3,3,1] = WIN x1=x1 x2=x1+1 X3=X2+1 & y1=y1 y2=y1+1 y3=y2+1
    [1,1,1],[2,2,2],[3,3,3] = WIN 
    [1,2,1],[2,2,2],[3,2,3] = WIN
    [1,1,1],[2,1,1],[2,1,2] = not WIN