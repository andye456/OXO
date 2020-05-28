# MLOXO
_n_-dimentional Noughts and Crosses
## References

In this repo there is a Q-Learning jupyter notebook which can be used from a 
notebook running anywhere. 

I used it from a Docker image on my AWS. (http://35.176.56.125:8888/notebooks/Q-Learning.ipynb)


Create a container from one in the Docker repo

    docker create --name tensor-test -p 8888:8888 tensorflow/tensorflow:latest-py3-jupyter
 
(NOTE: The recommended jupyter-latest doesn’t seem to work (maybe it’s using Python 3.8 which doesn’t work with TF)

    docker create --name tensor-test -p 8888:8888 tensorflow/tensorflow:jupyter-latest)

Start the container

    docker start -i tensor-test

    docker cp Q-Learning.ipynb tensor-test:/tf/notebooks/Q-Learning.ipynb

Create the new changed docker image:

    docker commit tensor-test
This will create a new version of the docker image, to view it use:

    docker images
Add a tag to the image:

    docker tag a68119c8fd51 basic-demo
Stop the current docker image and deploy the new one.

    docker ps

    docker stop tensor-test
    docker rm tensor-test
Create a new Docker container based on the image just created run it interactively

    docker run -i --name demo1 -d -p 80:8888 basic-demo
Then you can stop and start it at will:

    docker stop demo1
    docker start -i demo1


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