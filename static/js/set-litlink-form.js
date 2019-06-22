
selector_clicked_func = function(){
            // Get id of the selected item
            var choice = $(this).children("option:selected").attr("id");

            console.log(choice + ' clicked')

            // send POST request with option id to flask and receive necessary div
            $.ajax({
                url:"/link_form_selector",
                type: 'POST',
                data: JSON.stringify({'selected_source': choice}),
                dataType: "json",
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    // Add form to the page
                    $("#form-div").empty();
                    $("#form-div").append(response);
                }});





}

// Main function
main = function(){
        // Selector handler
        $("#ll-selector").click(selector_clicked_func)


}

$(document).ready(main)
