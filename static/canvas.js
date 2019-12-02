/* Using canvas to draw digit with mouse. */

var canvas = document.getElementById("digit");
var ctx = canvas.getContext("2d");
var width = canvas.width, height = canvas.height;
var hold = false;
// ctx.lineJoin = 'miter';
// ctx.lineWidth = 15;
// ctx.strokeStyle = '#FFFFFF';
// ctx.strokeRect(0, 0, 200, 200);
// CANVAS EVENTS
// get mouse coordinates relative to canvas
// move to the point 
canvas.onmousedown = function (e) {
    curX = e.clientX - canvas.offsetLeft;
    curY = e.clientY - canvas.offsetTop;
    hold = true;

    prevX = curX;
    prevY = curY;
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
};
// folllow mouse movement and get its coordinates
canvas.onmousemove = function (e) {
    if (hold) {
        curX = e.clientX - canvas.offsetLeft;
        curY = e.clientY - canvas.offsetTop;
        draw();
    }
};

canvas.onmouseup = function (e) {
    hold = false;
};

canvas.onmouseout = function (e) {
    hold = false;
};
// draw line from previous point to current
function draw() {
    ctx.lineWidth = 8;
    ctx.lineCap = "butt";
    ctx.lineJoin = "round";
    ctx.lineTo(curX, curY);
    ctx.stroke();
}


/* Convert image data 3d array to alpha channel matrix */
function img_to_alpha_array(imgData, row_length) {
    var alpha = [];
    var i = 0;

    for (i = 3; i < imgData.length; i = 4 + i) {
        alpha.push(imgData[i]);
    }
    var d = [];
    var r = [];
    var count = 0;
    for (var i = 1; i <= alpha.length; i++) {
        r.push(alpha[i - 1]);
        if (i % row_length == 0) {
            count++;
            // console.log(count);
            d.push(r);
            r = [];
        }
    }
    return d;
}
/* Function called on Test button press.
 */
function save(){
    //Getting image representation as a 3d array from canvas
    var imgdata = ctx.getImageData(0,0,canvas.width, canvas.height);
    var imgalpha = img_to_alpha_array(imgdata.data, canvas.width)
    var data = JSON.stringify(imgalpha)
    //Ajax request to webapp
    var xhr = new XMLHttpRequest();
    xhr.open('POST', "/send");
    xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    xhr.send(data);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {        
           
            ctx.clearRect(0,0,canvas.width, canvas.height);
            ctx.beginPath();
            console.log(xhr.response);  
            document.getElementById('predict').innerHTML = xhr.response;
        }
    }
   
} 