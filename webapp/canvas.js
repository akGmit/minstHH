/* Using canvas to draw digit with mouse. */

var canvas = document.getElementById("digit");
var ctx = canvas.getContext("2d");
var width = canvas.width, height = canvas.height;
var hold = false;

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
    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.lineTo(curX, curY);
    ctx.stroke();
}

/* Find rectangular boundries of a digit */
function digit_boundries(imgArr) {
    var x1 = width;
    var y1 = height;
    var x2 = 0;
    var y2 = 0;
    for (var i = 0; i < imgArr.length; i++) {
        for (var j = 0; j < imgArr.length; j++) {
            if (imgArr[i][j] > 0) {
                if (i < y1) y1 = i;
                if (j < x1) x1 = j;
            }
            if (imgArr[width - 1 - i][height - 1 - j] > 0) {
                if (width - 1 - i > y2) y2 = width - 1 - i;
                if (height - 1 - j > x2) x2 = height - 1 - j;
            }
        }
    }
    return { "x1": x1, "x2": x2, "y1": y1, "y2": y2 };
}
/* Convert image data array to alpha channel matrix */
function img_to_alpha_array(imgData, row_length) {
    var alpha = [];
    var i = 0;

    for (i = 3; i < imgData.data.length; i = 4 + i) {
        alpha.push(imgData.data[i]);
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
function test() {

    var c = digit_boundries(img_to_alpha_array(ctx.getImageData(0, 0, width, height), 100));
   
    var img = new Image();
    img.src = canvas.toDataURL("image/png");

    var ctx2 = document.getElementById("resized").getContext("2d");
    
    img.addEventListener("load", function () {
        ctx2.drawImage(img, c.x1, c.y1, c.x2 - c.x1, c.y2 - c.y1, 0, 0, 20, 20);
        var matrix = img_to_alpha_array(ctx2.getImageData(0, 0, 28, 28), 28);
        console.log(matrix);
    });
} 