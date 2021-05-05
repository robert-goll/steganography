console.log("hello there");
if(window.File && window.FileReader && window.FileList && window.Blob){
    alert("Success");
} else{
    alert("The File API is not supported on your browser. This app will not work.");
}