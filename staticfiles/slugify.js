var titleInput = document.querySelector('input[name=title]');
var slugInput = document.querySelector('input[name=slug]');



var slugify = (val) => {return val.toString().toLowerCase().trim().replace(/&/g, '-and-').replace(/[\s\W-]+/g, '-');};
            // Replace & with 'and'
            // Replace spaces, non-word characters and dashes with a single dash (-

if (titleInput == null){
    
} else {
titleInput.addEventListener('keyup', (e) => {slugInput.setAttribute('value', slugify(titleInput.value));
});
}











