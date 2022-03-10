const ImageInputElement = `
<div data-image-input class="wrapper">

    <div data-image-display-box>
        <img src="" alt="">
    </div>

    <div data-image-remove-button>
        <i class="fas fa-times"></i>
    </div>

    <div data-image-caption>
        File name here
    </div>

    <div data-image-upload-box>
        <div class="icon"> <i class="fas fa-cloud-upload-alt"></i> </div>
        <div class="text"> No file chosen, yet! </div>
    </div>

</div>
`;

const regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;


function ImageInput(element) {

    this.ImageButton = element;
    this.ImageInput = $("[data-image-input]");
    this.displayImage = $("[data-image-display-box] img");
    this.removeImage = $("[data-image-remove-button]");
    this.ImageCaption = $("[data-image-caption]");
    this.ImageUploadBox = $("[data-image-upload-box]");


    this.ImageButton.attr("hidden", true);

    console.log(this.ImageButton.data("current-image"));

    if (this.ImageButton.data("current-image")) {
        this.displayImage.attr("src", this.ImageButton.data("current-image"));
        this.ImageInput.addClass("active");
        let valueStore = this.ImageButton.data("current-image").match(regExp);
        this.ImageCaption.text(valueStore);
    }   

    this.removeImage.click((function(e) {
        this.displayImage.removeAttr("src");
        this.ImageInput.removeClass("active");
    }).bind(this));

    this.TriggerClick = (e) => {
        console.log("triggered is called");
        if ($(e.target) != this.displayImage || 
            $(e.target) != this.removeImage || 
            $(e.target) != this.ImageCaption) {
                this.ImageButton.trigger("click");
        }
    }

    this.HandleFileUpload = (e) => {
        const file = e.target.files[0];
        if(file) {
            const reader = new FileReader();
            reader.onload = (function() {
                const image = reader.result;
                this.displayImage.attr("src", image);
                this.ImageInput.addClass("active");
            }).bind(this)

            reader.readAsDataURL(file);
        }

        if(file.name) {
            let valueStore = file.name.match(regExp);
            this.ImageCaption.text(valueStore);
        }
        
    }

    this.ImageUploadBox.click(this.TriggerClick)

    this.ImageButton.change(this.HandleFileUpload);

}

$.fn.ImagePreloadInput = function() {
    this.before(ImageInputElement);
    new ImageInput(this);
    return this;
}
