

// function downloadImage(url) {
//     var a = document.createElement("a"); //Create <a>
//     a.href = "data:image/png;base64," + url; //Image Base64 Goes here
//     a.download = "Image.png"; //File name Here
//     a.click(); //Downloaded file
// }

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img_1')
                .attr('src', e.target.result)
                .width(300)
                .height(300);
        };

        reader.readAsDataURL(input.files[0]);

    }
}

function readURL2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img_2')
                .attr('src', e.target.result)
                .width(300)
                .height(300);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function handleDownload(event) {
    event.preventDefault();
}