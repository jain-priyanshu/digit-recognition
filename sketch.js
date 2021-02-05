var drawing = [];
var currentPath = [];
var isDrawing = false;

function setup(){
    canvas = createCanvas(500, 500);
    canvas.mousePressed(startPath);
    canvas.mouseReleased(endPath);
    clearButton = createButton('Clear');
}

function draw(){
    background(100, 255, 255);
    if(isDrawing){
        var pos = {
            x: mouseX,
            y: mouseY
        }
        currentPath.push(pos);
    }
    clearButton.mousePressed(() => {
        drawing = [];
    })
    stroke(0);
    strokeWeight(4);
    noFill();
    for(let i = 0; i < drawing.length; i++){
        var path = drawing[i];
        beginShape();
        for(let j = 0; j < path.length; j++){
            vertex(path[j].x, path[j].y)
        }
        endShape();
    }
} 

function startPath(){
    isDrawing = true;
    currentPath = [];
    drawing.push(currentPath);
}

function endPath(){
    isDrawing = false;
}