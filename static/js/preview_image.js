var $inputImage = $('.custom-file-input')
var $preview = $('.img-preview')
var preview = document.getElementsByClassName('img-preview')[0]
$inputImage.on('change', function(e){
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        $preview.attr('src', e.target.result)
    };
    reader.readAsDataURL(file);
    preview.style.display = 'block';
    if (document.getElementsByClassName('img-ticket')[0]) {
        document.getElementsByClassName('img-ticket')[0].style.display = 'none';
    }
});
