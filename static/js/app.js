$(function() {
    $('input.input-tags').selectize({

        // An array of the initial options available to select; array of objects. 
        // By default this is populated from the original input element. 
        // If your element is a <select> with <option>s specified this property gets populated automatically. 
        // Setting this property is convenient if you have your data as an array and want to automatically generate the <option>s.
        options: [],
      
        // Initial selected values.
        items: [],
      
        // Option groups that options will be bucketed into. 
        // If your element is a <select> with <optgroup>s this property gets populated automatically. 
        // Make sure each object in the array has a property named whatever optgroupValueField is set to.
        optgroups: [],
      
        // Custom delimiter character to separate items
        delimiter: ',',
        splitOn: null, // regexp or string for splitting up values from a paste command
    });      
});

function submitForm(e) {
    document.getElementById("submit-form").submit();
}