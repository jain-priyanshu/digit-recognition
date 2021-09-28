var drawing = [];
var currentPath = [];
var isDrawing = false;
var temp;
function setup(){
    stroke(4);
    canvas = createCanvas(280, 280);
    canvas.mousePressed(startPath);
    canvas.mouseReleased(endPath);
    submitButton = createButton('Submit');
    clearButton = createButton('Clear');
    var myAnswer = document.getElementById('myAnswer');
    var tfAnswer = document.getElementById('tfAnswer');
    submitButton.mousePressed(() => {
        var newCanvas = document.createElement("CANVAS");
        resample_single(canvas.canvas, 28, 28, true, newCanvas);
        var ctx = newCanvas.getContext("2d");
        var imgData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
        var tempData = imgData.data;
        var finalData = [];
        for(var i = 0; i < tempData.length; i += 4){
            var black = (tempData[i] + tempData[i+1] + tempData[i+2]) / 3;
            finalData.push(black);
        }
        finalData = finalData.map((elt) => {
            return 255 - elt;
        })
        var data = {
            arr: finalData
        }
        var options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(data)
        }
        fetch('/', options).then( async (res) => {
            var data = await res.json();
            temp = data;
            print(data)
            myAnswer.innerHTML = data[1];
            tfAnswer.innerHTML = data[2];
        });
    })
}

function draw(){
    background(255);
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
    strokeWeight(20);
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